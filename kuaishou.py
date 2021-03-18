import requests
import json
import re
import request_method

'''
获取快手直播m3u8地址
'''
def get_m3u8_url(room_url, proxies):
    try:
        m3u8_url=""
        rep = request_method.get(url=room_url, proxies=proxies)
        response = rep.text
        # fd = open('./index.html', 'w')
        # print(response, file = fd)
        userid = re.findall(r'ID：<span>([\s\S]*?)</span></div>', response)[0]
        authname = re.findall(r'<div class="author-name">([\s\S]*?)</div>', response)[0]
        print(authname)
        print(userid)
        print(room_url)
        m3u8_url = re.findall(r'src="([\s\S]*?).m3u8([\s\S]*?)"', response)[0]
        m3u8_url= m3u8_url[0] + '.m3u8' + m3u8_url[1]
        m3u8_url = m3u8_url.replace("&#38;", "&")
    except Exception as e:
        m3u8_url = e
    return m3u8_url