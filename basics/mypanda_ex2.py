import pandas as pd

df = pd.read_csv("emps.csv")
# read single col
print(df["name"])
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David
# 4        Eva
# Name: name, dtype: str
print("----------")

# read multiple cols
print(df[["name", "age"]])
#       name  age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35
# 3    David   28
# 4      Eva   32
print("----------")

# read cell value
print(df.loc[0, "name"])
# Alice
print("----------")

# add new col
df["bonus"]  = df["salary"] * 0.10
print(df)
#    id     name  age department  salary   bonus
# 0   1    Alice   25         IT   50000  5000.0
# 1   2      Bob   30         HR   40000  4000.0
# 2   3  Charlie   35         IT   60000  6000.0
# 3   4    David   28    Finance   45000  4500.0
# 4   5      Eva   32         HR   42000  4200.0
print("----------")

# delete col
df.drop("bonus", axis=1, inplace=True)
print(df)
#    id     name  age department  salary
# 0   1    Alice   25         IT   50000
# 1   2      Bob   30         HR   40000
# 2   3  Charlie   35         IT   60000
# 3   4    David   28    Finance   45000
# 4   5      Eva   32         HR   42000
print("----------")


df1 = pd.read_csv("emps.csv")
df2 = pd.read_csv("department.csv")

merged_df = pd.merge(df1, df2)
print(merged_df) # inner join based on common column - Department
#    id     name  age department  salary   location
# 0   1    Alice   25         IT   50000  Hyderabad
# 1   2      Bob   30         HR   40000  Bangalore
# 2   3  Charlie   35         IT   60000  Hyderabad
# 3   4    David   28    Finance   45000    Chennai
# 4   5      Eva   32         HR   42000  Bangalore
print("----------")

print(merged_df.sort_values(by="salary")) # ascending
#    id     name  age department  salary   location
# 1   2      Bob   30         HR   40000  Bangalore
# 4   5      Eva   32         HR   42000  Bangalore
# 3   4    David   28    Finance   45000    Chennai
# 0   1    Alice   25         IT   50000  Hyderabad
# 2   3  Charlie   35         IT   60000  Hyderabad
print("----------")

print( merged_df.sort_values(by="salary", ascending=False) ) # descending
#    id     name  age department  salary   location
# 2   3  Charlie   35         IT   60000  Hyderabad
# 0   1    Alice   25         IT   50000  Hyderabad
# 3   4    David   28    Finance   45000    Chennai
# 4   5      Eva   32         HR   42000  Bangalore
# 1   2      Bob   30         HR   40000  Bangalore
print("----------")

print( merged_df.groupby("department")["salary"].mean() )
# department
# Finance    45000.0
# HR         41000.0
# IT         55000.0
# Name: salary, dtype: float64
print("----------")
print( merged_df.groupby("department")["salary"].max() )
# department
# Finance    45000
# HR         42000
# IT         60000
# Name: salary, dtype: int64
print("----------")
print( merged_df.groupby("department")["salary"].min() )
# department
# Finance    45000
# HR         40000
# IT         50000
# Name: salary, dtype: int64
print("----------")
print( merged_df.groupby("department")["salary"].sum() )
# department
# Finance     45000
# HR          82000
# IT         110000
# Name: salary, dtype: int64
print("----------")


print(merged_df[ merged_df["salary"]>45000 ])
#    id     name  age department  salary   location
# 0   1    Alice   25         IT   50000  Hyderabad
# 2   3  Charlie   35         IT   60000  Hyderabad
print("----------")


df = pd.read_csv("students.csv")
print(df)
#    id     name  marks       city
# 0   1    Alice   85.0  Hyderabad
# 1   2      Bob    NaN  Bangalore
# 2   3  Charlie   90.0        NaN
# 3   4    David    NaN    Chennai
# 4   5      Eva   88.0  Hyderabad
print("----------")

# check missing values
print(df.isnull())
#       id   name  marks   city
# 0  False  False  False  False
# 1  False  False   True  False
# 2  False  False  False   True
# 3  False  False   True  False
# 4  False  False  False  False
print("----------")

# count of missing values column wise
print(df.isnull().sum())
# id       0
# name     0
# marks    2
# city     1
# dtype: int64
print("----------")


# any row contain null, that row will be deleted
# df.dropna(inplace=True)
# print(df)
#    id   name  marks       city
# 0   1  Alice   85.0  Hyderabad
# 4   5    Eva   88.0  Hyderabad
print("----------")

# df["marks"] = df["marks"].fillna(0,inplace=True)
# print(df)
#   df["marks"] = df["marks"].fillna(0,inplace=True)
#    id     name  marks       city
# 0   1    Alice   85.0  Hyderabad
# 1   2      Bob    0.0  Bangalore
# 2   3  Charlie   90.0        NaN
# 3   4    David    0.0    Chennai
# 4   5      Eva   88.0  Hyderabad
print("----fillna------")

# df["marks"] = df["marks"].ffill()
# print(df)
#    id     name  marks       city
# 0   1    Alice   85.0  Hyderabad
# 1   2      Bob   85.0  Bangalore
# 2   3  Charlie   90.0        NaN
# 3   4    David   90.0    Chennai
# 4   5      Eva   88.0  Hyderabad
print("----ffill------")


# df["marks"] = df["marks"].bfill()
# print(df)
#    id     name  marks       city
# 0   1    Alice   85.0  Hyderabad
# 1   2      Bob   90.0  Bangalore
# 2   3  Charlie   90.0        NaN
# 3   4    David   88.0    Chennai
# 4   5      Eva   88.0  Hyderabad
print("----bfill------")

print( df.replace("Hyderabad", "HYD", inplace=True) )
#    id     name  marks       city
# 0   1    Alice   85.0        HYD
# 1   2      Bob    NaN  Bangalore
# 2   3  Charlie   90.0        NaN
# 3   4    David    NaN    Chennai
# 4   5      Eva   88.0        HYD
print("----replace------")



