import pandas as pd
from gensim.corpora import Dictionary
from pyhanlp import *
import pkuseg
import numpy as np
import jieba
from jieba import posseg
from matplotlib import pyplot as plt

from wordcloud import WordCloud

from gensim.models import Phrases
from gensim.models import LdaModel



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
    return ','.join(sen_seg)


#计算词频,text为arrayLike对象，每一个元素为一句评论分词后结果
def word_freq(text):
    freq_dict={}
    for sentence in text:
        for word in sentence:
            if word in freq_dict.keys():
                freq_dict[word]+=1
            else:
                freq_dict[word]=1
    return freq_dict

def word_freq2(word_list):
    freq_dict = {}
    for word in word_list:
        if word in freq_dict.keys():
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
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
    jieba.load_userdict('source_data/mydict.txt')
    data_source_filename = 'source_data/shop_review.csv'
    word_cut = pd.DataFrame()
    text_df = pd.read_csv(data_source_filename)
    punc = ['：', '[', ']', '。', '【', '】', '!', '(', ')', '.', '~', '「', '」', '——', '-', '…']
    text_df['review'] = text_df['review'].apply(lambda x: clearpunctuations(x, punc))
    word_cut['jieba']=text_df['review'].apply(lambda x:','.join([i for i in jieba.lcut(x) if i!=' 'and i!='，']))#去除空格和逗号
    word_cut['jieba_pos']=text_df['review'].apply(lambda x:jieba.posseg.lcut(x))
    word_cut['jieba_pos_n']=text_df['review'].apply(seg_accord_pos,pos=['n','ns','nz','a','m','i','vn','nr'])
    word_cut['jieba_pos_nv']=text_df['review'].apply(seg_accord_pos,pos=['n','ns','nz'])
    # word_cut['clear_single']=word_cut['jieba_pos'].apply(clear_single)
    word_cut.to_excel('word_cut_jieba.xlsx')
    return word_cut

#
# all_word_freq=word_freq(word_cut['jieba'])
# all_word_freq=pd.Series(all_word_freq,name='frequence').to_frame()
# # all_word_freq.sort_values('frequence',inplace=True,ascending=False)
# word_matrix=generate_word_matrix(word_cut['jieba'],all_word_freq)


#生成词云图，查看效果
def generate_wordcloud(word_frequence,picturefile):

    wc = WordCloud(background_color='white',
                   max_words=200,
                   # mask=bg, #Set the background of the picture
                   max_font_size=200,
                   width=1000,
                   height=1000,
                   random_state=60,
                   font_path='C:/Windows/Fonts/simkai.ttf'
                   )

    wc.generate_from_frequencies(dict(word_frequence))
    wc.to_file(picturefile)
    plt.imshow(wc)
    plt.imshow(wc, interpolation="bilinear")
    # 去掉云图坐标
    plt.axis("off")
    plt.show()

def ldatrain(docs,num_topics):

    dictionary = Dictionary(docs)
    dictionary.filter_extremes(no_below=100, no_above=0.5)
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    id2word = dictionary
    chunksize = 2000
    passes = 20
    iterations = 1000
    eval_every = None

    topics_list={}
    for i in range(4,num_topics):
        model = LdaModel(
            corpus=corpus,
            id2word=id2word,
            chunksize=chunksize,
            alpha='auto',
            eta='auto',
            iterations=iterations,
            num_topics=i,
            passes=passes,
            eval_every=eval_every
        )
        top_topics = model.top_topics(corpus)
        print(top_topics)
        topics_list[i]=top_topics
        model.clear()

    topicfile= pd.DataFrame(dict([(k, pd.Series(v)) for k, v in topics_list.items()]))

    topicfile.to_excel('topicfile2.xlsx')


def preprocess(texts):
    # docs=[[token for token in doc if len(token>1)] for doc in docs]


    with open('source_data/stop_words.txt',encoding='utf-8') as f:
        stopwords=f.readlines()
    stopwords=[stopword.strip() for stopword in stopwords]
    wordfreq = word_freq(texts)
    wordfreq=pd.Series(wordfreq)
    wordfreq.sort_values(ascending=False,inplace=True)
    exclude_word=wordfreq[:10].index  #去掉高频词
    docs=[]
    for doc in texts:
        doc=[word for word in doc if word not in exclude_word and len(word)>1 and word not in stopwords]
        docs.append(doc)
    return docs


    #2-gram
    # bigram = Phrases(docs)
    # for idx in range(len(docs)):
    #     for token in bigram[docs[idx]]:
    #         if '_' in token:
    #             docs[idx].append(token)

    # docs = [[token for token in doc if len(token) > 1] for doc in docs]



    # for idx in range(len(docs)):
    #     for token in bigram[docs[idx]]:


def main():


    # for attr in ['jieba','jieba_pos_n','jieba_pos_nv']:
    #     word_list=[]
    #     for sentence in text_df[attr]:
    #         if isinstance(sentence,str):
    #             sentence=sentence.split(',')
    #             word_list.extend(sentence)
    #     wordfreq=word_freq2(word_list)
    #     wordfreq=pd.Series(wordfreq)
    #     wordfreq.sort_values(ascending=False,inplace=True)
    #     wordfreq=wordfreq[20:]
    #     generate_wordcloud(wordfreq,'word_picture/'+attr+'.png')
    #

    text_df=pd.read_excel('word_cut_jieba.xlsx')
    docs = text_df['jieba_pos_nv'].to_list()
    docs = [doc.split(',') for doc in docs if isinstance(doc, str)]

    #词云图
    # wordfreq = word_freq(docs)
    # generate_wordcloud(wordfreq,'word_picture/words.png')

    docs=preprocess(docs)
    ldatrain(docs,20)
    # cut_word_to_file()






if __name__=='__main__':
    main()