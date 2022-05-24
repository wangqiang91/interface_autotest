# coding=utf-8
import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append(path1)
from utils.operate_excel import Operate_Excel
from utils.operate_request import Requests
import datetime
import json
class Get_Case_Data():
    def __init__(self):
        self.caseid = 0
        self.casename = 1
        self.isgo = 2
        self.url = 3
        self.method = 4
        self.headers = 5
        self.data = 6
        self.relyid = 7
        self.relyfield = 8
        self.casefield = 9
        self.expect = 10
        self.minlength = 11
        self.ispass = 12
        self.dotime = 13
        self.spendtime = 14
        self.opera_excel = Operate_Excel()
        self.opera_request = Requests()
    def get_casenum(self):
        casenum = self.opera_excel.get_rows()
        return casenum
    def get_caseid(self,row):
        col = self.caseid
        value = self.opera_excel.get_cell_value(row,col)
        return value
    def get_isgo(self,row):
        col = self.isgo
        value = self.opera_excel.get_cell_value(row,col)
        return value
    def get_url(self,row):
        col = self.url
        value = self.opera_excel.get_cell_value(row,col)
        if value == '':
            return 'url错误'
        else:
            return value
    def get_method(self,row):
        col = self.method
        value = self.opera_excel.get_cell_value(row,col)
        return value
    def get_headers(self,row):
        col = self.headers
        value = self.opera_excel.get_cell_value(row,col) 
        if value == '':
            return {}
        else:
            header = dict(x.split(":") for x in value.split("\n"))
            return header
    def get_data(self,row):
        col = self.data
        value = self.opera_excel.get_cell_value(row,col)
        if value == '':
            return '{}'
        else:
            return value
    '''根据relyid找到对应的行号'''
    def get_row_from_relyid(self,row):
        col = self.relyid
        value = self.opera_excel.get_cell_value(row,col)
        if value == '':
            return None
        else:
            res = self.opera_excel.get_row_fromid(value)
            return res
    '''根据行号得到relyfield对应的数据'''
    def get_relyfield_data(self,row):
        rely_row = self.get_row_from_relyid(row)
        url = self.get_url(rely_row)
        data = str(self.get_data(rely_row))
        method = self.get_method(rely_row)
        header = self.get_headers(rely_row)
        res = self.opera_request.port(url,method,data,header).json()
        col = self.relyfield
        value = self.opera_excel.get_cell_value(row,col)
        list1 = value.split(',')
        for x in range(len(list1)):
            if list1[x].isdigit():
                list1[x] = int(list1[x])
        if len(list1) == 1:
            return res[list1[0]]
        if len(list1) == 2:
            return res[list1[0]][list1[1]]
        if len(list1) == 3:
            return res[list1[0]][list1[1]][list1[2]]
        if len(list1) == 4:
            return res[list1[0]][list1[1]][list1[2]][list1[3]]
    def get_casefield(self,row):
        col = self.casefield
        value = self.opera_excel.get_cell_value(row,col)
        return value 
    def get_newdata(self,row):
        data = self.get_data(row)
        key1 = self.get_casefield(row)
        value1 = str(self.get_relyfield_data(row))
        data = data[:-1] + ',"' + key1 + '":"'+ value1 + '"}' 
        return data
    def get_expect(self,row):
        col = self.expect
        value = self.opera_excel.get_cell_value(row,col)
        return value
    def get_min_length(self,row):
        col = self.minlength
        value = self.opera_excel.get_cell_value(row,col)
        if value == '' or value == ' ':
            return 0
        else:
            return value
    def write_data_toispass(self,row,value):
        col = self.ispass
        self.opera_excel.write_data(row,col,value)
    def write_data_dotime(self,row):
        col = self.dotime
        nowtime = str(datetime.datetime.now())
        self.opera_excel.write_data(row,col,nowtime)
    def write_data_spendtime(self,row,value):
        col = self.spendtime
        self.opera_excel.write_data(row,col,value)


if __name__ == '__main__':
    test = Get_Case_Data().get_caseid(3)
    print(type(test))
    