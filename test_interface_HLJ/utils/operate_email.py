# coding=utf-8
import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append(path1)
from utils.configuration import Configuration
case_excel = Configuration().get_Excel_Name()
path3 = os.path.join(path1,'test_case',case_excel)
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
    def email_message(self):
        self.send_user = "飘飘落叶" + "<" +"1316469308@qq.com" +">"
        self.receive_list = Configuration().get_Receive_Email()
        sub = '接口自动化测试报告'
        self.email_frame['From'] = self.send_user
        self.email_frame['To'] = ";".join(self.receive_list)
        self.email_frame['Subject'] = sub
    def email_content(self,pass_list,fail_list,total_time):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_rate = "%.2f%%" %(pass_num/count_num*100)
        content = '本次测试执行了%f秒，共运行%d个接口，成功%d个，失败%d，通过率为%s!' %(total_time,count_num,pass_num,fail_num,pass_rate)
        email_content = MIMEText(content,_subtype='plain',_charset='utf-8')
        self.email_frame.attach(email_content)
    def email_accessory(self):
        accessory = path3
        add_accessory = MIMEApplication(open(accessory,'rb').read())
        add_accessory["Content-Type"] = 'application/octet-stream'
        add_accessory["Content-Disposition"] = 'attachment; filename="interfaceTestReport.xls"'
        self.email_frame.attach(add_accessory)
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