# coding=utf-8
import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append(path1)
from utils.configuration import Configuration
case_excel = Configuration().get_Excel_Name()
path2 = os.path.join(path1,'test_case',case_excel)
import xlrd
from xlutils.copy import copy 

class Operate_Excel():
    def __init__(self,file=path2):
        self.file = file
        self.data = self.get_data()
    def get_data(self):
        data = xlrd.open_workbook(self.file).sheet_by_name('test_case')
        return data
    def get_rows(self):
        rows = self.data.nrows
        return rows
    def get_cell_value(self,row,col):
        value = self.data.cell_value(row,col)
        return value
    def get_row_fromid(self,id,col=0):
        row_datas = self.data.col_values(col)
        num = 0
        for x in row_datas:
            if id != x:
                num += 1
            else:
                return num
    def write_data(self,row,col,value):
        readdata = xlrd.open_workbook(self.file,formatting_info=True)
        writedata = copy(readdata)
        sheetdata = writedata.get_sheet(0)
        sheetdata.write(row,col,value)
        writedata.save(self.file)
    def setting_width(self):
        readdata = xlrd.open_workbook(self.file)
        copydata = copy(readdata)
        sheetdata = copydata.get_sheet(0)
        sheetdata.col(1).width = 256*15
        sheetdata.col(3).width = 256*50
        sheetdata.col(5).width = 256*50
        sheetdata.row(1).height_mismatch = True
        sheetdata.row(1).height = 20*30
        sheetdata.col(6).width = 256*40
        sheetdata.col(8).width = 256*18
        sheetdata.col(10).width = 256*15
        copydata.save(self.file)
if __name__ == '__main__':
    test = Operate_Excel()
    res = test.get_cell_value(1,1)
    print(res)