#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-08-02 20:48:06
# Project: sohu

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.sohu.com/', callback=self.index_page)

    @config(age= 60)
    def index_page(self, response):
        for each in response.doc('div[class="list16"]').items():
            detail_url = each('a').attr.href
            print (detail_url)
            self.crawl(detail_url, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        header = response.doc('head > title')
        print(header.text())
        return {
            "title": header.text()
            }
        
