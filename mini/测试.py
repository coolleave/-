import requests

url = 'https://dushu.baidu.com/api/pc/getChapterContent?' \
          'data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|' + f'{cid}' + ',%22need_bookinfo%22:1}'
resp = requests.get(url)
dic = resp.json()
print(dic['data']['novel']['content'])
