封装pymysql模块

```python
import pymysql
from settings import DATABASE_INFO

class DoMysql:
    def __init__(self):

        self.conn = pymysql.connect(
            # connect中的参数是通过关键字参数传入的，但也可以通过**字典传入参数
            **DATABASE_INFO
        )

        self.cursor = self.conn.cursor()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        return res[0]

if __name__ == '__main__':
    res = DoMysql().execute_sql('select id from loan where MemberID = 11')
    print(res)
```

