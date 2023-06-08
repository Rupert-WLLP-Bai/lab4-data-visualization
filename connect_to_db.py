# 连接数据库
import pandas as pd
from sqlalchemy import create_engine

def store_data_to_postgres(data, table_name, connection_string):
    # 创建到PostgreSQL数据库的连接
    engine = create_engine(connection_string)

    # 将DataFrame存储到PostgreSQL数据库中
    data.to_sql(table_name, engine, index=False, if_exists='replace')
    
    # 关闭数据库连接
    engine.dispose()
    
    print('数据已存储到PostgreSQL数据库中！')
    
def get_connection_string(user, password, host, port, database):
    # 构建连接字符串
    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    
    return connection_string

def main():
    # 读取数据
    data = pd.read_csv('./cleaned_data.csv')
    
    # 连接字符串
    user = 'postgres'
    password = '1230'
    host = '119.3.154.46'
    port = '5432'
    database = 'test_salary'
    connection_string = get_connection_string(user, password, host, port, database)
    
    # 存储数据
    store_data_to_postgres(data, 'salary', connection_string)
    
if __name__ == '__main__':
    main()