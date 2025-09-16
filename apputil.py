#import seaborn as sns
import pandas as pd


# update/add code below ...

# Exercise 1
def fib(n):
    # if statement intitially, then add recursive function
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive function
        return fib(n-1) + fib(n-2)


# Test cases
print(fib(9))
print(fib(22))


# Exercise 2
def to_binary(n):
    # Initial if statement
    if n < 2:
        return str(n)
    else:
        # Recursive function
        return to_binary(n // 2) + str(n % 2)


# Test cases
print(to_binary(2))
print(bin(2))
print(to_binary(12))
print(bin(12))  


# Exercise 3
# import pandas as pd
# Access data
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

# Task 1:
def task_1():
    df = df_bellevue.copy()

    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()
        df["gender"] = df["gender"].replace({
            "m": "male",
            "f": "female",
            "": None,
            "nan": None
        })
        # Sort columns
    missing_counts = df.isna().sum().sort_values()
    sorted_columns = list(missing_counts.index)
    return sorted_columns

print(task_1())


# Task 2:
def task_2():
    df = df_bellevue.copy()
    # Making data frame
    df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
    df["year"] = df["date_in"].dt.year
    admissions = (
        #  Labeling data frame
        df.groupby("year")
          .size()
          .reset_index(name="total_admissions")
    )
    return admissions

print(task_2())

# Task 3:
def task_3():
    df = df_bellevue.copy()
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()
        df["gender"] = df["gender"].replace({
            "m": "male",
            "f": "female",
            "": None,
            "nan": None
        })
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    # simplify metadata attached to result
    result = df.groupby("gender")["age"].mean()
    result.name = None
    return result

print(task_3())

# Task 4:
def task_4():
    df = df_bellevue.copy()
    if "profession" not in df.columns:
        return []
    # Find top 5 professions
    top5 = df["profession"].value_counts().head(5).index.tolist()
    
    return top5

print(task_4())