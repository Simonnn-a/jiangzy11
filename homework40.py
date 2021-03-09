# _*_ conding:utf-8 _*-
# @Time:2021/1/4 &{TIME}
import requests
import json
import time
"""
#####################
数据
#####################
"""
data = {
    'username':'admin',
    'password':'123456'
}
data1 = {
    'city':'1'
}
data2 = {
     'openid': 'UEHUXUXU78272SDSassDD',
     'productid': 8888,
     'userid': 17890,
     'token': '23657DGYUSGD126731638712GE18271H'
}
data3 = {
     'cartid': 45233, 'openid': 'UEHUXUXU78272SDSassDD', 'productid': 8888, 'userid': 17890
}
data4 = {
     'limit':1
}
data5 = {
    'cardnum':10987
}
data6 = {
    'productid':88
}
data7 = {
    'city':2
}

# jsondata=json.dumps(data)#用dunmps对data进行转型，将原有的字典数据转为json格式
# print(type(jsondata))
# print(jsondata)
time.sleep(1)
# headers = {
#     'Content-Type': 'application/json'
# }

"""
#####################
headers
#####################
"""
headers2={
    'token':'23657DGYUSGD126731638712GE18271H'
}
headers3={
    'token':'23657DGYUSGD126731638712GE18271H'
}
headers8={
    'token':'23657DGYUSGD126731638712GE18271H'
}
headers9={
    'token':'cemaxueyuan'
}
headers10={
    'token':'cemaxueyuan'
}
"""
#####################
url
#####################
"""
url='http://39.98.138.157:5000/api/login'
url1='http://39.98.138.157:5000/api/getweather'
url2='http://39.98.138.157:5000/api/addcart'
url3='http://39.98.138.157:5000/api/createorder'
url4='http://39.98.138.157:5000/api/demo'
url5='http://39.98.138.157:5000/api/getbloodchecklist'
url6='http://39.98.138.157:5000/api/getproductinfo'
url7='http://39.98.138.157:5000/api/gettomorrow'
url8='http://39.98.138.157:5000/api/getuserinfo'
url9='http://39.98.138.157:5000/api/user/list'
url10='http://39.98.138.157:5000/api/user/viplist'
url11='http://39.98.138.157:5000/api/user/delete'
# res=requests.post(url=url,data=jsondata,headers=headers)

"""
#####################
response
#####################
"""
res=requests.post(url=url,json=data)
res1=requests.get(url=url1,json=data1)
res2=requests.post(url=url2,json=data2,headers=headers2)
res3=requests.post(url=url3,json=data3,headers=headers3)
res4=requests.get(url=url4,json=data4)
res5=requests.get(url=url5,json=data5)
res6=requests.get(url=url6,json=data6)
res7=requests.get(url=url7,json=data7)
res8=requests.get(url=url8,headers=headers8)
res9=requests.get(url=url9,headers=headers9)
res10=requests.get(url=url10,headers=headers10)
res11=requests.delete(url=url11)
res.close()
res1.close()
res2.close()
res3.close()
res4.close()
res5.close()
res6.close()
res7.close()
res8.close()
res9.close()
res10.close()
res11.close()
"""
#####################
显示
#####################
"""
print(res.status_code)
print(res.text)
# print(res.raise_for_status())
# print(res.content)
# print(res.raw)
# print(res.request.headers)
# content=json.loads(res.text)
# print(content)

print(res1.status_code)
print(res1.text)

print(res2.status_code)
print(res2.text)
# print(res2.request.headers)

print(res3.status_code)
print(res3.text)

print(res4.status_code)
print(res4.text)

print(res5.status_code)
print(res5.text)

print(res6.status_code)
print(res6.text)

print(res7.status_code)
print(res7.text)

print(res8.status_code)
print(res8.text)

print(res9.status_code)
print(res9.text)

print(res10.status_code)
print(res10.text)

print(res11.status_code)
print(res11.text)