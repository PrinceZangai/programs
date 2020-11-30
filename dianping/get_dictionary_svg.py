import json
import requests
import re
from pyquery import  PyQuery as pq


urls={}


contain_id=[
    'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/a33336b2ca2677129e7faef6d03a330b.css',
    'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/b520e612ddff11faad62f4af7e97ae7d.svg'
]

comment4=[
    'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/a2822bc00c3ede8c8e8af05c391b71a1.css',
    'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/1370c302577298e22e0643fb49319f2a.svg'
]
header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }

url=[
    'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/7a98327646746b5e3b0d0062069b3c8e.css',
    'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/1c68618b38bd36fd77f70b163ac7cdbb.svg'
]


def decode(urls):
    for url in urls.keys():
        css=urls[url][0]
        svg=urls[url][1]
        css_html=requests.get(css,headers=header).text
        svg_html=requests.get(svg,headers=header).text
        keys_list=re.findall('\.([0-9a-zA-Z]{6}?)\{background:-([0-9]+)\.0px\s-([0-9]+)\.0px;\}',css_html)
        # doc=pq(svg_html.encode('utf-8'))
        # values_list=doc.find('text').items()
        # values_list={(item.attr('y'),item.text()) for item in values_list}

        values_list=re.findall('<text\sx=\"0\"\sy=\"([0-9]+)\">(.*?)</text>',svg_html)

        dic={}
        for key in keys_list:
            for value in values_list:
                if int(key[2])<=int(value[0]):
                    dic[key[0]]=value[1][int(int(key[1])/14)]
                    break
            continue
        with open('dict_comment.json','w') as f:
            json.dump(dic,f)

def decode_id(url):
    css=url[0]
    svg=url[1]
    css_html=requests.get(css,headers=header).text
    svg_html=requests.get(svg,headers=header).text
    keys_list=re.findall('\.([0-9a-zA-Z]{6}?)\{background:-([0-9]+)\.0px\s-([0-9]+)\.0px;\}',css_html)
    id_to_y=re.findall('<path id=\"[0-9]+\" d=\"M0 ([0-9]+) H600\"/>',svg_html)
    values=re.findall('<textPath xlink:href=\"#([0-9]+)\" textLength=\"([0-9]+)\">(.*)</textPath>',svg_html)
    values_list=list(map(lambda x,y:(x,y[2],y[1]),id_to_y,values))

    dic={}
    for key in keys_list:
        for value in values_list:
            if int(key[2]) <= int(value[0]):
                if int(key[1])+14>int(value[2]):
                    break
                else:
                    dic[key[0]] = value[1][int(int(key[1]) / 14)]
                    break
        continue

    print(dic)
    with open('dict_comment.json', 'w') as f:
        json.dump(dic, f)




decode_id(url)





