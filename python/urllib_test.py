from urllib import request

def get_url_content(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))

get_url_content('https://baike.baidu.com/item/%E6%A2%85%E8%89%B3%E8%8A%B3/230174?fr=aladdin')