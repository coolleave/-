# from urllib.request import urlopen
# url = 'http://121.26.242.250:8001/srcja.asp?dhhm1=aaaa'
# resp = urlopen(url)
# with open('pqyz.html', mode='w')as f:
#     f.write(resp.read().decode('gbk'))  # 读取到页面源代码
# print('over')


# import requests
# url = 'https://www.sogou.com/web?query=周杰伦'
# dic = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}
# resp = requests.get(url, headers=dic)
# resp = requests.get(url)
# print(resp.text)

import requests
url = 'https://api.cognitive.microsofttranslator.com/translate?from=' \
      'en&to=zh-CHS&api-version=3.0&includeSentenceLength=true'
dat = {'kw'}
requests.post(url)
