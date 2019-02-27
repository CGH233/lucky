#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os


def info(username, password):
    session = requests.Session()
    headers1 = session.get('https://account.ccnu.edu.cn/cas/login/').headers
    set_cookie = headers1['Set-Cookie'].split(';')[0].split('=')[1]
    r = session.get('https://account.ccnu.edu.cn/cas/login;jsessionid='+ set_cookie)
    soup = BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')

    tag = soup.find('section',attrs={'class':'row btn-row'})
    lt = tag.find('input',attrs={'name':'lt'})
    exec1 = tag.find('input',attrs={'name':'execution'})

    payload = {'username':username,
	       'password':password,
	       'lt':lt.get('value'),
	       'execution':exec1.get('value'),
	       '_eventId':'submit'}
    url = 'https://account.ccnu.edu.cn/cas/login;jsessionid='+ set_cookie + '?service=http%3A%2F%2Fone.ccnu.edu.cn%2Fcas%2Flogin_portal'
    r2 = session.post(url, data = payload)
    r3 = session.get('http://one.ccnu.edu.cn/cas/login_portal?ticket=ST-157563-dZldO1asnbbLC31qtlPF-account.ccnu.edu.cn')
    print(r3.headers)
    rr1 = session.get('http://one.ccnu.edu.cn/index')
    r4 = session.get('http://one.ccnu.edu.cn/user_portal/index')
    print(r4.json())
    return r4

