# _*_ conding:utf-8 _*-
# @Time:2021/1/10 &{TIME}
import json
import jsonpath
import requests
class jiekouKey:
    def do_get(self,url,params=None,**kwargs):
        return requests.get(url=url,params=params,**kwargs)
    def do_post(self,url,data=None,**kwargs):
        return requests.post(url=url,data=data,**kwargs)
    def do_delete(self,url,**kwargs):
        return requests.delete(url=url,**kwargs)
    def get_text(self,txt,key):
        try:
            txt=json.loads(txt)
            value=jsonpath.jsonpath(txt,'$..{0}'.format(key))
            if value:
                if len(value) == 1:
                    return value[0]
                return value
        except Exception as e:
            return e
        return value

if __name__ == '__main__':
    ak = jiekouKey()
    data = {
        'username':'admin','password':'123456'
    }
    res = ak.do_get(url='http://39.98.138.157:5000/api/getuserinfo')
    print(res.text)
    res1=ak.do_post(url='http://39.98.138.157:5000/api/login', json=data)
    print(res1.text)


