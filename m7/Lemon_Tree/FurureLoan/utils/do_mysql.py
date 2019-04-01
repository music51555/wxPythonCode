import pymysql
from settings import DATABASE_INFO

class DoMysql:
    def __init__(self):

        self.conn = pymysql.connect(
            **DATABASE_INFO
        )

        self.cursor = self.conn.cursor()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        if res:
            return res[0]
        else:
            return None

if __name__ == '__main__':
    DoMysql().execute_sql('select LeaveAmount from member where MobilePhone = 18611848465')
