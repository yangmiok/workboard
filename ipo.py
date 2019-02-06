# -*- coding: utf-8 -*-
import requests
import string
import random


def postonetime():

    #随机生成手机号码
    def phone_num(num):
        all_phone_nums = ""
        num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                     '188',
                     '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
        for i in range(num):
            start = random.choice(num_start)
            end = ''.join(random.sample(string.digits, 8))
            res = start + end
            all_phone_nums = res
        return all_phone_nums

    s = requests.session()
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://www.chinaipo.com',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://www.chinaipo.com/index.php?app=public&mod=Register&act=index',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
        'Cookie':'__cfduid=d6d31ca2d7239b842438738aa27e860eb1527671641; PHPSESSID=4aim6uk6kn103rq14vfanbo9a0; yjs_id=dc22140fa243d1d46891cef28a73a790; XSBlang=en; ctrl_time=1; Hm_lvt_61a2d81fc23a3a8087c8791bf55f7e6e=1543455586,1543469246,1543543077,1543803591; Hm_lpvt_61a2d81fc23a3a8087c8791bf55f7e6e=1543803591',
    }

    phone = phone_num(1)
    phone = str(phone)

    data = {'phone': phone,
            'verify': 'KPJRV',}
    url = ''
    response = s.post(url, headers=headers, data=data)
    print(response.content)
    return response.content

if __name__ == "__main__":
    for i in range(0,100):
        postonetime()
