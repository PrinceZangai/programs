# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:21:36 2020

@author: Txin
"""

import pandas as pd
from pandas import DataFrame as df
import numpy as np
from pyhanlp import *

from itertools import chain #这个方法可以将[[1,2],[3,4]]展开成[1,2,3,4]
import os
import re
import gc

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.font_manager as fm
from imageio import imread

from sklearn.feature_extraction.text import TfidfTransformer #计算各篇文档的TF-IDF矩阵 
from sklearn.feature_extraction.text import CountVectorizer #统计各篇文档的词频用

from scipy.spatial.distance import pdist   # 用来计算余弦距离
# import ckpe


#统计词频
def list_to_frequence_dict(word_list):
    word_dict=dict()
    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    return word_dict
    

TOP_N=1000
data_source_filename= 'source_data/shop_review.csv'

############Step1:读取数据############
text_df=pd.read_csv(data_source_filename)

#加载分词模型
###使用hanlp提取关键词
text_df['review']=text_df['review'].apply(lambda x:HanLP.extractPhrase(x,300))

##使用ckpe提取关键词
#ckpe_obj = ckpe.ckpe()
#text_df['review']=text_df['review'].apply(lambda x:ckpe_obj.extract_keyphrase(x,300,stricted_pos=False,stop_word_num=5))

all_review_list=list(chain.from_iterable(text_df['review'].tolist()))

all_review=' '.join(all_review_list)
all_review_frequencies=list_to_frequence_dict(all_review_list)

#将词频写入文档，并为每个词赋予id
all_review_df=df(pd.Series(all_review_frequencies),columns=['frequence'])

#reset_index()函数将原索引作为一列，以整数作为新索引
#rename()函数替换原索引或列名
all_review_df=all_review_df.reset_index().rename(columns={'index':'word'})
all_review_df.sort_values("frequence",ascending=False,inplace=True)
all_review_df=all_review_df.reset_index(drop = True)
all_review_df.to_csv('text_information/words_frequence_all_hanlp.csv',index_label='word_id',encoding ='utf-8')

all_review_frequencies=sorted(all_review_frequencies.items(),reverse=True,key=lambda x:x[1])

############Step6:筛选出高频词############
filter_num=20
filter_word_list=[x for (x,_) in all_review_frequencies][:filter_num]


############Step7:生成图云############
# bg=imread('foo.jpg')
wc=WordCloud(background_color='white',
             max_words=200,
             # mask=bg, #Set the background of the picture
             max_font_size=200,
             width=1000,
             height=1000,
             random_state=60,
             font_path='C:/Windows/Fonts/simkai.ttf'
             )

#传入画词云图的文本
#wc.generate(all_review)
#基于词频生成云图
wc.generate_from_frequencies(dict(all_review_frequencies))
plt.imshow(wc)
#为图片设置字体
# my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
#产生背景图片，基于彩色图像的颜色生成器
# image_colors=ImageColorGenerator(bg)
#开始画图
plt.imshow(wc,interpolation="bilinear")
#去掉云图坐标
plt.axis("off")
plt.show()
wc.to_file("word_picture/all_review_wordcloud_hanlp.png")


############Step7:基于brand生成图云############
groups=text_df.groupby('shop_name')
file_path='word_picture\\shop'
if not os.path.exists(file_path):
    os.makedirs(file_path)
for shop,group in groups:
    #print (brand,group)
    review_list=list(chain.from_iterable(group['review'].tolist()))
    review_frequencies=list_to_frequence_dict(review_list)

    review_frequencies_df=df(pd.Series(review_frequencies),columns=['frequence'])
    review_frequencies_df=review_frequencies_df.reset_index().rename(columns={'index':'word'})
    review_frequencies_df.sort_values("frequence",ascending=False,inplace=True)
    review_frequencies_df=review_frequencies_df.reset_index(drop = True)
    review_frequencies_df.to_csv('text_information/words_frequence'+str(shop)+'_hanlp.csv',index=False,encoding ='utf-8')


    #过滤掉高频词
    for key in list(review_frequencies.keys()):
        if key in filter_word_list:
            del review_frequencies[key]

    picture_filename=os.path.join(file_path,shop+'_wordcloud_hanlp.png')
    #brand_review_frequencies=sorted(brand_review_frequencies.items(),reverse=True,key=lambda x:x[1])
    wc.generate_from_frequencies(review_frequencies)
    plt.imshow(wc)
    my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
    # image_colors=ImageColorGenerator(bg)
    plt.imshow(wc,interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wc.to_file(picture_filename)

#
############Step8:基于level生成图云############
groups=text_df.groupby('level')
file_path='word_picture\\level'
if not os.path.exists(file_path):
    os.makedirs(file_path)
for level,group in groups:
    #print (brand,group)
    review_list=list(chain.from_iterable(group['review'].tolist()))
    review_frequencies=list_to_frequence_dict(review_list)

    #过滤掉高频词
    
    for key in list(review_frequencies.keys()):
        if key in filter_word_list:
            del review_frequencies[key]
    
    picture_filename=os.path.join(file_path,'level'+str(level)+'_wordcloud_hanlp.png')
    #brand_review_frequencies=sorted(brand_review_frequencies.items(),reverse=True,key=lambda x:x[1])
    wc.generate_from_frequencies(review_frequencies)
    plt.imshow(wc)
    my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
    # image_colors=ImageColorGenerator(bg)
    plt.imshow(wc,interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wc.to_file(picture_filename)

