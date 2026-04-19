import pandas as pd

df = pd.read_csv("orders.csv")
print(df)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK'],
}

df2 = pd.DataFrame(data)
print(df2)