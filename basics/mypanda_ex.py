import pandas as pd

# 1D data
data = [10, 20, 30, 40, 50]
dataFrame = pd.Series(data)
print(dataFrame)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64
print("------------")

data = {
    "name": ["std1", "std2", "std3", "std4", "std5", "std6", "std7", "std8", "std9", "std10", "std11"],
    "marks": [10,20,30,40,50,60,70,80,90,100,110]
}
df = pd.DataFrame(data)
print(df)
#      name  marks
# 0    std1     10
# 1    std2     20
# 2    std3     30
# 3    std4     40
# 4    std5     50
# 5    std6     60
# 6    std7     70
# 7    std8     80
# 8    std9     90
# 9   std10    100
# 10  std11    110
print("------------")

print(df.head()) # first 5 rows
#    name  marks
# 0  std1     10
# 1  std2     20
# 2  std3     30
# 3  std4     40
# 4  std5     50
print("------------")
print(df.head(7)) # first 7 rows
#    name  marks
# 0  std1     10
# 1  std2     20
# 2  std3     30
# 3  std4     40
# 4  std5     50
# 5  std6     60
# 6  std7     70
print("------------")

print(df.tail()) # last 5 rows
#      name  marks
# 6    std7     70
# 7    std8     80
# 8    std9     90
# 9   std10    100
# 10  std11    110
print("------------")
print(df.tail(8)) # last 8 rows
#      name  marks
# 3    std4     40
# 4    std5     50
# 5    std6     60
# 6    std7     70
# 7    std8     80
# 8    std9     90
# 9   std10    100
# 10  std11    110
print("------------")

print(df.sample()) # one random row
#    name  marks
# 5  std6     60
print("------------")
print(df.sample(5)) # 5 random rows
#    name  marks
# 8  std9     90
# 2  std3     30
# 3  std4     40
# 7  std8     80
# 0  std1     10
print("------------")

print( df.sample(frac=0.5) ) # 50% of random data
#      name  marks
# 2    std3     30
# 7    std8     80
# 8    std9     90
# 0    std1     10
# 10  std11    110
# 1    std2     20
print("------------")

print(df.shape) # rows, cols
# (11, 2)
print("------------")
print(df.size) # no of elements
# 22
print("------------")
print(df.ndim) # 2
print("------------")
print(df.columns) # column names
# Index(['name', 'marks'], dtype='str')
print("------------")
print(df.index) # index range
# RangeIndex(start=0, stop=11, step=1)
print("------------")
print(df.dtypes) # datatypes of columns
# name       str
# marks    int64
# dtype: object
print("------------")

print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 11 entries, 0 to 10
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   name    11 non-null     str  
#  1   marks   11 non-null     int64
# dtypes: int64(1), str(1)
# memory usage: 308.0 bytes
# None
print("------------")


print(df.describe()) # first numberical cols (mathematical calculations)
#             marks
# count   11.000000
# mean    60.000000
# std     33.166248
# min     10.000000
# 25%     35.000000
# 50%     60.000000
# 75%     85.000000
# max    110.000000
print("------------")


print( df.describe(include="all") ) # include all numberical columns
#         name       marks
# count     11   11.000000
# unique    11         NaN
# top     std1         NaN
# freq       1         NaN
# mean     NaN   60.000000
# std      NaN   33.166248
# min      NaN   10.000000
# 25%      NaN   35.000000
# 50%      NaN   60.000000
# 75%      NaN   85.000000
# max      NaN  110.000000
print("------------")


print(df.iloc[0]) # row at "0" position
# name     std1
# marks      10
# Name: 0, dtype: object
print("------------")


print(df.loc[0]) # based on label (name or marks)
# name     std1
# marks      10
# Name: 0, dtype: object
print("------------")


df.index = [100,200,300,400,500,600,700,800,900,1000,1100]
print(df)
#        name  marks
# 100    std1     10
# 200    std2     20
# 300    std3     30
# 400    std4     40
# 500    std5     50
# 600    std6     60
# 700    std7     70
# 800    std8     80
# 900    std9     90
# 1000  std10    100
# 1100  std11    110
print("------------")

print(df.loc[500])
# name     std5
# marks      50
# Name: 500, dtype: object
print("------------")


print(df.iloc[5])
# name     std6
# marks      60
# Name: 600, dtype: object
print("------------")

data = {
    "name": ["std1", "std2", "std3", "std4", "std5", "std6", "std7", "std8", "std9", "std10", "std11"],
    "marks": [10,20,30,40,50,60,70,80,90,100,110]
}
df = pd.DataFrame(data)
print("---include test----")
print(df.loc[0:2]) # 0 and 2 will include
#    name  marks
# 0  std1     10
# 1  std2     20
# 2  std3     30
print("------------")


print(df.iloc[0:2]) # 0 will inclue and 2 will exclude
#      name  marks
# 100  std1     10
# 200  std2     20
print("------------")


print(df[ df['marks']> 50 ])
#      name  marks
# 5    std6     60
# 6    std7     70
# 7    std8     80
# 8    std9     90
# 9   std10    100
# 10  std11    110
print("------------")

print(df[df['marks']==50])
#    name  marks
# 4  std5     50
print("------------")

print( df[ (df["marks"]>50) & (df["marks"]<90) ] )
#    name  marks
# 5  std6     60
# 6  std7     70
# 7  std8     80
print("------------")


print(df.sort_values("marks"))
#      name  marks
# 0    std1     10
# 1    std2     20
# 2    std3     30
# 3    std4     40
# 4    std5     50
# 5    std6     60
# 6    std7     70
# 7    std8     80
# 8    std9     90
# 9   std10    100
# 10  std11    110
print("------------")
print(df.sort_values("marks",ascending=False))
#      name  marks
# 10  std11    110
# 9   std10    100
# 8    std9     90
# 7    std8     80
# 6    std7     70
# 5    std6     60
# 4    std5     50
# 3    std4     40
# 2    std3     30
# 1    std2     20
# 0    std1     10
print("------------")
print(df.sort_index())
#      name  marks
# 0    std1     10
# 1    std2     20
# 2    std3     30
# 3    std4     40
# 4    std5     50
# 5    std6     60
# 6    std7     70
# 7    std8     80
# 8    std9     90
# 9   std10    100
# 10  std11    110
print("------------")


df = pd.read_csv("employees_null.csv")
print(df)
#    name   age   salary
# 0  emp1  22.0  10000.0
# 1  emp2   NaN  20000.0
# 2  emp3  26.0      NaN
# 3  emp4   NaN      NaN
print("------------")
print(df["name"])
# 0    emp1
# 1    emp2
# 2    emp3
# 3    emp4
# Name: name, dtype: str
print("------------")
print(df[["name","age"]])
#    name   age
# 0  emp1  22.0
# 1  emp2   NaN
# 2  emp3  26.0
# 3  emp4   NaN
print("------------")

print(df.isnull())
#     name    age  salary
# 0  False  False   False
# 1  False   True   False
# 2  False  False    True
# 3  False   True    True
print("------------")

print(df.notnull())
#  name    age  salary
# 0  True   True    True
# 1  True  False    True
# 2  True   True   False
# 3  True  False   False
print("------------")


print(df.dropna()) # if any row contains null, then drop
#    name   age   salary
# 0  emp1  22.0  10000.0
print("------------")


print(df.dropna(axis=1)) # if any column contains not null, then print
#    name
# 0  emp1
# 1  emp2
# 2  emp3
# 3  emp4
print("------------")


print(df.fillna(0))
#    name   age   salary
# 0  emp1  22.0  10000.0
# 1  emp2   0.0  20000.0
# 2  emp3  26.0      0.0
# 3  emp4   0.0      0.0
print("------------")


print(df.fillna(10))
#    name   age   salary
# 0  emp1  22.0  10000.0
# 1  emp2  10.0  20000.0
# 2  emp3  26.0     10.0
# 3  emp4  10.0     10.0
print("------------")


print(df.ffill()) # fill forward: data will fill in forward direction
#    name   age   salary
# 0  emp1  22.0  10000.0
# 1  emp2  22.0  20000.0
# 2  emp3  26.0  20000.0
# 3  emp4  26.0  20000.0
print("------------")


print(df.bfill()) # fill backward: data will fill in forward direction
#    name   age   salary
# 0  emp1  22.0  10000.0
# 1  emp2  26.0  20000.0
# 2  emp3  26.0      NaN
# 3  emp4   NaN      NaN
print("------------")


print(df["age"].fillna(df["age"].mean()))
# 0    22.0
# 1    24.0
# 2    26.0
# 3    24.0
# Name: age, dtype: float64
print("------------")

