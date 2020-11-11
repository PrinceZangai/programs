from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyquery import PyQuery as pq

import json

browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
browser.get('http://www.dianping.com/chengdu/ch10/g132r1577')

def close():
    closebutton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J-img-pop > span')))
    closebutton.click()

def char_decode(code,dictionary):
    chars = code.split('\n')
    result = []
    with open(dictionary, 'r') as f:
        dictionary = json.load(f)
    for char in chars:
        if '\\u' in repr(char):
            s = 'uni' + repr(char)[3:7]
            if s in dictionary.keys():
                string = dictionary.get(s)
                result.append(dictionary.get(s))
        else:
            result.append(char)
    return ''.join(result)

def getaddress(chars,dictionary):
    return char_decode(chars,dictionary)

def getscore(chars):
    if '.' in chars:
        return float(chars)
    else:
        return '无'

def comment_count(chars,dictionary):
    result=char_decode(chars,dictionary)
    if result.isdigit():
        return int(result)
    else:
        return result


def next_page():
    try:
        nextpage=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.section.Fix.J-shop-search > div.content-wrap > div.shop-wrap > div.page > a.next')))
        nextpage.click()
        getcoffeelist()
    except TimeoutException:
        return None
    except ElementClickInterceptedException:
        close()
        next_page()

def get_cost(chars,dictionary):
    return char_decode(chars,dictionary)


def getcoffeelist():
    try:
        html=browser.page_source
        doc=pq(html)
        items=doc('#shop-all-list li').items()
        shop_list=[]
        for item in items:
            shop={
                'url':item.find('.pic a').attr('href'),
                'shop_name':item.find('.tit h4').text(),
                'score':getscore(item.find('.txt .star_score').text()),
                'address':getaddress(item.find('.addr').text(),'dictionary.json'),
                'comment_count':comment_count(item.find('.comment .review-num b').text(),'dictionary3.json'),
                'average_cost':get_cost(item.find('.comment .mean-price b').text(),'dictionary3.json'),
                'recommend':item.find('.recommend a').text(),
                }
            shop_list.append(shop)
            print(shop)
        return shop_list
        # print(0)
        # textinput=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J-search-input')))
        # submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J-channel-bnt')))
        # closebutton=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J-img-pop > span')))
        # closebutton.click()
        # textinput.send_keys(keyword)
        # submit.click()
        # filterbutton=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.section.Fix.J-shop-search > div.navigation > div.nav-category.J_filter_channel > div > div > div > a.cur > span')))
        # filterbutton.click()
    except TimeoutException:
        getcoffeelist()




def main():
    shop_list=getcoffeelist()
    shop_urls={item['shop_name']:item['url'] for item in shop_list}
    print(shop_urls)
    browser.get('https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2F')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#logo-input > div > div.search-box > div')))
    for url in shop_urls.values():
        browser.get(url)
        wait.until()

    while True:
        try:
            next_page()
        except NoSuchElementException:
            break

if __name__=='__main__':
    main()