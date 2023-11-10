# 尝试爬取梨视频 防盗链
"""
1、拿到id
2、拿到XHR中返回的json -> src url
3、对拿到的url进行修整
4、下载视频
"""
import requests


url_raw = 'https://www.pearvideo.com/video_1741350'
url1 = 'https://video.pearvideo.com/mp4/adshort/20210910/1661176910754-15765120_adpkg-ad_hd.mp4'
ad = 'cont' + url_raw.split("_")[1]
json_url = f'https://www.pearvideo.com/videoStatus.jsp?contId={ad}&mrd=0.722910306719668'
resp = requests.get(json_url)
s1 = url1.replace('1661176910754', 'cont-1741350')
print(s1)
