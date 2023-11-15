import json
import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
path2 = os.path.join(path1,'test_case','configuration.json')


class Configuration():
    def __init__(self,excel_file = path2):
        self.file = excel_file
        self.f = open(self.file)
        self.data = json.loads(self.f.read())
        self.f.close()
    def get_Excel_Name(self):
        return self.data["fileName"]
    def get_Receive_Email(self):
        emails = self.data["receiveEmail"]
        email_list = emails.split(",")
        return email_list

if __name__ == '__main__':
    data = Configuration().get_Receive_Email()
    print(data)
