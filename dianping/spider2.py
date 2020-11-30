import re

import requests
from pyquery import PyQuery as pq
import time
import random
import json



# url='http://www.dianping.com/shop/k3mz5QpZezLxDWIB/review_all'

def get_ua():#构建ua池
	user_agents = [
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
		'Opera/8.0 (Windows NT 5.1; U; en)',
		'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
		'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
		'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
		'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
	]
	user_agent = random.choice(user_agents) #random.choice(),从列表中随机抽取一个对象
	return user_agent

def get_ref():#构建referer池
	referers=['http://www.dianping.com/chengdu/ch10/r7949',
	'http://www.dianping.com/chengdu/ch10/r1577',
	'http://www.dianping.com/chengdu/ch10/r7767',
	'http://www.dianping.com/chengdu/ch10/r5894',
	'http://www.dianping.com/chengdu/ch10/r1592',
	'http://www.dianping.com/chengdu/ch10/r1601',
	'http://www.dianping.com/chengdu/ch10/r70146',
	'http://www.dianping.com/chengdu/ch10/r7764',
	'http://www.dianping.com/chengdu/ch10/r7771',
	'http://www.dianping.com/chengdu/ch10/r7769',
	'http://www.dianping.com/chengdu/ch10/r1597',
	'http://www.dianping.com/chengdu/ch10/r7768',
	'http://www.dianping.com/chengdu/ch10/r1974',
	'http://www.dianping.com/chengdu/ch10/r1578',
	'http://www.dianping.com/chengdu/ch10/r1604',
	'http://www.dianping.com/chengdu/ch10/r1579'
	]
	referer=random.choice(referers)
	return referer

# cookies=[
#         's_ViewType=10; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=52a56ecb-2c3f-a4e8-8139-231ba840b9c6.1597291385; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1597215322,1597291258; fspop=test; cy=8; cye=chengdu; lgtoken=0c7a4cf2e-ffbb-4594-abce-8b6170d2c1fe; dplet=fffe9aca5f375170bced5f59233f6648; dper=14665b781c236c2cb93f42796edbb9b32f36be195a4a732f0595430d54738d494801ef82860ab0e3f28faabd10a73dcd56004fdd1638c305dbd93cd53359261d82e33eb4ae309100754560c66c536ee432acbfa822bb0371d2b237c4d72dd1af; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%91%B5%E5%91%B5wn0626; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597588591; _lxsdk_s=173f79ff81e-e4e-dd9-815%7C%7C62',
#         's_ViewType=10; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=52a56ecb-2c3f-a4e8-8139-231ba840b9c6.1597291385; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1597215322,1597291258; fspop=test; cy=8; cye=chengdu; lgtoken=0e4660e27-c0f1-484a-add3-335d4a003a56; dplet=dde4f33b9daf35464f1dac4ce75a2167; dper=6219d5f81e51cedfb9e0e8f910cc18e9aaba34b27582f8ee19829487a1f02bf98e7aeba4a528e84e1d660d7c38101fd663d84d9c8941809cd7fa2ae93360e03cdefb0ba6dc2a2a6f1af2cbc656b9d1f3d7e8bcf0f1571e740263ea3b3dc832f9; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_6638015618; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597587717; _lxsdk_s=173f79ff81e-e4e-dd9-815%7C%7C18',
#         'cy=8; cye=chengdu; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=a5ed6f72-ef14-2a82-b9c2-12988d574794.1596348004; s_ViewType=10; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134e8e0be0cd4edee2eaba509213a972efb; ua=dpuser_1470708380; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1596545171,1596797154,1596895657,1596901097; fspop=test; dplet=852dcfcd88a09e22835bac5c8d74e1b6; dper=c7394aa46308e849eb11d671b574179af192439588bef68585f401117b921638761b43340be555d7dc4a6f4fa87065414be4038a1d52d8cbe9e61f82a50001bbfd867d6b48e1fd07db258c3fbc9549ddd9c9f0f53d2b736625764a3fc7b53891; ll=7fd06e815b796be3df069dec7836c3df; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597064576; _lxsdk_s=173d897befd-e45-1f4-027%7C%7C1',
#         's_ViewType=10; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=52a56ecb-2c3f-a4e8-8139-231ba840b9c6.1597291385; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1597215322,1597291258; fspop=test; cy=8; cye=chengdu; lgtoken=03a90a00b-ae55-4200-90f3-e137653fd682; dplet=8c77089412dc30f5beaba7c26f1b7da0; dper=a60473c03e7ffd4fbc4ccd1229e0d9a3b8793b04723dc43899fa786a52812043571154f8f2397eb184623713d811812beeff11ac98d4131c4be939e58e5694dd4d05c64bc5b0b209df2899d7008e746d6ceb06fef5e042f6a7e619e3095a9e94; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3239098757; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597484008; _lxsdk_s=173f15af765-eb1-3bb-5c2%7C1522617073%7C494'
#         'cy=8; cye=chengdu; _lxsdk_cuid=1736f1248570-0dbed264fe2f3d-5d37194f-e1000-1736f124858c8; _lxsdk=1736f1248570-0dbed264fe2f3d-5d37194f-e1000-1736f124858c8; _hc.v=e7edfde2-f58f-c5af-1dd7-2dbb599da937.1595296337; s_ViewType=10; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134c8ce59468d87e30b8799b555fff288e5; fspop=test; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1596794041,1596900252,1597460816,1597579791; _dp.ac.v=693e7e3e-8a83-4405-8096-c38017fd06ed; expand=yes; _lxsdk_s=173f72d0747-80b-9d9-fb5%7C%7C95; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597579937; lgtoken=0286f3ebf-1991-4345-81dd-4ac7ff11b604; dplet=0256ab43704452158456604ba334808f; dper=c7394aa46308e849eb11d671b574179a18a5c498caa46b408f133073dbededb9f26f49df51c8e5e0f1d8f906b2d669be108d516ea1de353d14febe3227dee8e70c8b2dd63dff3eb9dab50b89e2f3dd5d915a740ee949fad83258803120bc189e; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1470708380',
#     ]
def get_cookie():#两个cooki
    cookies=[
            '',
            'cy=8; cye=chengdu; _lxsdk_cuid=1756eefb923be-0e689a69d184e3-303464-125f51-1756eefb924c8; _lxsdk=1756eefb923be-0e689a69d184e3-303464-125f51-1756eefb924c8; _hc.v=a2a07d40-b72a-6d18-7911-c73ed5bf191d.1603884006; s_ViewType=10; cityid=8; switchcityflashtoast=1; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134550ec6133005ff12aef460bb54d45c28; aburl=1; fspop=test; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1605782711,1606528078; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; expand=yes; lgtoken=0866a71a6-a1b7-4007-94ab-15bfae2d6d48; dplet=1db66dce3d457ec9e659d1fb4c4c429b; dper=a1d8817d9634edec913de63afa89827cd81264868b82cbaed2637b7297960fb0b7713ef213651bb375fb0d889ff80067b8a41289fb73e8dc36c50769946fbe5ffb7d5766cc1714f49a92ab1e110d2c77170cb0d9f5542859440e86565f05820e; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3799410952; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606631683; _lxsdk_s=17612b549df-de2-394-6da%7C%7C80',
            'cy=8; cye=chengdu; _lxsdk_cuid=1756eefb923be-0e689a69d184e3-303464-125f51-1756eefb924c8; _lxsdk=1756eefb923be-0e689a69d184e3-303464-125f51-1756eefb924c8; _hc.v=a2a07d40-b72a-6d18-7911-c73ed5bf191d.1603884006; s_ViewType=10; cityid=8; switchcityflashtoast=1; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1470708380; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134550ec6133005ff12aef460bb54d45c28; aburl=1; fspop=test; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1605782711,1606528078; dplet=fe008c02d2a809323ec2498f889b9ef5; dper=d4c7d351fe957b83476443c8b3d009d925d0c86ae4da06c8ba6c735f4684d4ad111275741fbb308f9cf9c2c67fff341b324abcdd537ae6eba9b866ce65371d8bde68daa7b57ee1ebc7dc38c45f06d39b3bfb18e12fdad998fdaee116199c0209; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606551535; _lxsdk_s=1760deecf04-9c5-f10-c6%7C%7C6',
            # 's_ViewType=10; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=52a56ecb-2c3f-a4e8-8139-231ba840b9c6.1597291385; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1597215322,1597291258; fspop=test; cy=8; cye=chengdu; lgtoken=0c7a4cf2e-ffbb-4594-abce-8b6170d2c1fe; dplet=fffe9aca5f375170bced5f59233f6648; dper=14665b781c236c2cb93f42796edbb9b32f36be195a4a732f0595430d54738d494801ef82860ab0e3f28faabd10a73dcd56004fdd1638c305dbd93cd53359261d82e33eb4ae309100754560c66c536ee432acbfa822bb0371d2b237c4d72dd1af; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%91%B5%E5%91%B5wn0626; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597588591; _lxsdk_s=173f79ff81e-e4e-dd9-815%7C%7C62',
            # 's_ViewType=10; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=52a56ecb-2c3f-a4e8-8139-231ba840b9c6.1597291385; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1597215322,1597291258; fspop=test; cy=8; cye=chengdu; lgtoken=0e4660e27-c0f1-484a-add3-335d4a003a56; dplet=dde4f33b9daf35464f1dac4ce75a2167; dper=6219d5f81e51cedfb9e0e8f910cc18e9aaba34b27582f8ee19829487a1f02bf98e7aeba4a528e84e1d660d7c38101fd663d84d9c8941809cd7fa2ae93360e03cdefb0ba6dc2a2a6f1af2cbc656b9d1f3d7e8bcf0f1571e740263ea3b3dc832f9; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_6638015618; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597587717; _lxsdk_s=173f79ff81e-e4e-dd9-815%7C%7C18',
        #     'cy=8; cye=chengdu; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=a5ed6f72-ef14-2a82-b9c2-12988d574794.1596348004; s_ViewType=10; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134e8e0be0cd4edee2eaba509213a972efb; ua=dpuser_1470708380; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1596545171,1596797154,1596895657,1596901097; fspop=test; dplet=852dcfcd88a09e22835bac5c8d74e1b6; dper=c7394aa46308e849eb11d671b574179af192439588bef68585f401117b921638761b43340be555d7dc4a6f4fa87065414be4038a1d52d8cbe9e61f82a50001bbfd867d6b48e1fd07db258c3fbc9549ddd9c9f0f53d2b736625764a3fc7b53891; ll=7fd06e815b796be3df069dec7836c3df; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597064576; _lxsdk_s=173d897befd-e45-1f4-027%7C%7C1',
        #     's_ViewType=10; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=52a56ecb-2c3f-a4e8-8139-231ba840b9c6.1597291385; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1597215322,1597291258; fspop=test; cy=8; cye=chengdu; lgtoken=03a90a00b-ae55-4200-90f3-e137653fd682; dplet=8c77089412dc30f5beaba7c26f1b7da0; dper=a60473c03e7ffd4fbc4ccd1229e0d9a3b8793b04723dc43899fa786a52812043571154f8f2397eb184623713d811812beeff11ac98d4131c4be939e58e5694dd4d05c64bc5b0b209df2899d7008e746d6ceb06fef5e042f6a7e619e3095a9e94; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3239098757; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597484008; _lxsdk_s=173f15af765-eb1-3bb-5c2%7C1522617073%7C494',
        #     'cy=8; cye=chengdu; _lxsdk_cuid=1736f1248570-0dbed264fe2f3d-5d37194f-e1000-1736f124858c8; _lxsdk=1736f1248570-0dbed264fe2f3d-5d37194f-e1000-1736f124858c8; _hc.v=e7edfde2-f58f-c5af-1dd7-2dbb599da937.1595296337; s_ViewType=10; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134c8ce59468d87e30b8799b555fff288e5; fspop=test; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1596794041,1596900252,1597460816,1597579791; _dp.ac.v=693e7e3e-8a83-4405-8096-c38017fd06ed; expand=yes; _lxsdk_s=173f72d0747-80b-9d9-fb5%7C%7C95; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597579937; lgtoken=0286f3ebf-1991-4345-81dd-4ac7ff11b604; dplet=0256ab43704452158456604ba334808f; dper=c7394aa46308e849eb11d671b574179a18a5c498caa46b408f133073dbededb9f26f49df51c8e5e0f1d8f906b2d669be108d516ea1de353d14febe3227dee8e70c8b2dd63dff3eb9dab50b89e2f3dd5d915a740ee949fad83258803120bc189e; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1470708380',
         ]
    cookie=random.choice(cookies)
    return cookie


def get_header():
    header = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'User-Agent': get_ua(),
        'Reference':get_ref(),
        'Cookie':get_cookie()
    }
    return header

def get_html(url):
    time.sleep(random.randint(0,3))
    header=get_header()
    response=requests.get(url,headers=header,allow_redirects=False)

    #找不到页面
    if response.status_code==403:
        print('请求失败')
        return get_html(url)

    #验证中心
    if response.status_code==302:
        print('验证中心')
        return get_html(url)

    html=response.text
    return response.text,response.status_code
    # if response.status_code==403:
    #     header=get_header()
    #     return get_html(url,header)
def parse(string,dictionary):
    chars=string.split('\n')
    return get_words(chars,dictionary)


def char_decode(code,dictionary):
    chars = code.split('\n')
    result = []
    for char in chars:
        if '\\u' in repr(char):
            s = 'uni' + repr(char)[3:7]
            if s in dictionary.keys():
                string = dictionary.get(s)
                result.append(dictionary.get(s))
        else:
            result.append(char)
    return ''.join(result)

def get_words(words,dictionary):
    result=[]
    for word in words:
        if word in dictionary.keys():
            string=dictionary.get(word)
            result.append(string)
        else:
            result.append(word)

    return ''.join(result)


def get_address(element,dictionary):
    element=str(element)
    element=element.replace('\n','')
    elements = re.findall('<div\sclass=\"address-info\">(.*)</div>', element)
    element = elements[0]
    start_word = element[:element.find('<bb')]

    chars = element.split('<bb')
    chars = chars[1:]
    words = []
    words.append(start_word)
    for char in chars:
        start = char.find(('"'))

        words.append(char[start + 1: start + 7])
        if not char.endswith('>'):
            words.append(char[char.find('>') + 1:])

    return get_words(words,dictionary)


def get_content(element,dictionary):
    element=str(element).replace('\n','')
    element=re.findall('<div class=\"review-words.{0,5}\">(.*?)</div>',element)[0]
    # end = element.find('<div class="less-words">')
    # element = element[:end - 1]

    element = re.sub('<img\sclass=.*?/>', '', element)
    element=re.sub('<div class=\"less-words\">.*</a>','',element)

    chars = element.split('<svgmtsi')
    # chars = chars[1:]
    words = []
    words.append(chars[0])
    chars=chars[1:]
    for char in chars:
        start = char.find(('"'))

        words.append(char[start + 1: start + 7])
        if not char.endswith('</svgmtsi>'):
            words.append(char[char.find('>') + 1:])

    return get_words(words, dictionary)


# def char_decode_svg(children,dictionary):
#     chars = []
#     for item in children:
#         item = str(item).strip()
#         chars.append(item[11:16])
#         if len(item) > 19:
#             chars.append(item[19:])
#
#     words = []
#     for char in chars:
#         if char.isalnum():
#             if char in dictionary.keys():
#                 words.append(dictionary[char])
#             else:
#                 words.append(char)
#         else:
#             words.append(char)
#
#     return words


def shop_list_url(url):
    html,status=get_html(url)
    doc=pq(html)
    items=doc('#shop-all-list li').items()
    shop_url=[]
    for item in items:
        shop_url.append(item.find('.tit a').attr('href'))
    return shop_url

def get_comments(html,comments,dictionary1,dictionary2):#得到评论，列表形式，每一条评论，包含用户，vip，时间等信息，有些需要解密处理
    doc=pq(html)
    items = doc('.reviews-items .main-review').items()
    for item in items:
        user_url=item.find('.dper-info .name').attr('href')
        comment = {

            # 'vip_or_not': item.find('.dper-info').children().hasClass('vip'),
            'review_after_spend': item.children().hasClass('richtitle'),
            'review_rank': item.find('.score').text(),
            'recommends': item.find('.review-recommend').text(),
            'time': item.find('.misc-info .time').text(),
            'content': get_content(item.find('.review-words'),dictionary1),
            'reply_or_not':item.children().hasClass('shop-reply'),
            'like':item.find('.actions > em:nth-child(2)').text(),
            'reply':item.find('.actions > em:nth-child(4)').text()
            # 'user': get_user('http://www.dianping.com' + user_url, dictionary2),

        }
        comment['user']=get_user(user_url,dictionary2),
        comments.append(comment)
        print(comment)

def get_level(element):
    element=str(element)
    elements=re.findall('<span title=\"\" class=\"user-rank-rst urr-rank([0-9]+)\"/>',element)
    level=elements[0]
    return int(level)

def get_vip(element):
    element=str(element)
    if 'icon-vip' in element:
        return True
    else:
        return False


def get_user(url,dictionary):
    if url is None:
        return '匿名用户'
    html,status=get_html('http://www.dianping.com'+url)
    while status==404:
        html,status=get_html(url)
    doc=pq(html)
    user = {
        'user_name': doc('.header-nav .txt .tit .name').text(),
        'vip_or_not': get_vip(doc('.header-nav .txt .tit .vip')),
        'level': get_level(doc('.header-nav .user-info.col-exp')),
        'follows':char_decode(doc('.user_atten > ul > li:nth-child(1) > a > strong').text(),dictionary),
        'fans':char_decode(doc('.user_atten > ul > li:nth-child(2) > a > strong').text(),dictionary),
        'likes':char_decode(doc('.user_atten > ul > li:nth-child(3) strong').text(),dictionary)

    }
    return user


def get_shop_info(url_list,dictionary1,dictionary2):#写入商店信息，包括地址，电话，人均消费，和评论对象
    for url in url_list:
        # print(url)
        html,status=get_html(url+'/review_all')
        doc=pq(html)
        title=doc.find('head title').text()
        if title=='美食, 餐厅餐饮, 团购,生活,优惠券-大众点评网':
            continue
        basic_info=doc('.review-shop-wrap')
        shop_info={
            'shop_name':basic_info.find('.shop-name').text(),
            'ave_cost ':basic_info.find('.rank-info .price').text(),
            'score ':basic_info.find('.rank-info .score').text(),
            # 'address':get_address(basic_info.find('.address-info'),dictionary1),
            # 'phone':get_phone(basic_info.find('.phone-info')),
            'comment_count':basic_info('.reviews').text(),
            'review_labels':doc('.reviews-tags .content a').text(),
        }
        comments = []
        get_comments(html, comments,dictionary1,dictionary2)#第一页评论

        #评论翻页
        reviews_pages=doc('.reviews-pages')
        flag=reviews_pages.children().hasClass('NextPage')
        while flag:
            next_page=reviews_pages.find('.NextPage').attr('href')#下一页url
            html,status=get_html('http://www.dianping.com'+next_page)#下一页网页源代码
            doc=pq(html)
            reviews_pages = doc('.reviews-pages')
            flag=doc('.reviews-pages').children().hasClass('NextPage')
            get_comments(html, comments,dictionary1,dictionary2)



        # reviews_pages = doc('.reviews-pages a').items()
        # reviews_pages = ['http://www.dianping.com/'+page.attr('href') for page in reviews_pages]
        # for url in reviews_pages:
        #     html=get_html(url)
        #     get_comments(html,comments)
        shop_info['comments']=comments
        json_str=json.dumps(shop_info)
        with open(shop_info['shop_name']+'.json','w',encoding='utf-8') as f:
            f.write(json_str)





def get_shop_pages(url):
    html,status=get_html(url)
    doc=pq(html)
    itmes=doc('.content-wrap .shop-wrap .page a').items()
    shop_pages=[page.attr('href') for page in itmes]
    return shop_pages[1:]




def main():
    with open('address.json','r') as f:
        dictionary1 = json.load(f)

    with  open('comment.json','r') as f:
        dictionary2=json.load(f)

    url='http://www.dianping.com/chengdu/ch10/g132r1577'
    # url='https://httpbin.org/get'
    shop_list=shop_list_url(url)#第一页商店url列表
    get_shop_info(shop_list,dictionary1,dictionary2)#将首页商店的信息写入列表
    shop_pages = get_shop_pages(url)  # 商店翻页url
    for page in shop_pages:
        shop_list=shop_list_url(page)
        get_shop_info(shop_list,dictionary1,dictionary2)

    # with open('shops_info.json','w') as f:
    #     json.dumps(shops_info)


    # with open('shops_info.json','w') as f:#保存商店信息为json
    #     json.dump(f)


if __name__=='__main__':
    main()