import numpy as np

np.set_printoptions(suppress=True)

#File content to array conversion
def fileConvert(fileName):
    dataArray = np.loadtxt(fileName)

    return dataArray
#Each solution income calculation and selection of the best one
def incomeSolutionFunction (solutionArray):
    
    incomeArray = np.zeros(len(solutionArray[0]))

    for i in range(len(incomeArray)):

        if i == 0 or i == 1:
            incomeArray[i] = 5 * solutionArray[i][0] * ( solutionArray[i][2] * solutionArray[i][3] - solutionArray[i][4] * solutionArray[i][5] ) - solutionArray[i][1]
        else:
            incomeArray[i] = 4 * solutionArray[i][0] * ( solutionArray[i][2] * solutionArray[i][3] - solutionArray[i][4] * solutionArray[i][5] ) - solutionArray[i][1]

    selectedSolution = np.max(incomeArray)
    return incomeArray, selectedSolution

#Main function
def main():

    #Textfile read
    dataArray = fileConvert("dataArray.txt")
    
    generalInfo = "Build now/ Not to build now (1/0); Cost; Success probability; Yearly income; Failure probality; Yearly loss"
    print(generalInfo)
    
    #Empty list for the annotations
    solutionInfo = []

    #Each array line reading and annotation adding
    for i in range(len(dataArray[0])):
        if i == 0:
            solutionInfo.append("Large factory, build now")
            print(dataArray[i])
        elif i == 1:
            solutionInfo.append("Small factory, build now")
            print(dataArray[i])
        elif i == 2:
            solutionInfo.append("Large factory, build next year")
            print(dataArray[i])
        elif i == 3:
            solutionInfo.append("Small factory, build next year")
            print(dataArray[i])
        else:
            solutionInfo.append("Cancel constructiom")
            print(dataArray[i])

    #Target function execution       
    incomeArray, selectedSolution = incomeSolutionFunction(dataArray)

    #Solution print
    print ("All soutions: ", incomeArray)
    for i in range(len(incomeArray)):
        if selectedSolution  == incomeArray[i]:
            print("The best option: ", selectedSolution, solutionInfo[i],)

#Main function execution
if __name__ == "__main__":
    main()
