from urllib import request,parse

# 构建一个代理字典
# proxy = {
#     'http' : 'http://61.155.164.107:3128', # 本机发起http请求  用代理服务器（字典值）
#     'https' : 'http://61.155.164.107:3128', # 本机发起https请求  用代理服务器（字典值）
# }

# 付费代理
proxy = {
    'http' : 'http://1752570559:wd0p04kd@117.48.199.243:16816',
    'https' : 'http://1752570559:wd0p04kd@117.48.199.243:16816'
}
# 创建代理处理器
proxy_handler = request.ProxyHandler(proxy)
opener = request.build_opener(proxy_handler)
base_url = 'http://www.baidu.com/s?wd=ip'
response = opener.open(base_url)
print(response.read().decode('utf-8'))