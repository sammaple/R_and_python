# coding=utf-8

#import pandas as pd
#csv_reader = pd.read_csv('data_06.csv')
import csv
csv_reader = csv.reader(open('new22.csv',encoding='utf-8'))

siglist_h = []
siglist_j = []
siglist_d = []
siglist_z = []
import re
for row in csv_reader:
    if(row[0] == '1' and row[2] == '1'):
        try :
            print(row[0],row[3])
        except UnicodeDecodeError :
            print ("parse error")
        else :
            signature_pre = row[3].strip().replace("@我在建湖想小心", "").replace("@我爱周星驰", "").replace("@小心我来了", "").replace("@我要去西藏", "")
            rep = re.compile("1f\d+\w*|[<>/=]")
            signature = rep.sub("", signature_pre)
            siglist_h.append(signature)

print(siglist_h)
text = "".join(siglist_h)
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("wechat.jpg"))
my_wordcloud = WordCloud(background_color="white", max_words=50,
                         mask=coloring, max_font_size=60, random_state=42, scale=2,
                         font_path="SimHei.ttf").generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
