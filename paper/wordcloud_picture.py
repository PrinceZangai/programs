import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import pandas as pd
import matplotlib.font_manager as fm


#计算词频
def word_freq(text):
    freq_dic={}
    for sentence in text:
        sentence=sentence[1:-1]
        sentence=sentence.replace('\'','')
        for word in sentence.split(','):
            word=word.strip()
            if word in freq_dic.keys():
                freq_dic[word]+=1
            else:
                freq_dic[word]=1
    return freq_dic

text_df=pd.read_excel('word_cut_jieba.xlsx')
all_review_frequencies=word_freq(text_df['clear_single'])
all_review_frequencies=sorted(all_review_frequencies.items(),reverse=True,key=lambda x:x[1])


wc=WordCloud(background_color='white',
             max_words=200,
             # mask=bg, #Set the background of the picture
             max_font_size=200,
             width=1000,
             height=1000,
             random_state=60,
             font_path='C:/Windows/Fonts/simkai.ttf'
             )

wc.generate_from_frequencies(dict(all_review_frequencies))
plt.imshow(wc)
plt.imshow(wc,interpolation="bilinear")
#去掉云图坐标
plt.axis("off")
plt.show()
print()