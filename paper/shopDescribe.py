import re

import pandas  as pd
import numpy as np
import os
import json
import plotly.graph_objects as go

def prepocess_data():
    shop_list=os.listdir('data2')
    shopinfos=pd.DataFrame(columns=['shop_name','ave_cost','score','comment_num','review_labels'])
    shop_review_info=pd.DataFrame(columns=['shop_name','review_after_spend','review_rank','recommends','time','content'])
    for theshop in shop_list:
        with open('data2/'+theshop) as f:
            shop=json.load(f)
            shopinfo=pd.Series([shop['shop_name'],shop['ave_cost '],shop['score '],shop['comment_count'],shop['review_labels']],
                               index=['shop_name','ave_cost','score','comment_num','review_labels'])
            shop_reviews=pd.DataFrame(shop['comments'])
            shop_reviews['shop_name']=theshop[:-5]
            shopinfos=shopinfos.append(shopinfo,ignore_index=True)
            shop_review_info=shop_review_info.append(shop_reviews)
        print()
    shop_review_info.to_excel('source_data/shop_reviews.xlsx')
    shopinfos.to_excel('source_data/shopinfos.xlsx')


def apply_score(score):
    scores=re.findall('\d+.\d+',score)
    return sum([float(s) for s in scores])/3

def apply_user(user):
    if 'True' in user:
        return True
    else:
        return False

def main():
    # prepocess_data()
    shops=pd.read_excel('source_data/shopinfos.xlsx')
    shops = shops.iloc[:, 1:]
    shops = shops.set_index('shop_name')
    shops['ave_cost'] = shops['ave_cost'].apply(lambda x: int(re.findall('\d+', x)[0]))
    shops['score'] = shops['score'].apply(lambda x: re.findall('\d+.\d+', x))
    shops['taste_score'] = shops['score'].apply(lambda x: float(x[0]))
    shops['env_score'] = shops['score'].apply(lambda x: float(x[1]))
    shops['service_score'] = shops['score'].apply(lambda x: float(x[2]))
    shops['comment_num'] = shops['comment_num'].apply(lambda x: int(x[:-3]))
    shops['review_labels'] = shops['review_labels'].apply(lambda x: ' '.join(re.findall(r'[\u4e00-\u9fa5]+', x)))
    shops = shops.drop(columns=['score'])


    reviews_all=pd.read_excel('source_data/shop_reviews.xlsx')
    print(reviews_all.info())
    reviews_all=reviews_all.iloc[:,1:]
    reviews_all['user_name']=reviews_all['user'].apply(lambda x:x.split(',')[0][16:-1])
    reviews_all['vip'] = reviews_all['user'].apply(apply_user)
    reviews_all['level']=reviews_all['user'].apply()


    print()


if __name__=='__main__':
    main()



