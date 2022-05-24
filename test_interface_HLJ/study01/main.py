import unittest
from unittest01 import TestMethod
import HTMLTestRunner

filepath = r"D:\study\practice\unittest\report\htmlreport.html"
fp = open(filepath,'wb')
suite_all = unittest.TestSuite()
suite_all.addTests([TestMethod('test_01'),TestMethod('test_02')]) 
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告").run(suite_all)
# unittest.TextTestRunner().run(suite_all)

# box = unittest.TestSuite()
# box.addTests([TestMethod("test_01"),TestMethod("test_02")])
# unittest.TextTestRunner().run(box)


