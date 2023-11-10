import requests


def write():
    with open('name.txt', mode='w', encoding='utf-8')as f:
        f.write('2''\n')
        f.write('3')


def request():
    url = 'http://121.26.242.250:8001/jsxx.asp'
    dic = {
        'Cookie': 'zzx2=%C0%EE%D1%F3; mm3=202205sm; dlmkq3=%B8%DF%CF%B2%D4%AA; dlmzzx1=%CD%F5%BD%A8%BA%EC; mm6=; mm18=bkf202207; dlma5=%B7%EB%D3%F1%BD%F0; dlmqj=0314; dlmkq1=%CD%F5%D3%C0%C8%AA; lzkf=200; wzkf=200; dlmcca=%D5%C5%D3%C0%C3%F1; dlmp=%CB%CE%D5%BC%C3%F7; dlme=%C7%C7%B9%FA%C8%F0; dlmkq2=%B9%F9%B6%AB%BB%D4; dlmzzx3=%D5%B2%B4%AB%B2%C6; ltyf=295; wtyf=227; wbkf=443; wzdf=506; lbkf=430; lzdf=487; zksj=2022zk; dlmss4=%B7%EB%D3%F1%BD%F0; mm2=202207lk; mm4=; sjb=%C8%AB; sbma=b; dlmf=%D5%C5%D3%C0%C3%F1; dlmcj2=%B4%DE%D1%F4; sksjb=2022%2F9%2F4; mm19=bkf202206; mm20=bkf202205; dlmdd=%CD%F5%D3%C0%C8%AA; dlmc=%B7%EB%D3%F1%BD%F0; dlma3=%B9%AC%D7%D3%BA%CD; dlmcj1=%B3%C2%C1%BC%D3%F1; gksj=2022gk; mm7=202205yk; mm16=202208; dlmccc=%B6%C5%C1%A2%C9%FA; srgkcj=; dlm=%BA%EE%D0%E3%D1%DE; dlma=78963; ljma=; jggz1=; yzxh=+; njaa1=3; zha=; yhb1=%A1%CC; nja2=0; njx1=1; njb1=0; njy1=0; njc1=0; aa1=1; kma2=%CA%FD%D1%A7; ldbj=; ldbjb=59188; yjxx=%C6%BD%C8%AA%CF%D8%D2%BB%D6%D0; bgs=206; zp1=; nj4=3; kma1=%CA%FD%D1%A7; nja4=+; cjkma=cjk; ipdz=10%2E40%2E6%2E15; xha1=80137; nja1=3; yh2=13603140429; zbxh1=01; kma3=sx; dlxha=0; bjaa1=1112; njd1=0; bzr1=; bgl=%B2%A9%D1%C5%C2%A5; xj1=%2A; nja3=+; sbmyz=b'

    }

    resp = requests.get(url, headers=dic)
    resp.encoding = 'gbk'
    print(resp.text)


if __name__ == '__main__':
    request()
