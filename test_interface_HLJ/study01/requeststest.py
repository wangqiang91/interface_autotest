import json
from operator import rshift
import requests

class RunMain():
    def send_get(self,url,header=None):
        res = requests.get(url,headers=header)
        return res
        # return json.dumps(res,indent=2,sort_keys=True)
    def send_post(self,url,data,header=None):
        res = requests.post(url,data,headers=header).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def send_put(self,url,data,header=None):
        res = requests.put(url,data.encode('utf-8'),headers=header)
        return res.json()

if __name__ == "__main__":
    # url = "https://api.hunliji.com/hms/hljUser/appApi/user"
    # data = '{"nick":"看星星01"}'
    # data = json.dumps(data)
    # header = {
    #     "Content-Type":"application/json",
    #     "phone":"c81cf4c35e52b236d4b719f258946c0c1eb00b88",
    #     "token":"1ee57318edef141e32a7599cc17084cb",
    # }
    url = "https://api.hunliji.com/hms/hljUser/appApi/userInformation/getInfo"
    header = {
        "token":"1ee57318edef141e32a7599cc17084cb",
        "phone":"1111"
    }
    res = RunMain().send_get(url,header)
    print(type(res))
    print(res.json())

