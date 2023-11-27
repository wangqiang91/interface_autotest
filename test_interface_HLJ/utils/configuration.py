import json
import os
import configparser
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Configuration():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(path1 + r"/test_case/test.conf",encoding="utf-8")
    def get_Excel_Name(self):
        return self.config.get('run_test_case_file','fileName')
    def get_Receive_Email(self):
        email_receivers = self.config.get('receiveEmail','receiveEmail')
        mail_receivers_list = email_receivers.split(",")
        return mail_receivers_list
# class Configuration():
#     def __init__(self,excel_file = path2):
#         self.file = excel_file
#         self.f = open(self.file)
#         self.data = json.loads(self.f.read())
#         self.f.close()
#     def get_Excel_Name(self):
#         return self.data["fileName"]
#     def get_Receive_Email(self):
#         emails = self.data["receiveEmail"]
#         email_list = emails.split(",")
#         return email_list

if __name__ == '__main__':
    data = Configuration().get_Receive_Email()
    print(data)