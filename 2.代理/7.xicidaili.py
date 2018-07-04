from urllib import request
import re

base_url = 'http://www.xicidaili.com/nt/1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
}

req = request.Request(base_url,headers=headers)
response = request.urlopen(req)
html = response.read().decode('utf-8')

tr_pattern = re.compile(r'<tr.*?>.*?</tr>',re.S) # 让.可以匹配换行
tr_list = tr_pattern.findall(html)[1:]

with open('ip','w',encoding='utf-8') as f:
    for tr in tr_list:
        td_pattern = re.compile('<td>(.*?)</td>')
        td_list = td_pattern.findall(tr)
        ip = td_list[0]
        port = td_list[1]
        f.write(ip + ':' + port + '\n')
