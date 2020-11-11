import re

element1="""
<div class="review-words">
<svgmtsi class="slbeo"></svgmtsi><svgmtsi class="sln8m"></svgmtsi><svgmtsi class="sla96"></svgmtsi><svgmtsi class="slfnw"></svgmtsi>餐。<svgmtsi class="slh5n"></svgmtsi><svgmtsi class="slzad"></svgmtsi><svgmtsi class="slipd"></svgmtsi><svgmtsi class="slh5n"></svgmtsi><svgmtsi class="slzad"></svgmtsi>很<svgmtsi class="slhsn"></svgmtsi>吃，<svgmtsi class="slipd"></svgmtsi>有<svgmtsi class="slbeo"></svgmtsi>儿咸。玫瑰盐咖啡<svgmtsi class="sl2fj"></svgmtsi>可以。红丝<svgmtsi class="slqq6"></svgmtsi>整体特别一般。<svgmtsi class="sla6r"></svgmtsi><svgmtsi class="slxj8"></svgmtsi>挺<svgmtsi class="slhsn"></svgmtsi>，门<svgmtsi class="slyzf"></svgmtsi>有太多<svgmtsi class="sl66r"></svgmtsi>着用力<svgmtsi class="sl3qq"></svgmtsi>猛的妹妹<svgmtsi class="sl3qq"></svgmtsi>来<svgmtsi class="sl1v9"></svgmtsi><svgmtsi class="sltfq"></svgmtsi>，<svgmtsi class="slj6c"></svgmtsi>仁<svgmtsi class="sl2iy"></svgmtsi>，<svgmtsi class="sluku"></svgmtsi><svgmtsi class="sl6d3"></svgmtsi>是进<svgmtsi class="sl9v1"></svgmtsi>吃<svgmtsi class="slipd"></svgmtsi>啊，别<svgmtsi class="slao6"></svgmtsi>在门<svgmtsi class="slyzf"></svgmtsi><svgmtsi class="sl1v9"></svgmtsi><svgmtsi class="sl1v9"></svgmtsi><svgmtsi class="sl1v9"></svgmtsi>啊！	                        </div>
"""
element2="""
    <div class="review-words Hide">
                            <svgmtsi class="sla9g"></svgmtsi>众<svgmtsi class="slbeo"></svgmtsi>评找到<svgmtsi class="sllv6"></svgmtsi>网红咖啡<svgmtsi class="sltng"></svgmtsi>，和酒<svgmtsi class="sltng"></svgmtsi><svgmtsi class="slxqf"></svgmtsi>一<svgmtsi class="slqz6"></svgmtsi>，<svgmtsi class="sloq5"></svgmtsi><svgmtsi class="sl30a"></svgmtsi>下雨没<svgmtsi class="slxqf"></svgmtsi>外面拍照。现场很<svgmtsi class="sloub"></svgmtsi><svgmtsi class="slmdv"></svgmtsi>生群体，<svgmtsi class="slbeo"></svgmtsi><svgmtsi class="sln8m"></svgmtsi><svgmtsi class="sltng"></svgmtsi>内<svgmtsi class="sltln"></svgmtsi><svgmtsi class="sle3n"></svgmtsi>，很<svgmtsi class="sltna"></svgmtsi>算，99有2个主<svgmtsi class="sly22"></svgmtsi>和2<svgmtsi class="slfzy"></svgmtsi><svgmtsi class="sltvq"></svgmtsi>品，我<svgmtsi class="slxte"></svgmtsi><svgmtsi class="sln8m"></svgmtsi>dirty，比<svgmtsi class="sl96g"></svgmtsi>一<svgmtsi class="slg1i"></svgmtsi>。但整体消<svgmtsi class="sli6r"></svgmtsi>环境还<svgmtsi class="sli7s"></svgmtsi>错，<svgmtsi class="slyzw"></svgmtsi>得一去。离<svgmtsi class="sleer"></svgmtsi><svgmtsi class="slurl"></svgmtsi>里<svgmtsi class="sldsw"></svgmtsi><svgmtsi class="sli7s"></svgmtsi><svgmtsi class="sl5sq"></svgmtsi>
                            <div class="less-words">
	                            <a href="javascript:;"
	                               class="unfold"
                                   data-click-name="收起评论12"
                                   data-click-title="文字"
	                            >
		                            收起评论<i class="icon"></i>
	                            </a>
                            </div>
"""
def get_content(element):
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

        words.append(char[start + 1: start + 6])
        if not char.endswith('</svgmtsi>'):
            words.append(char[char.find('>') + 1:])

    print(words)

get_content(element1)
get_content(element2)