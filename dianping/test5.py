import json
from  pyquery import PyQuery as pq


def get_comments(html,comments):
    doc=pq(html)
    items = doc('.reviews-items .main-review').items()
    print(items)
    for item in items:
        print(item)
        comment = {
            'user': item.find('.dper-info a').text(),
            'vip_or_not': item.find('.dper-info').children().hasClass('vip'),
            'review_after_spend': item.children().hasClass('richtitle'),
            'review_rank': item.find('.score').text(),
            'content': item.find('.review-words').text(),
            'recommends': item.find('.review-recommend').text(),
            'time': item.find('.misc-info .time').text()
        }
        comments.append(comment)
        print(comment)


with open('shop_detail_review.html','r',encoding='utf-8') as f:
    f=f.read()

doc=pq(f)
shop_wrap=doc('.review-shop-wrap')
shop_name=shop_wrap.find('.shop-name').text()
ave_cost=shop_wrap.find('.rank-info .price').text()
score=shop_wrap.find('.rank-info .score').text()
address=shop_wrap.find('.address-info').text()
phone=shop_wrap.find('.phone-info').text()


comments=[]
get_comments(f,comments)
reviews_pages=doc('.reviews-pages a').items()
reviews_pages=[page.attr('href') for page in reviews_pages]
for url in reviews_pages:
    get_comments(comments)