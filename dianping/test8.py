import re
from pyquery import PyQuery as pq

html="""
.berb0{background:-322.0px -56.0px;}.beqeo{background:-476.0px -582.0px;}.beeit{background:-322.0px -2258.0px;}.be2h1{background:-252.0px -2107.0px;}.be18h{background:-490.0px -2023.0px;}.belgd{background:-574.0px -2107.0px;}
"""

# keys_list=re.findall('\.(be[0-9a-zA-Z]{3})\{backgroud:-([0-9]+)\.0px\s-([0-9]+)\.0px;\}',html)
keys_list=re.findall('\.([0-9a-zA-Z]{5}?)\{background:-([0-9]+)\.0px\s-([0-9]+)\.0px;\}',html)
# keys_list=re.findall('\{.*?\}',html)
print(keys_list)
print(len(keys_list))