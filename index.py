# import requests
import douyin
import kuaishou
import re
import sys
import codecs
import proxies
import redis
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

'''
获取各个直播平台直播流(m3u8,flv等)
'''
def redirect(platform, arg):
    proxies_ = proxies.get_proxies()
    try:
        if platform == 'douyin':
            real_url = douyin.get_real_url(arg, proxies_)
        elif  platform == 'kuaishou':
            real_url = kuaishou.get_real_url(arg, proxies_)
        else:
            real_url = '未找到文件'
    except Exception as e:
        real_url = e
    return real_url

if __name__ == '__main__':
    # 脚本形式传参
    # real_url = redirect(sys.argv[1], sys.argv[2])
    # 抖音
    # real_url = redirect('douyin', 'https://v.douyin.com/e8uxu1H/')
    # 快手
    real_url = redirect('kuaishou', 'https://v.kuaishou.com/cwvL67')
    print(real_url)