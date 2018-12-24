"""
Pandas中有Series和DataFrame两种重要的数据结构。
    Series：是一个定长的字典序列。有两个基本属性：index，values
    DataFrame：类似于数据库表的一种数据结构。我们甚至可以像操作数据库表那样对DataFrame数据进行
    连接，合并，查询等等
    常用DataFrame进行数据清晰：用到的发方法有:
        去重删除：drop()，drop_duplicates(),rename()
        去空格：strip(),lstrip(),rstrip()
        变换大小写：upper(),lower(),title()
        改变数据格式：astype()
        查找空值：lsnull
        apply


"""
from pandas import DataFrame

# Scores of students
scores = {'Chinese': [66, 95, 95, 90, 80, 80],
          'English': [65, 85, 92, 80, 90, 90],
          'Math': [None, 98, 96, 77, 90, 90],
          'Total': [None, None, None, None, None, None]}
df = DataFrame(scores, index=['Zhang Fei', 'Guan Yu', 'Zhao Yun', 'Huang Zhong', 'Dian Wei','Dian Wei'],)

# Data ckeaning.
# remove the duplicated record.
df = df.drop_duplicates()
# print(df)

# Calculate the total scores.
df['Total'] = df.sum(axis=1)
print(df.describe())