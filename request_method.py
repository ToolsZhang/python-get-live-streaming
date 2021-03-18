import requests

'''
简单封装requests
'''
def get(url, proxies):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        if proxies:
            return requests.get(url=url, headers=headers, proxies=proxies)
        else:
            return requests.get(url=url, headers=headers)
    except Exception as e:
        return e