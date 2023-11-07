import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
# 通过抓包工具可以得知，以下数据，其中efg都是定值
song_id = '31445554'
data = {
    'csrf_token': "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "3",
    'pageSize': "20",
    'rid': f"R_SO_4_{song_id}",
    'threadId': f"R_SO_4_{song_id}"
}
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a87' \
    '6aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d0' \
    '5c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
# i是通过随机数获得，并且通过网易算法计算出encSecKey的值，把i的值固定下来，得到对应的值，就用这一套值
i = 'Pkz5tKHCnKOoFqfH'
encSecKey = 'c2ee9cda3f1f0b4c6340734a22a88f8501feebe4dceacfb4840d6b0922581e062f60f3' \
           '297f75dc2d48481937d06988e6be11d1f749cb6664d34c74786239d3f15f348927ec39' \
           'c1c0e32f26b99984133ad130d9153f24b35c6a6d288695c23bd7fb377e545742056fba5' \
           'dddacf04a29dfaca419c390a8d72d7b7c01b75898dbf8'
"""
window.asrsea
加密过程
 function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { # d是本身的参数，e是010001 
        var h = {}
          , i = a(16);
        h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        return h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
"""


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad)*pad
    return data


def get_param(data):  # 默认收到的是字符串
    first = get_text(data, g)  # 第一次加密函数
    sec = get_text(first, i)  # 第二次加密函数
    return sec


# 加密函数
def get_text(data, key):
    iv = '0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs), 'utf-8')


resp = requests.post(url, data={
    'params': get_param(json.dumps(data)),
    'encSecKey': encSecKey
})
# print(resp.text)
dic = resp.json()
# print(dic['data']['comments'])
for comment in dic['data']['comments']:
    print(comment['content'])
