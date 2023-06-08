import pandas as pd

# 从../dataset/college-salaries/salaries-by-region.csv读取数据
data = pd.read_csv('./dataset/college-salaries/salaries-by-region.csv')

# 处理数据，去除符号并转换为float类型
scatter_columns = ['Starting Median Salary', 'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary',
                   'Mid-Career 25th Percentile Salary', 'Mid-Career 75th Percentile Salary',
                   'Mid-Career 90th Percentile Salary']

for column in scatter_columns:
    data[column] = data[column].str.replace('$', '', regex=False)
    data[column] = data[column].str.replace(',', '', regex=False)
    data[column] = data[column].astype(float)

# 创建新的DataFrame，仅包含所需的列
new_data = data[['School Name', 'Starting Median Salary', 'Mid-Career Median Salar`y',
                 'Mid-Career 10th Percentile Salary', 'Mid-Career 25th Percentile Salary',
                 'Mid-Career 75th Percentile Salary', 'Mid-Career 90th Percentile Salary']].copy()

# 保存新的DataFrame到CSV文件
new_data.to_csv('cleaned_data.csv', index=False)
