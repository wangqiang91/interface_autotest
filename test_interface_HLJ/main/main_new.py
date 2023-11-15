# coding=utf-8
import datetime
import sys
import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path1)
import time
from utils.operate_email import SendEmail
from utils.operate_request import Requests
from get_data.get_case_data import Get_Case_Data
from utils.operate_mysql import OperateMysql
from utils.log import Log
class Main():
    def __init__(self):
        self.getdata = Get_Case_Data()
        self.request = Requests()
        self.sendemail = SendEmail()
        self.operatemysql = OperateMysql()
        self.log = Log()
    def while_case_success(self,row,res):
        self.getdata.write_data_toispass(row, 'PASS')
        self.getdata.write_data_dotime(row)
        spend_time = res.elapsed.total_seconds()
        self.getdata.write_data_spendtime(row, spend_time)

    def while_case_fail(self,row):
        self.getdata.write_data_toispass(row, 'ERROR')
        self.getdata.write_data_dotime(row)
    def other_fail(self,row):
        self.getdata.write_data_toispass(row, '接口异常/超时')
        self.getdata.write_data_dotime(row)
        self.getdata.write_data_spendtime(row, '')

    def statistical_data(self,start_time,end_time,pass_list,fail_list):
        all_time = end_time-start_time
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_rate = "%.2f%%" % (pass_num/count_num*100)
        response =  '本次测试执行了%f秒,共运行%d个接口，成功%d个，失败%d，通过率为%s!运行失败的测试用例：%s' % (
            all_time, count_num, pass_num, fail_num, pass_rate,fail_list)
        print(response)
        return response

    def runcase(self):
        casenum = self.getdata.get_casenum()
        pass_list = []
        fail_list = []
        start_time = time.time()
        for row in range(1, casenum):
            caseid = self.getdata.get_caseid(row)
            casename = self.getdata.get_case_name(row)
            isgo = self.getdata.get_isgo(row)
            url = self.getdata.get_url(row)
            method = self.getdata.get_method(row)
            header = self.getdata.get_headers(row)
            data = self.getdata.get_data(row)
            expect = self.getdata.get_expect(row)
            min_length = self.getdata.get_min_length(row)
            relyid = self.getdata.get_row_from_relyid(row)

            if isgo == 'Y':
                try:
                    if relyid:
                        data = self.getdata.get_newdata(row)
                    res = self.request.port(url, method, data, header)
                    insert_list = [caseid,casename,url,method,str(header),data,expect,min_length,str(datetime.datetime.now()),str(res.elapsed.total_seconds())]
                    res_str = str(res.json())
                    # print(res1)
                    res_text = res.text
                    if (expect in res_str) and (res.status_code == 200) and (len(res_text) >= min_length):
                        self.while_case_success(row,res)
                        pass_list.append(caseid)
                        # print(insert_list)
                        self.operatemysql.insert_data(insert_list + [1,""])
                    else:
                        self.while_case_fail(row)
                        fail_list.append(caseid)
                        self.log.info("请求接口参数：\n" + url + "\n" + data + "\n" + str(header))
                        self.log.error(res_str)
                        self.operatemysql.insert_data(insert_list + [0,res_text])
                except Exception as e:
                    self.log.info("请求接口参数：\n" + url + "\n" + data + "\n" + str(header))
                    self.log.error(e)
                    self.other_fail(row)
                    fail_list.append(caseid)
                    self.operatemysql.insert_data(insert_list + [0,e])
                    print(e)
            else:
                self.getdata.write_data_toispass(row, "")
        end_time = time.time()
        if fail_list:
            self.sendemail.email_main(pass_list, fail_list, end_time-start_time)  # 发送邮件
        # self.request.feishu_message(self.statistical_data(start_time,end_time,pass_list,fail_list))  # 飞书发送消息
        self.statistical_data(start_time,end_time,pass_list,fail_list)
        self.operatemysql.close()
        

if __name__ == '__main__':
    test = Main().runcase()
    print("")
