import http.client
import hashlib
import urllib
import random
import json


def get_md5(s):
  # MD5加密签名
    md = hashlib.md5()
    md.update(s.encode('utf-8'))
    return md.hexdigest()


class BaiduTrans:
    def __init__(self, appid, secretKey):
        self.__appid = appid
        self.__secretKey = secretKey

    def translate(self, q):
        fetchUrl = '/api/trans/vip/translate'
        fromLang = 'auto'  # 原文语种
        toLang = 'zh'  # 译文语种
        salt = random.randint(32768, 65536)
        sign = self.__appid + q + str(salt) + self.__secretKey
        fetchUrl = fetchUrl + '?appid=' + self.__appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + get_md5(sign)
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', fetchUrl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            return result['trans_result'][0]['dst']
        except Exception as e:
            print('err', e)
        finally:
            if httpClient:
                httpClient.close()
