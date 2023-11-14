# coding=utf-8
import requests
import json

class Requests():
    def port(self,url,method,data,header=None,time_out=3):
        if method == 'get':
            res = requests.get(url,data.encode('utf-8'),headers=header,timeout=time_out)
            return res
        if method == 'post':
            res = requests.post(url,data.encode('utf-8'),headers=header,timeout=time_out)
            return res
        if method == 'put':
            res = requests.put(url,data.encode('utf-8'),headers=header,timeout=time_out)
            return res
        if method == 'delete':
            res = requests.delete(url,data.encode('utf-8'),headers=header,timeout=time_out)
            return res
        else:
            return '方法异常，请检查。'
    def feishu_message(self,feishu_content):
        url = 'https://open.feishu.cn/open-apis/bot/v2/hook/c8ea3367-6906-4090-9537-e558e245e8c5'
        data = {
            "msg_type":"text",
            "content":{
                "text":feishu_content
            }
        }
        data = json.dumps(data)
        header = {
            "Content-Type":"application/json"
        }
        res = requests.post(url,data,headers=header)
        return res

if __name__ == '__main__':
    url = "https://open.jiehun.com.cn/search/entry/hot/v1"
    data = '{"nick":"看星星01"}'
    # data = json.dumps(data)
    header = {
        "Content-Type":"application/json",
        "phone":"c81cf4c35e52b236d4b719f258946c0c1eb00b88",
        "token":"1ee57318edef141e32a7599cc17084cb",
    }
    res = Requests().port(url,'put',data,header)
    print(res.json())

