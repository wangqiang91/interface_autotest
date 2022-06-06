import pymysql

class OperateMysql():
    def __init__(self):
        self.cursortest = self.connectTestMysql()
    def connectTestMysql(self):
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
        )
        cursor = conn.cursor()
        return cursor
    def selectData(self,sql):
        self.cursortest.execute(sql)
        data_list = []
        for i in self.cursortest.fetchall():
            data_list.append(i)
        return data_list


if __name__ == "__main__":
    sql = "select * from find_job.course limit 7"
    res = OperateMysql().selectData(sql)
    print(res)

