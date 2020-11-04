import json
from spider2 import get_shop_info






def main():
    shop_list = [
        # 'http://www.dianping.com/shop/l4SIujY0y9HUjej0',
        # 'http://www.dianping.com/shop/k1Y0DDQaVEtGPUGh',
        # 'http://www.dianping.com/shop/G49js9Hi4R5oIjST',
        # 'http://www.dianping.com/shop/l2doop5fMN89xhKR',
        # 'http://www.dianping.com/shop/k5xgMkKhPhdbJUoL',
        # 'http://www.dianping.com/shop/k5N5QZiPLpMSsR53',
        # 'http://www.dianping.com/shop/k6he0Kgkx9JfqNk5',
        # 'http://www.dianping.com/shop/l561Ag24FZjPjgRk',
        # 'http://www.dianping.com/shop/EDOMV6jiQTQUgXad',
        # 'http://www.dianping.com/shop/H8cJl8laXpRUPbn1',
        # 'http://www.dianping.com/shop/irKop4LiLQFLFhUo',
        # 'http://www.dianping.com/shop/H3wrOjmFam09fg23',
        # 'http://www.dianping.com/shop/laBkairQFDHrgBIb',
        # 'http://www.dianping.com/shop/G95opQz2TULQoQu7',
        # 'http://www.dianping.com/shop/G66m005w8viJ1zPv',
        # 'http://www.dianping.com/shop/G6wvIBg2zdrjRBNa',
        # 'http://www.dianping.com/shop/FrfGYmwAz9SunhrF',
        # 'http://www.dianping.com/shop/GawglDpZU3xWLS5a',
        # 'http://www.dianping.com/shop/l7AhCvcHX5Nxvt0v',
        # 'http://www.dianping.com/shop/l4SIujY0y9HUjej0',
        # 'http://www.dianping.com/shop/G95opQz2TULQoQu7',
        # 'http://www.dianping.com/shop/G3IfObatB16oG3c5',
        # 'http://www.dianping.com/shop/G6wvIBg2zdrjRBNa',
        # 'http://www.dianping.com/shop/H2jGfGujB6IJpwEz',
        # 'http://www.dianping.com/shop/l24p2I7Rwa0RMviC',#JUST CHILL CAFE
        # 'http://www.dianping.com/shop/l4SIujY0y9HUjej0',#% Arabica
        # 'http://www.dianping.com/shop/G95opQz2TULQoQu7',#PLUS IN
        # 'http://www.dianping.com/shop/H7rksKEVyqyUeVqO',#挝咖 老挝咖啡
        # 'http://www.dianping.com/shop/G66m005w8viJ1zPv',#漫舞时光·猫咖·羊驼咖(IFS店)
        # 'http://www.dianping.com/shop/irKop4LiLQFLFhUo',#常识咖啡PY COMMONSS(春熙路店)
        # 'http://www.dianping.com/shop/l24p2I7Rwa0RMviC',#JUST CHILL CAFE(瓦当瓦舍春熙路店)
        'http://www.dianping.com/shop/l561Ag24FZjPjgRk',#Manner Coffee(IFS一楼店)
        'http://www.dianping.com/shop/H2jGfGujB6IJpwEz',#esp.1917
        'http://www.dianping.com/shop/jOdWJ2Idu41otSzo',#格度猫咪咖啡馆
        'http://www.dianping.com/shop/H8cJl8laXpRUPbn1',#Coffee Store咖啡便利屋

        
    ]

    with open('comment_821.json', 'r') as f:#评论
        dictionary1 = json.load(f)

    with open('dictionary4.json','r') as f:#fansNum
        dictionary2=json.load(f)
    # with  open('comment.json', 'r') as f:
    #     dictionary2 = json.load(f)

    get_shop_info(shop_list,dictionary1,dictionary2)



if __name__=='__main__':
    main()