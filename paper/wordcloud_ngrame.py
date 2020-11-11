# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:26:58 2020

@author: Txin
"""


import pandas as pd
from pandas import DataFrame as df
import numpy as np

import jieba
import jieba.analyse

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




#分词并去停用词      
def cut_sentence_and_remove_stop_words(sentence,stopwords):
    word_list=jieba.lcut(sentence)
    new_word_list = []
    for word in word_list:
        if word in stopwords:
            # print "stopword: %s" % word
            continue
        else:
            new_word_list.append(str(word))
    return new_word_list

#统计词频
def list_to_frequence_dict(word_list):
    word_dict=dict()
    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    return word_dict
    
#生成3-gram
def list_3_ngram(sentence,n=3,m=2):
    if len(sentence)<n:
        n=len(sentence)
    temp=[sentence[i-k:i] for k in range(m,n+1) for i in range(k,len(sentence)+1)]
    temp=[i for i in temp if len(set(i))>=m]
    return [item for item in temp if len(''.join(item).strip())>0]


#过滤掉其他词汇，只保留关键词
def key_words_filter(word_list,keywords_list):
    return [word for word in word_list if word in keywords_list]
            
            
if __name__=='__main__':

    data_source_filename='shop_review.xlsx'
    # stopwords_filename='source_data/stop_words_small.txt'
    stopwords_filename='source_data/stop_words.txt'
    # keywords_filename='source_data/key_words.csv'
    
    stopwords=list()
    with open(stopwords_filename,'r',encoding ='utf-8') as f:
        stopwords_org = f.readlines()
        for word in stopwords_org:
            stopwords.append(word.split('\n')[0])
        stopwords.append(' ')
        stopwords.append('\n')
        stopwords.append('\t')

    # keywords_list=list()
    # with open(keywords_filename,'r',encoding ='utf-8') as f:
    #     keywords_org = f.readlines()
    #     for word in keywords_org:
    #         keywords_list.append(word.split('\n')[0])
    #
    # pattern=re.compile(u'[0-9a-zA-Z\u4E00-\u9FA5]')
    # pattern1=re.compile(r'[0-9]')
    ############Step1:读取数据############
    text_df=pd.read_excel(data_source_filename)
    
    ############Step2:分词并且去掉停用词############
    text_df['review']=text_df['review'].apply(lambda x:cut_sentence_and_remove_stop_words(x,stopwords))
    #text_df= text_df[:100]
    
    ############Step3:生成3-gram并去掉数字############
    #text_df['review_ngram']=text_df['review'].apply(lambda x:[' '.join(['_'.join(i) for i in list_3_ngram(x,n=3, m=1)])][0])
    text_df['review_ngram']=text_df['review'].apply(lambda x:[''.join(i) for i in list_3_ngram(x,n=3, m=2)])

    ############Step4:只保留key_words(key_words是根据tfidf筛选保留的)############
    #text_df['review_ngram']=text_df['review_ngram'].apply(lambda x:[i for i in key_words_filter(x,keywords_list)])

    
    ############Step5:统计词频############
    all_review_list=list(chain.from_iterable(text_df['review_ngram'].tolist()))

    all_review=' '.join(all_review_list)
    all_review_frequencies=list_to_frequence_dict(all_review_list)
    
    #将词频写入文档，并为每个次赋予id
    all_review_df=df(pd.Series(all_review_frequencies),columns=['frequence'])
    all_review_df=all_review_df.reset_index().rename(columns={'index':'word'})
    all_review_df.sort_values("frequence",ascending=False,inplace=True)
    all_review_df=all_review_df.reset_index(drop = True)
    all_review_df.to_csv('text_information/words_frequence_all_2.csv',index_label='word_id',encoding ='utf-8')
    
    ############Step6:筛选出高频词############
    filter_num=20
    high_words=sorted(all_review_frequencies.items(),reverse=True,key=lambda x:x[1])
    filter_word_list=[x for (x,_) in high_words][:filter_num]

    
    ############Step7:生成图云############
    bg=imread('foo.jpg')
    wc=WordCloud(background_color='white',
                 max_words=200,
                 mask=bg, #Set the background of the picture
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
    my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
    #产生背景图片，基于彩色图像的颜色生成器
    image_colors=ImageColorGenerator(bg)
    #开始画图
    plt.imshow(wc,interpolation="bilinear")
    #去掉云图坐标
    plt.axis("off")
    plt.show()
    wc.to_file("word_picture/all_review_wordcloud_ngram.png")

    
    ############Step7:基于brand生成图云############
    groups=text_df.groupby('brand')
    file_path='word_picture\\brand'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    for brand,group in groups:
        #print (brand,group)
        review_list=list(chain.from_iterable(group['review_ngram'].tolist()))
        review_frequencies=list_to_frequence_dict(review_list)
        
        review_frequencies_df=df(pd.Series(review_frequencies),columns=['frequence'])
        review_frequencies_df=review_frequencies_df.reset_index().rename(columns={'index':'word'})
        review_frequencies_df.sort_values("frequence",ascending=False,inplace=True)
        review_frequencies_df=review_frequencies_df.reset_index(drop = True)
        review_frequencies_df.to_csv('text_information/words_frequence'+str(brand)+'_2.csv',index=False,encoding ='utf-8')
    
            
        #过滤掉高频词 
        for key in list(review_frequencies.keys()):
            if key in filter_word_list:
                del review_frequencies[key]
        
        picture_filename=os.path.join(file_path,brand+'_wordcloud_ngram.png')
        #brand_review_frequencies=sorted(brand_review_frequencies.items(),reverse=True,key=lambda x:x[1])
        wc.generate_from_frequencies(review_frequencies)
        plt.imshow(wc)
        my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
        image_colors=ImageColorGenerator(bg)
        plt.imshow(wc,interpolation="bilinear")
        plt.axis("off")
        plt.show()
        wc.to_file(picture_filename)
        
        
    ############Step8:基于level生成图云############
    groups=text_df.groupby('level')
    file_path='word_picture\\level'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    for level,group in groups:
        #print (brand,group)
        review_list=list(chain.from_iterable(group['review_ngram'].tolist()))
        review_frequencies=list_to_frequence_dict(review_list)

        #过滤掉高频词
        
        for key in list(review_frequencies.keys()):
            if key in filter_word_list:
                del review_frequencies[key]
        
        picture_filename=os.path.join(file_path,'level'+str(level)+'_wordcloud_ngram.png')
        #brand_review_frequencies=sorted(brand_review_frequencies.items(),reverse=True,key=lambda x:x[1])
        wc.generate_from_frequencies(review_frequencies)
        plt.imshow(wc)
        my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
        image_colors=ImageColorGenerator(bg)
        plt.imshow(wc,interpolation="bilinear")
        plt.axis("off")
        plt.show()
        wc.to_file(picture_filename)