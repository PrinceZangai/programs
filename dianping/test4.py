import requests
import json
from  pyquery import PyQuery as pq

url='http://www.dianping.com/shop/G1UUylDZj7pSOtJx'
url2='http://www.dianping.com/shop/l3ungd7Yl2GBz1Qo/review_all'
headers={
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Cookie': 'cy=8; cye=chengdu; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=a5ed6f72-ef14-2a82-b9c2-12988d574794.1596348004; s_ViewType=10; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134e8e0be0cd4edee2eaba509213a972efb; fspop=test; dplet=1c7b09e1c8b74f5b99179fb182c15125; ua=dpuser_1470708380; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1597215322,1597291258; _lxsdk_s=173e5f74633-5ce-5a0-bc5%7C%7C152; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597291369'
}
response=requests.get(url2,headers=headers)
html=response.text
print(response.text)
with open('shop_detail_review.html','w',encoding='utf-8') as f:
    f.write(html)