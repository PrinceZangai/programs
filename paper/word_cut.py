import pandas as pd
from pyhanlp import *
import pkuseg
import numpy as np
import jieba
from jieba import posseg





#标点符号替换
def clearpunctuations(str,punctuation):
    for s in punctuation:
        str=str.replace(s,' ')
    return str


# print(text_df)


#hanlp
# word_cut['hanlp']=text_df['review'][:100].apply(lambda x:HanLP.extractPhrase(x,300))

#pkuseg
# word_cut['pkuseg']=text_df['review'][:100].apply(lambda x:pkuseg.pkuseg(model_name='web').cut(x))
# word_cut.to_excel('word_cut.xlsx')

#jieba


# word_cut['jieba']=text_df['review'].apply(lambda x:jieba.lcut(x))
#筛选出指定词性的词
def seg_accord_pos(sentence,pos):
    sen_seg=[]
    for pair in jieba.posseg.cut(sentence):
        if pair.flag in pos:
            sen_seg.append(pair.word)
    return sen_seg


#计算词频
def word_freq(text):
    freq_dict={}
    for sentence in text:
        for word in sentence:
            if word in freq_dict.keys():
                freq_dict[word]+=1
            else:
                freq_dict[word]=1
    return freq_dict

#n-gram
def generate_word_matrix(corpus,word_freq):
    n=word_freq.size
    word_matrix=pd.DataFrame(np.zeros((n,n)),columns=word_freq.index,index=word_freq.index)
    for doc in corpus:
        for index,value in enumerate(doc):
            if index<len(doc)-1:
                word_matrix[doc[index+1]][value]+=1
    return word_matrix

def clear_single(word_list):#去除单个词
    new_word_list=[word for word in word_list if len(word)>1]
    return new_word_list

def cut_word_to_file():#分词后保存为xlsx文件
    jieba.load_userdict('mydict.txt')
    data_source_filename = 'shop_review.csv'
    word_cut = pd.DataFrame()
    text_df = pd.read_csv(data_source_filename)
    punc = ['：', '[', ']', '。', '【', '】', '!', '(', ')', '.', '~', '「', '」', '——', '-', '…']
    text_df['review'] = text_df['review'].apply(lambda x: clearpunctuations(x, punc))
    word_cut['jieba']=text_df['review'].apply(lambda x:[i for i in jieba.lcut(x) if i!=' 'and i!='，'])#去除空格和逗号
    word_cut['jieba_pos']=text_df['review'].apply(lambda x:jieba.posseg.lcut(x))
    word_cut['jieba_pos_n']=text_df['review'].apply(seg_accord_pos,args={'pos':['n','ns','m']})
    word_cut['jieba_pos_nv']=text_df['review'].apply(seg_accord_pos,args={'pos':['n','ns']})
    # word_cut['clear_single']=word_cut['jieba_pos'].apply(clear_single)
    word_cut.to_excel('word_cut_jieba.xlsx')
    return word_cut
#n-gram
#
# all_word_freq=word_freq(word_cut['jieba'])
# all_word_freq=pd.Series(all_word_freq,name='frequence').to_frame()
# # all_word_freq.sort_values('frequence',inplace=True,ascending=False)
# word_matrix=generate_word_matrix(word_cut['jieba'],all_word_freq)

cut_word_to_file()
# word_cut.to_excel('word_cut_jieba.xlsx')
print()