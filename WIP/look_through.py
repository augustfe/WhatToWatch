import pandas as pd

df = pd.read_csv("serier.csv")

print(df["ID"])

a = 460627
b = 12

print(a in df.values)
print(b in df.values)

print(df.values)
