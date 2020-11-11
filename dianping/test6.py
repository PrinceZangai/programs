import json
import re

from pyquery import PyQuery as pq
from spider2 import get_html
from spider2 import char_decode

import requests
url1='http://www.dianping.com/shop/l24p2I7Rwa0RMviC/review_all'
url='http://www.dianping.com/member/67588168'
html,status=get_html(url1)
html,status=get_html(url)
print(html)
doc = pq(html)

def get_level(element):
    element=str(element)
    elements=re.findall('<span title=\"\" class=\"user-rank-rst urr-rank([0-9]+)0\"/>',element)
    level=elements[0]
    return int(level)

def get_vip(element):
    element=str(element)
    if 'icon-vip' in element:
        return True
    else:
        return False

with open('dictionary4.json','r') as f:
    dictionary=json.load(f)



user = {
    'user_name': doc('.header-nav .txt .tit .name').text(),
    'vip_or_not': get_vip(doc('.header-nav .txt .tit .vip')),
    'level': get_level(doc('.header-nav .user-info.col-exp')),
    'follows':char_decode(doc('.user_atten > ul > li:nth-child(1) > a > strong').text(),dictionary),
    'fans':char_decode(doc('.user_atten > ul > li:nth-child(2) > a > strong').text(),dictionary),
    'likes':char_decode(doc('.user_atten > ul > li:nth-child(3) strong').text(),dictionary)

}

print(user)
