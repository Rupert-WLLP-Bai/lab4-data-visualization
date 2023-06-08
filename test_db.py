# 测试从数据库中读取数据

import unittest
from sqlalchemy import create_engine
import pandas as pd

# 连接字符串
connection_string = 'postgresql://postgres:1230@119.3.154.46:5432/test_salary'

class TestDB(unittest.TestCase):
    def test_read_data_from_postgres(self):
        # 创建到PostgreSQL数据库的连接
        engine = create_engine(connection_string)
        
        # 读取数据
        data = pd.read_sql('SELECT * FROM salary', engine)
        
        # 关闭数据库连接
        engine.dispose()
        
        # 断言数据的行数
        self.assertTrue(len(data) > 0)
        
        # 输出前5行数据
        print(data.head())
        
if __name__ == '__main__':
    unittest.main()