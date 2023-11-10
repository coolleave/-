import requests

id_url = 'https://www.pearvideo.com/video_1470999'
ad = id_url.split('_')[1]


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
    "Referer": id_url}  # UA给他怼上
# 注意上边的referer是防盗链  防盗链就是溯源 上一个链接是不是指定链接


video_status = f'https://www.pearvideo.com/videoStatus.jsp?contId={ad}&mrd=0.4809772707893196'
# 上面的链接是xhr
# https://video.pearvideo.com/mp4/adshort/20210302/cont-1721371-15619988_adpkg-ad_hd.mp4


resp = requests.get(video_status, headers=headers)
# print(resp.json())
url = resp.json()['videoInfo']['videos']['srcUrl']  # 用索引找到字典中的伪视频链接
# print(url)


s1 = url.split('/')[-1].split('-')[0]  # 将伪链接中的需要替换切出来
url1 = url.replace(s1, f'cont-{ad}')  # 替换部分
print(url1)


resp2 = requests.get(url1)  # 请求解析网址
print(resp2)
with open('../视频/pv.mp4', 'wb')as f:  # 写入视频和写入图片的方法一样
    f.write(resp2.content)

print('over!')
