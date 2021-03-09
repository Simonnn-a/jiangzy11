# _*_ conding:utf-8 _*-
# @Time:2021/1/11 &{TIME}
import requests
session = requests.session()
print(session.cookies)
url = 'http://39.98.138.157:5000/api/login'
data = {
    'username':'admin',
    'password':'123456'
}
res = requests.post(url=url, json=data)

url = 'http://39.98.138.157:5000/api/getuserinfo'
headers = {
    'token':res.json()['token']
}
res = requests.get(url=url, headers=headers)
print(res.text)
print(session.cookies)