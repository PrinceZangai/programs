import json
import pandas as pd
#将店铺评论输出为excel表

import os

shop_list=os.listdir('data2')

shop_review=pd.DataFrame(columns=['review','shop_name'])
for shop in shop_list:
    with open('data2/'+shop) as f:
        shopinfo=json.load(f)
        reviewitem=pd.DataFrame(shopinfo['comments'])
        reviewitem=reviewitem['content'].str.strip().to_frame(name='review')
        reviewitem['shop_name']=shop[:-5]
        shop_review=shop_review.append(reviewitem)

shop_review.to_csv('shop_review.csv')
# shop_review.to_excel('shop_review.xlsx')

