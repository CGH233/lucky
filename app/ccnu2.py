import requests
from pprint import pprint

HEADER = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Control-Allow-Headers": "X-Requested-With",
    "Host": "spoc.ccnu.edu.cn",
    "Content-Type": "application/json",
    "Origin": "http://spoc.ccnu.edu.cn",
    "Referer": "http://spoc.ccnu.edu.cn/studentHomepage",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}

LOGIN = [
    "http://spoc.ccnu.edu.cn/userLoginController/getUserProfile",
    "http://spoc.ccnu.edu.cn/userInfo/getUserInfo",
]

def get_info(session, userId):
    response = session.get("http://spoc.ccnu.edu.cn/userInfo/getUserInfo")
    return str(response.json())


def login_once(USERNAME, PASSWORD):
    session = requests.Session()
    response = session.get("http://spoc.ccnu.edu.cn/userLoginController/getVerifCode")
    payload = {
        "loginName": USERNAME,
        "password": PASSWORD,
    }
    for url in LOGIN:
        response = session.post(url,data=payload)
    if 'Content-Language' not in response.headers:
        userInfo = response.json()
        uid = userInfo.get("data").get("userInfoVO").get("id")
        return get_info(session, uid) #获取个人信息
    else:
        return None
