import requests

parm={             "ck": "",
                    "area_code": "+86",
                    "number": "18937057052"
    }

hrader={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Referer':'https://accounts.douban.com/passport/login_popup?login_source=anony',
    # 'Host':'accounts.douban.com',
    # 'X-Requested-With':'XMLHttpRequest',
    'Cookie':'ll="108258"; bid=-K8egElCKj8; __utmc=30149280; _vwo_uuid_v2=D974E94D5D37E8D99F881CCA4EB4E7610|56e1b182b9dd62a81a855f54dbdd6963; douban-fav-remind=1; apiKey=; __gads=ID=dafff9f799cac006:T=1569208163:S=ALNI_MZ4tylO6lH_PtharBU-8nz-sm7lBw; login_start_time=1589027138854'
}
resp=requests.post(url='https://accounts.douban.com/j/mobile/login/request_phone_code',data=parm,headers=hrader)
print(resp.text)