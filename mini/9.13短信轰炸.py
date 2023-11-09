import requests

phone = '18703340697'
url = 'https://m.16888.com/wap.php?mod=commonApi&extra=mobileCode&mobile='
url_rear = url + phone
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}
data = {
    'mod': 'commonApi',
    'extra': 'mobileCode',
    'mobile': '18703340697',
    'token': 'UtDGfdl4jez2',
    'verify': 'a294f522eb11ac9fc100cc397ffe5b45',
    '_': 1663079278745
}
"""

mod: commonApi
extra: mobileCode
mobile: 13367452768
token: UtDGfdl4jez2
verify: a294f522eb11ac9fc100cc397ffe5b45
_: 1663079456365
"""
resp = requests.get(url_rear, data=data)
print(resp.text)