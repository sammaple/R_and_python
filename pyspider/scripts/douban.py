#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-08-04 11:36:23
# Project: douban

from pyspider.libs.base_handler import *
import re
import json

class Handler(BaseHandler):
    crawl_config = {
        "headers": {
            "Referer":"https://movie.douban.com/tag/",
        },
    }
    
    #def __init__(self):
    #    self.base_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start='
    #    self.page_num = 0
    #    self.total_num = 30

    @every(minutes=24 * 60)
    def on_start(self):
        
        self.base_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start='
        self.page_num = 0
        self.total_num = 2
        ##self.crawl('https://movie.douban.com/tag/#/', fetch_type='js', callback=self.index_page, validate_cert=False)
        #self.crawl('https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0',fetch_type='js', callback=self.index_page, validate_cert=False)
        
        while self.page_num < self.total_num:
            url = self.base_url + str(self.page_num*20) #¶ÁÈ¡Ç°600²½Æ¬×Ó
            print (url)
            self.crawl(url,fetch_type='js',callback=self.index_page, validate_cert=False)
            self.page_num += 1

    @config(age= 60)
    def index_page(self, response):
        details = response.doc.text()
        ##print(json.dumps(details))
        details_json = json.loads(details)
        
        for each in details_json['data']:
            #print (type(each))
            #print (each.get('url')) 
            urlx = each.get('url')
            self.crawl(urlx, fetch_type='js', callback=self.detail_page, validate_cert=False)
            
        
        ##for each in response.doc('a[href^="http"]').items():
        #    print(each) 
        #    if re.match("https://movie.douban.com/subject/\w+", each.attr.href, re.U):
        ##        self.crawl(each.attr.href, callback=self.list_page, validate_cert=False)

    @config(age= 10,priority=2)
    def detail_page(self, response):
        #print(response.doc('#info').text().split(":")[5].replace("ÓïÑÔ",""))
        res =  {
            "url": response.url,
            "title": response.doc('title').text(),
            "rate": response.doc('#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong').text(),
            "director": response.doc('#info > span:nth-child(1) > span.attrs > a').text(),
            "scriptwriter": response.doc('#info > span:nth-child(3) > span.attrs').text(),
            "actor": response.doc('#info > span.actor > span.attrs').text(),
            "style": response.doc('#info > span[property="v:genre"]').text(),
            #"country": [x.text() for x in response.doc('#info)],
            "country": response.doc('#info').text().replace("¹Ù·½ÍøÕ¾:","").replace("http:","").split(":")[5].replace("ÓïÑÔ",""),
            "date": response.doc('#content > h1 > span.year').text(),
            "time": response.doc('#info > span[property="v:runtime"]').text(),
        }
        #print (res)
        return res