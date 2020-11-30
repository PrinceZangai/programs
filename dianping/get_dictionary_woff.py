import json
from fontTools.ttLib import TTFont

a='./font/be9febf2.woff'
b='./font/2ed8f6f4.woff'
c='./font/6e3abc4e.woff'
d='./font/78b94d73.woff'
e='./font/732b648f.woff'
font = TTFont(e)
font.saveXML('test.xml')

        #该步骤为得到字体的按照顺序排列的结果，前两个是没用的，最后的结果和上面的字的列表相对应
names=font.getGlyphNames()[1:]


# print(result)
chars=[]
with open('fontchar/732b648f.txt',encoding='utf-8') as f:
    while True:
            char=f.read(1)
            if char!='\n':
                chars.append(char)
            if not char:
                break
        # char=f.read(1)
    # if char!='\n':
    #     chars.append(char)


print(len(names))
print(len(chars))
dictionary=dict(zip(names,chars))
print(dictionary)
with open('dic_number.json','w',encoding='utf-8') as f:
    json.dump(dictionary,f)
