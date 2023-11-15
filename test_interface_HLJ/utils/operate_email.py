# coding=utf-8
import base64
import os
import time
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append(path1)
from utils.configuration import Configuration
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
class SendEmail():
    def __init__(self,email_host="smtp.qq.com",send_name="1316469308@qq.com"):
        self.email_host = email_host
        self.send_name = send_name
        self.email_frame = MIMEMultipart()
        self.send_user = "飘飘落叶" + " "  + "<" +"1316469308@qq.com" +">"
    def email_message(self):
        name64str = str(base64.b64encode(bytes("飘飘落叶", 'utf-8')),'utf-8')
        fromnamestr = '"=?utf-8?B?' + name64str + '=?=" <' + "1316469308@qq.com" + ">"
        self.receive_list = Configuration().get_Receive_Email()
        sub = '接口自动化测试报告'
        self.email_frame['From'] = fromnamestr
        self.email_frame['To'] = ";".join(self.receive_list)
        self.email_frame['Subject'] = sub
    def email_content(self,pass_list,fail_list,total_time):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_rate = "%.2f%%" %(pass_num/count_num*100)
        content = f'本次测试执行了{total_time}秒，共运行{count_num}个接口，成功{pass_num}个，失败{fail_num}，通过率为{pass_rate}!运行失败的测试用例：{fail_list}'
        email_content = MIMEText(content,_subtype='plain',_charset='utf-8')
        self.email_frame.attach(email_content)
    def email_accessory(self):
        try:
            case_excel = Configuration().get_Excel_Name()
            accessory01 = os.path.join(path1,'test_case',case_excel)
            with open(accessory01,'rb') as as1:
                add_accessory = MIMEApplication(as1.read())
                add_accessory["Content-Type"] = 'application/octet-stream'
                add_accessory["Content-Disposition"] = 'attachment; filename="interfaceTestReport.xls"'
                self.email_frame.attach(add_accessory)
            accessory02 = os.path.join(path1,'logs','%s.log'%time.strftime('%Y_%m_%d'))
            with open(accessory02,"rb") as as2:
                attachment2 = MIMEApplication(as2.read(), _subtype='txt')
                attachment2.add_header('Content-Disposition', 'attachment', filename=f'{time.strftime("%Y_%m_%d")}.txt')
                self.email_frame.attach(attachment2)
        except:
            print("添加附件异常")
        
    def email_server(self):
        server = smtplib.SMTP()
        server.connect(self.email_host)
        server.login(self.send_name,'buhdpheoqahihdje')
        server.sendmail(self.send_user,self.receive_list,self.email_frame.as_string())
        server.close()
    def email_main(self,pass_list,fail_list,total_time):
        self.email_message()
        self.email_content(pass_list,fail_list,total_time)
        self.email_accessory()
        self.email_server()


if __name__ == '__main__':
    pass_list = [1,2,3,4]
    fail_list = []
    total_time = 5.56
    sendeamil = SendEmail().email_main(pass_list,fail_list,total_time)