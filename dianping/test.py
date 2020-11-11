
from selenium import webdriver
import time
import random
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

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

# def parser(chars,dictionary):
#     chars=chars.split('\n')
#     result=[]
#     with open(dictionary,'r') as f:
#         dictionary=json.load(f)
#     for char in chars:
#         if '\\u' in repr(char):
#             s='uni'+repr(char)[3:7]
#             if s in dictionary.keys():
#                 string=dictionary.get(s)
#                 result.append(dictionary.get(s))
#         else:
#             result.append(char)
#     return ''.join(result)


def main():
    chromeOptions = webdriver.ChromeOptions()
    useragent=get_ua()
    chromeOptions.add_argument('--useragent=%s' % useragent)
    chromeOptions.add_experimental_option('excludeSwitches',
                                          ['enable-automation'])  # 设置webdriver为undefind， 因为自动驱动时该值为true
    browser=webdriver.Chrome(options=chromeOptions)
    headers={
        'Cookie': 'fspop=test; cy=8; cye=chengdu; _lxsdk_cuid=173d653d1f1c8-0d828cc1d1dcb3-3323765-e1000-173d653d1f1c8; _lxsdk=173d653d1f1c8-0d828cc1d1dcb3-3323765-e1000-173d653d1f1c8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1597028685; _hc.v=8e69b6be-a040-b252-9883-68c6185673c7.1597028685; dplet=94452d407460354008b9f408031b34e2; dper=c7394aa46308e849eb11d671b574179ae9ff6ddea94cc1e891149e7258506168f238e8b5278fe10cbbf5a1a36071fae63816a58d49a7ab713d64e0967c3e2b824ff16729d813d67e80ea5113a2be2d76ceb31b6c891b569a4a923bf9aef8837c; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1470708380; ctu=e48c5ff2ea40c54cf1a6b6defe4c1134fedb4927685ca28a3f748a0a3ed0a5d5; s_ViewType=10; _lxsdk_s=173d6706e1a-853-8ca-613%7C%7C89; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1597031395',
        'Host': 'hls.dianping.com',
        'Referer': 'http://www.dianping.com/chengdu/ch10/g132r1577',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    browser.get('http://www.dianping.com/')



    # iframe =browser.find_element_by_xpath('//*[@id="J_login_container"]/div/iframe')  # 切换到登陆模块
    # browser.switch_to.frame(iframe)
    # icon_pc = browser.find_element_by_xpath('/html/body/div/div[2]/div[5]/span')  # 选择账户登录
    # icon_pc.click()
    # time.sleep(2)
    # name_login = browser.find_element_by_xpath('//*[@id="tab-account"]')  # 选择手机密码登录登录
    # name_login.click()
    # time.sleep(2)
    #
    # browser.find_element_by_xpath('//*[@id="account-textbox"]').send_keys('15272570669')  # 输入手机号
    # browser.find_element_by_xpath('//*[@id="password-textbox"]').send_keys('ljd232425')  # 输入密码
    # browser.find_element_by_xpath('//*[@id="login-button-account"]').click()  # 点击登录
    wait=WebDriverWait(browser,10)
    time.sleep(5)
    closebutton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.fullScreenFlash > div.countDown')))
    closebutton.click()


    browser.get('http://www.dianping.com/chengdu/ch10/g132r1577')

    wait.until(10)

if __name__=='__main__':
    main()
    # get_dictionary()