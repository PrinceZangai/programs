import json
from selenium import webdriver

dirver = webdriver.Chrome()
dirver.delete_all_cookies()
dirver.get('https://account.dianping.com/login?redir=http://www.dianping.com')
dictCookies = dirver.get_cookies()
print(dictCookies)
jsonCookies = json.dumps(dictCookies)
# 登录完成后,将cookies保存到本地文件
with open("cookies_dianping.json", "w") as fp:
    fp.write(jsonCookies)