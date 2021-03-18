import requests
import re
import request_method

'''
获取抖音直播m3u8地址
'''
def get_m3u8_url(rid, proxies):
    try:
        if 'v.douyin.com' in rid:
            room_id = re.findall(r'(\d{19})', requests.get(url=rid).url)[0]
        else:
            room_id = rid
        room_url = 'https://webcast.amemv.com/webcast/reflow/'+ str(room_id)
        response = request_method.get(url=room_url, proxies=proxies).text
        # fd = open('./index.html', 'w')
        # print(response, file = fd)
        authname = re.findall(r'<p class="name-wrap">([\s\S]*?)</p>', response)[0]
        userid = re.findall(r'"display_id":"([\s\S]*?)"', response)[0]
        print(authname)
        print(userid)
        print(rid)
        m3u8_url = re.findall(r'"hls_pull_url":"([\s\S]*?).m3u8"', response)[0]
        m3u8_url = m3u8_url+'.m3u8'
    except Exception as e:
        m3u8_url = e
    return m3u8_url

