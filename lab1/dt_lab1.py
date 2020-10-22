import numpy as np
import os

def minRowValueFunction(dataArray):
    
    minRowArray = dataArray.min(axis=1)
    return minRowArray

def maxRowValueFunction(dataArray):
    
    maxRowArray = dataArray.max(axis=1)
    return maxRowArray

def HurwitzFunction(dataArray, coefficient):
    
    minRowArray = minRowValueFunction(dataArray)
    maxRowArray = maxRowValueFunction(dataArray)
    HurwitzRowArray = np.zeros(len(minRowArray))

    for i in range(len(minRowArray)):
        HurwitzRowArray[i] = (minRowArray[i] * (1 - coefficient)) + (maxRowArray[i] * coefficient)

    return HurwitzRowArray

def BayesLaplaceFunction(dataArray, coefficient_array):
    RowArray = np.zeros(( len(dataArray), len(dataArray)))

    for i in range(len(dataArray[0])):
        for j in range(len(dataArray[0])):
            RowArray[i][j] = dataArray[i][j] * coefficient_array[i]

    BayesLaplaceRowArray = maxRowValueFunction(RowArray)

    return BayesLaplaceRowArray

def fileConvert(fileName):
    dataArray = np.loadtxt(fileName)
    return dataArray


def main():

    fileName = input("Welcome! Please, enter the file name from the listed below: \n {0} \n: ".format([f for f in os.listdir('.') if os.path.isfile(f)] ) )
    dataArray = fileConvert(fileName)

    while len(dataArray) == 0:
        fileName = input("Please, enter the file name: ")
        dataArray = fileConvert

    print(dataArray)
    
    coefficient = float(input("Please enter the coefficient in range from 0 to 1: "))

    while coefficient == None or coefficient <= 0 or coefficient >= 1:
        coefficient = float(input("Please enter the coefficient in range from 0 to 1: "))

    customProbabilities = np.zeros(len(dataArray[0]))
    for i in range (len(dataArray[0]) ):
        value = float(input("Input custom predefined probabilities values #{0} in range from 0 to 1: ".format( i+1 ) ) )
        customProbabilities[i] = value

    print("Executing the following decision making methods: ")

    print("1. Walde criterion")
    minRowArray = minRowValueFunction(dataArray)
    print("Selected decision: ", minRowArray)

    print("2. Bayes criterion")
    maxRowArray = maxRowValueFunction(dataArray)
    print("Selected decision: ", maxRowArray)

    print("3. Hurwitz criterion")
    HurwitzRowArray = maxRowValueFunction(dataArray)
    print("Selected decision: ", HurwitzRowArray)

    print("4. Bayes Laplace criterion. Using custom probablities")
    BayesLaplaceRowArray = BayesLaplaceFunction(dataArray, customProbabilities)
    print("Selected decision: ", BayesLaplaceRowArray)
    
if __name__ == "__main__":
    main()
