from bs4 import BeautifulSoup
import requests
import random
import redis
import request_method
import redis

# single 单通道 ,multi 多通道
IP_CHANNEL = 'single' 
global_proxies = ""
'''
    代理ip获取
'''
def get_proxies():
    # 获取redis里的可用代理ip
    r = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
    ret = r.get('proxies')
    proxies_ = ""
    if IP_CHANNEL == 'single':
        ip_str = ret
        if ip_str is None:
            # 可用代理ip添加进redis
            ip_str = get_ip_single()
            # redis储存
            r.set('proxies', ip_str, ex=10800)
            proxies_ = {'http': 'http://' + ip_str}
    elif IP_CHANNEL == 'multi':
        if ret is None:
            ip_str = get_ip_list()
        else:
            ip_str = ret.split(",")
            # 测试ip可用
            ip_str = test_proxy_ip(ip_str)
        # 取随机ip
        proxies_ = get_random_ip(ip_str)
    return proxies_

'''
多通道获取代理ip数组
'''
def get_ip_list():
    # 多ip通道 可找一些代理IP网站
    http_url = "https://www.89ip.cn/" 
    web_data = request_method.get(http_url, None)
    soup = BeautifulSoup(web_data.text, "html.parser")
    ip_list = []
    ips = soup.find_all('tr')
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        tds_0 = tds[0].text.replace("\t", "").replace("\n", "")
        tds_1 = tds[1].text.replace("\t", "").replace("\n", "")
        proxies = {'http': 'http://' + tds_0 + ':' + tds_1}
        try:
            response_= requests.get('https://www.baidu.com', proxies=proxies, timeout=1)
            if response_.status_code == 200:
                ip_list.append(tds_0 + ':' + tds_1)
            else :
                continue
        except Exception as e:
            continue   
    # redis储存
    r = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
    r.set('proxies',  ",".join(ip_list), ex=360)
    return ip_list  
    except ValueError:
        print(ValueError)
        return ValueError
        
'''
单通道获取代理ip
'''
def get_ip_single():
    try:
        # 单ip通道(极光代理等ip代理网站获取ip) 
        https_url = "http://d.jghttp.alicloudecs.com/getip?num=1&type=3&pro=0&city=0&yys=0&port=11&time=2&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions=110000,230000,320000,330000,340000,360000,410000,420000,430000,450000,500000,520000"
        web_data = request_method.get(https_url, None)
        soup = BeautifulSoup(web_data.text, "html.parser")
        ip_str = soup.text.replace("\r", "").replace("\n", "")
        proxy = {'http': 'http://' + ip_str}
        # ip测试能否进行代理
        global global_proxies
        global_proxies = ""
        test_ip(proxy)
        return global_proxies
    except ValueError:
        print(ValueError)
        return ValueError

'''
测试当前代理ip是否成功代理
'''
def test_proxy_ip(proxies):

    ip_list = []
    for i in range(1, len(proxies)):
        proxiy = {'http': 'http://' + proxies[i] }
        try:
            response_= requests.get('https://www.baidu.com', proxies=proxiy, timeout=1)
            if response_.status_code == 200:
                ip_list.append(proxies[i])
            else :
                continue
        except Exception as e:
            continue   
    # redis储存
    r = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
    r.set('proxies',  ",".join(ip_list), ex=360)
    return ip_list

'''
根据ip列表,获取随机ip
'''
def get_random_ip(ip_list_):
    try:
        proxy_list = []
        for ip in ip_list_:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip}
    except ValueError:
        print(ValueError)
    return proxies

'''
测试list_ip可用性,使用百度测试
'''
def test_list_ip(proxies):
    rep = request_method.get(url='http://icanhazip.com', proxies=proxies)
    print(rep)

'''
测试ip可用性,使用百度测试
'''
def test_ip(proxies):
    try:
        response_= requests.get('https://www.baidu.com', proxies=proxies, timeout=2)
        if response_.status_code == 200:
            global global_proxies
            global_proxies = proxies
        else:
            get_ip_single()
    except Exception as e:
        get_ip_single()
