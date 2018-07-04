from urllib import request
import re
import time
import random
from py03_spider_day5 import mydownloader

proxy_switch = 1 # 1 使用代理  0 不使用代理
# 加载一次代理池
proxies = mydownloader.getProxy('proxy')

def parse_list(base_url):
    # base_url = 'http://www.xicidaili.com/nt/1'
    print('crawling page %s' % base_url)
    user_agnets = [
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'

    ]
    headers = {
        'User-Agent' : random.choice(user_agnets)
    }

    if not proxy_switch: # 不使用代理
        req = request.Request(base_url,headers=headers)
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
    else: # 使用代理
        req = request.Request(base_url,headers=headers)
        opener = mydownloader.getOpener(proxies)
        html = mydownloader.downloader(opener,req,proxies,retry=5)

    if html is not None:
        # html = response.read().decode('utf-8')
        tr_pattern = re.compile(r'<tr.*?>.*?</tr>',re.S) # 让.可以匹配换行
        tr_list = tr_pattern.findall(html)[1:]

        with open('ip','a',encoding='utf-8') as f:
            for tr in tr_list:
                td_pattern = re.compile('<td>(.*?)</td>')
                info_pattern = re.compile(r'title="(.*?)".*?title="(.*?)"',re.S)
                td_list = td_pattern.findall(tr)
                info_list = info_pattern.findall(tr)
                info_list = info_list[0]

                speed = info_list[0] # 获取连接速度
                speed = speed.replace('秒','')

                contime = info_list[1] # 获取连接时间
                contime = contime.replace('秒','')

                ip = td_list[0]
                port = td_list[1]
                contype = td_list[2]
                alive = td_list[3]
                if float(speed) < 0.5: # 过滤速度
                    if float(contime) < 0.5: # 过滤连接时间
                        if '天' in alive: # 过滤存活时间
                            alive = alive.replace('天','')
                            if int(alive) > 10:
                                f.write(' '.join([ip,str(port),contype,str(alive)]) + '\n')

# 构建分页请求
def getPage():
    start = input('输入起始页：')
    end = input('输入结束页：')
    for page in range(int(start),int(end) + 1):
        base_url = 'http://www.xicidaili.com/nn/%d'
        fullurl = base_url % page
        time.sleep(1)
        parse_list(fullurl)



if __name__ == '__main__':
    getPage()