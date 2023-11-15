# coding=utf-8
import os,sys
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path1)
import requests
import json
from utils.log import Log
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
    url = "https://open.jiehun.com.cn/search/entry/list"
    data = {"clientType": "1","pageId": "9999"}
    data = json.dumps(data)
    header = {
        'User-Agent':'Mozilla/5.0',
        "Content-Type":"application/json",
        # "token":"626ac3b97c8d97b3f8055881edbb85a2",
        "city-id":"330100"
    }
    res = Requests().port(url,'post',data,header)
    Log().info("请求接口参数：\n" + url + "\n" + data + "\n" + str(header))
    Log().info(res.text)
    print(res.json())

