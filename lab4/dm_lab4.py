import pandas as pd

def main():
    #CSV file reading
    df = pd.read_csv("data.csv")

    #Coeffient definiton
    coeff = [0.25, 0.2, 0.22, 0.18, 0.15]

    #Solution calculation
    for i in range(len(df)):
        df.iloc[:,i+1] *= coeff[i]

    #Summing final value for each row
    df["sum"] = df.sum(axis=1)

    #Result print
    print (df)

if __name__ == "__main__":
    main()