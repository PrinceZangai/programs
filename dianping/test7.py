from pyquery import PyQuery as pq
html="""
<div class="reviews-pages">


						<span class="PageSel">1</span>
                                <a href="/shop/laBkairQFDHrgBIb/review_all/p2" data-pg="2" class="PageLink" title="2" data-click-name="页码2" data-click-title="文字" data-click-shopuuid="laBkairQFDHrgBIb" data-click-pagetailurl="" data-click-curpage="1">2</a>
                                <a href="/shop/laBkairQFDHrgBIb/review_all/p3" data-pg="3" class="PageLink" title="3" data-click-name="页码3" data-click-title="文字" data-click-shopuuid="laBkairQFDHrgBIb" data-click-pagetailurl="" data-click-curpage="1">3</a>


					<a href="/shop/laBkairQFDHrgBIb/review_all/p2" data-pg="2" class="NextPage" title="下一页" data-click-name="页码2" data-click-title="文字" data-click-shopuuid="laBkairQFDHrgBIb" data-click-pagetailurl="" data-click-curpage="1">下一页</a>
		</div>
"""
d=pq(html)
children=d.children()
flag=d.children().hasClass('NextPage')
print(children)#返回True
print(flag)
