from unicodedata import name
import unittest
from  requeststest import RunMain
class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.method = RunMain()
    # def setUp(self):
    #     self.method = RunMain()
    # def tearDown(self):
    #     print("======teardown")
    def test_01(self):
        url = "https://api.hunliji.com/hms/hljUser/appApi/userInformation/getInfo"
        header = {
            "token":"1ee57318edef141e32a7599cc17084cb",
            "phone":"1111"
        }
        res = self.method.send_get(url,header)
        self.assertEqual(res.json()["status"]["msg"],"成功","用例失败")
        # globals()['name'] = res.json()["data"]["weddingCityInfo"][0]["name"]
        print("第一个测试用例结束")
    def test_02(self):
        url = "https://api.hunliji.com/hms/hljUser/appApi/userInformation/getInfo"
        header = {
            "token":"1ee57318edef141e32a7599cc17084cb",
        }
        res = self.method.send_get(url,header)
        self.assertEqual(res.json()["status"]["msg"],"成功","用例失败")
        print("第二个测试用例结束")
        # print(name)
    def test_03(self):
        url = "https://api.hunliji.com/hms/hljUser/appApi/userInformation/getInfo"
        header = {
            "token":"1ee57318edef141e32a7599cc17084cb",
        }
        res = self.method.send_get(url,header)
        self.assertEqual(res.json()["status"]["msg"],"成功","用例失败")
        print("第三个测试用例结束")



if __name__ == '__main__':
    box = unittest.TestSuite()
    box.addTests([TestMethod("test_02"),TestMethod("test_03")])
    unittest.TextTestRunner().run(box)