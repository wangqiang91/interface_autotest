import pymysql

class OperateMysql():
    def __init__(self):
        self.cursortest = self.connectTestMysql().cursor()
    def connectTestMysql(self):
        try:
            self.conntest = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="123456",
            )
            return self.conntest
        except:
            return "连接失败"
    def selectData(self,sql):
        try:
            self.cursortest.execute(sql)
            data = self.cursortest.fetchall()
            return data
        except:
            return "查询失败，请检查"
        finally:
            self.conntest.close()
    def addData(self,sql):
        try:
            self.cursortest.execute(sql)
            self.conntest.commit()
        except:
            self.conntest.rollback()
        finally:
            self.conntest.close()


if __name__ == "__main__":
    sql = "select * from find_job.course limit 7"
    # sql = "insert into find_job.course() values ('05','地理2','05')"
    res = OperateMysql().selectData(sql)
    print(res)
    # OperateMysql().connectTestMysql().close()
