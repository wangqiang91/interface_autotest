import pymysql

class OperateMysql():
    def __init__(self):
        self.conn = self.connectTestMysql()
        self.cur = self.conn.cursor()
    def connectTestMysql(self):
        try:
            conntest = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="123456",
                database="interface_autotest",
                charset="utf8"
            )
            return conntest
        except:
            return "连接失败"
    def select_data(self,sql):
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            for row in data:
                print(row) 
        except:
            return "查询失败，请检查"
        finally:
            self.conn.close()
    def insert_data(self,insert_list):
        sql_insert = "insert into executed_test_cases (case_id,case_name,url,method,headers,data,expect,min_length,execute_time,spend_time,is_pass,error_message) values (%s,%s,%s,%s,%s,%s,%s,%r,%s,%s,%r,%s);"
        try:
            self.cur.execute(sql_insert,insert_list)
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()
    def close(self):
        self.conn.close()
        self.cur.close()


if __name__ == "__main__":
    sql = "select * from executed_test_cases;"
    insert_list = ["test_002","002的名称","www.baidu.com","post","请求头header","请求体data","测试期望",200,"2023-11-14","1.5",0,"error错误信息嘿嘿嘿"]
    # print(OperateMysql().select_data(sql))
    OperateMysql().insert_data(insert_list)
    OperateMysql().close()

