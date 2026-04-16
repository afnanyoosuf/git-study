import pandas as pd

df = pd.read_csv("data/iris_dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())