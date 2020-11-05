import pandas as pd

df = pd.read_csv("data.csv")

coeff = [0.25, 0.2, 0.22, 0.18, 0.15]

for i in range(len(df)):
    df.iloc[:,i+1] *= coeff[i]

df["sum"] = df.sum(axis=1)

print (df)