import requests
import json
import re
import urllib.parse

'''
解析淘口令获取直播间url,并获取直播流
'''
def get_real_url(rid):
    try:
        # 解析淘口令
        room_url = 'https://api.taokouling.com/tkl/tkljm?apikey={0}&tkl={1}'.format('tFEWzfJLXn',rid)
        req = requests.get(url=room_url)
        response = req.json()
        # url UnEscape解码
        encode_url = urllib.parse.unquote(response.get('url'))
        feed_id = re.findall(r'"feed_id":"([\s\S]*?)"', encode_url)[0]
        spm = re.findall(r'&spm=([\s\S]*?)&', encode_url)[0]
        # 拼接淘宝直播间url 可在网页检查中查看network 获取直播流
        real_url = 'https://taobaolive.taobao.com/room/index.htm?spm={0}&feedId={1}'.format(spm,feed_id)
    except Exception as e:
        real_url = e
    return real_url


if __name__ == '__main__':
    # 此处填写淘宝直播淘口令
    real_url = get_real_url('$BV6OcAvrMjC$')
    print('该直播间源地址为：')
    print(real_url)