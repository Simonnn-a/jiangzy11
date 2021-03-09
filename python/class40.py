# _*_ conding:utf-8 _*-
# @Time:2021/1/4 &{TIME}
'''
    requests库实现的接口测试应用：
        1. 导包
        2. 接口请求的模拟
            1. 确定协议是http/https
            2. 确定请求需传递的参数：通过api文档进行确认
        3. 如果需要对请求的内容做一定限制，可以在参数中进行设置
            json 表示传入json格式的参数
            timeout 表示本次接口的调用超时时长的定义
            headers 表示本次接口传输时的headers当中自定义添加的内容
        4. 在requests库中，进行请求模拟时，请标注清晰每一个参数分别是什么
'''
import requests
import json

# 接口请求的模拟
# 数据的生成
data = {
    'username': 'admin',
    'password': '123456'
}
# 文件上传时的文件参数形式
file = {
    'file': open('../class10/report/report.html', 'r', encoding='utf-8')
}
# 将data转换为JSON对象：通过使用json库来进行转换
# dumps是进行转型，将原有的字典数据转换为json格式
jsonData = json.dumps(data)
# print(jsonData)
# print(type(jsonData))
# 请求头定义
# headers = {
#     'Content-Type': 'application/json'
# }
# 接口的地址
url = 'http://39.98.138.157:5000/api/login1'
data1 = {
    'limit': '1'
}
# 将数据传递到对应的接口地址，来实现一次该接口的请求下发并返回响应结果：定义对应的请求方法
res = requests.post(url=url, data=data)
res1 = requests.get(url='http://39.98.138.157:5000/api/demo', params=data1, timeout=0.1)
print(res1.text)
# 输出是一个响应对象，默认显示状态码
# print(res)
# 输出状态码
# print(res.status_code)
# 用于判断接口请求的状态码是否为200，如果是，则返回none，如果不是则返回异常，所以要调用时一定结合try...except进行使用
print(res.raise_for_status())
# # assert res == res.status_code
# # 输出响应结果：返回原始结果
# print(res.content)
# # 输出响应结果：编译后的内容
# print(res.json())
# # 最基本的响应原始内容
# # print(res.raw)
# # 请求头
# print(res.request.headers)
# # 数据进行转码：loads是将json格式的内容转换为字典的格式
# # content = json.loads(res.text)
# # 对响应结果进行内容的获取，并判断关键内容是否符合预期结果
# assert 'success' == res.json()['msg']