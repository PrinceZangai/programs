
#coding=utf-8
import requests
import json


response=requests.get('http://tiqu.linksocket.com:81/abroad?num=1&type=1&lb=1&sb=0&flow=1&regions=china&n=1')
print(response.text)
#请求地址
targetUrl = 'http://www.dianping.com/chengdu/ch10/g132r1577'
response=response.text.split(':')
ip=response[0]
port=response[1]
#代理服务器
proxyHost =ip
proxyPort = port

proxyMeta = "http://%(host)s:%(port)s" % {
    'host':proxyHost,
    'port':proxyPort
}

#pip install -U requests[socks]  socks5代理
# proxyMeta = "socks5://%(host)s:%(port)s" % {

#     "host" : proxyHost,

#     "port" : proxyPort,

# }

proxies = {
    "http" : proxyMeta
}
header={
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Cookie':'cy=8; cye=chengdu; _lxsdk_cuid=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _lxsdk=173adc173e1c8-010ef609693dea-3323765-e1000-173adc173e1c8; _hc.v=a5ed6f72-ef14-2a82-b9c2-12988d574794.1596348004; s_ViewType=10; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134e8e0be0cd4edee2eaba509213a972efb; ua=dpuser_1470708380; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1596545171,1596797154,1596895657,1596901097; fspop=test; dplet=852dcfcd88a09e22835bac5c8d74e1b6; dper=c7394aa46308e849eb11d671b574179af192439588bef68585f401117b921638761b43340be555d7dc4a6f4fa87065414be4038a1d52d8cbe9e61f82a50001bbfd867d6b48e1fd07db258c3fbc9549ddd9c9f0f53d2b736625764a3fc7b53891; ll=7fd06e815b796be3df069dec7836c3df; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597064576; _lxsdk_s=173d897befd-e45-1f4-027%7C%7C1'
    }
resp = requests.get(targetUrl,headers=header)
print(resp.status_code)
print(resp.text)

