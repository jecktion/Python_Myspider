import random
from urllib import request
def getProxy():
    with open('proxy', 'r') as f:
        proxy_list = f.readlines()  # 读取每一行
        proies = []
        for pro in proxy_list:  # 循环获取代理信息，追加到列表中
            proxy_info = pro.replace('\n','').split(' ')
            proxy = {}  # 代理字典
            proxy['http'] = proxy_info[2] + '://' + proxy_info[0] + ':' + proxy_info[1]
            proxy['https'] = proxy_info[2] + '://' + proxy_info[0] + ':' + proxy_info[1]
            proies.append(proxy)

    return proies

def getOpener(proies):
    proxy = random.choice(proies)
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    return opener