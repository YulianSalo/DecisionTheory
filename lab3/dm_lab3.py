#read dictionary from file
def readFromFileToDictionary(filename):
    dataDictionary= {}

    with open(filename) as f:
        dataDictionary = {int(pa[0]): pa[1:] for pa in map(str.split, f)}

    return dataDictionary

#Borda function
def BordaVote(dataDictionary):

    #empty arrays initialization for candidate votes counting    
    arrayA = []
    arrayB = []
    arrayC = []

    #iterating through each voting group
    for key in dataDictionary:

        #iterating through candidate prefenreces in each voting groups
        for j in range(len(dataDictionary[key])):
            
            #adding top scores for the most favoutiye candidate
            if j == 0:

                if dataDictionary[key][j] == 'a':
                    arrayA.append(key * 3)
                elif dataDictionary[key][j] == 'b':
                    arrayB.append(key * 3)
                elif dataDictionary[key][j] == 'c':
                    arrayC.append(key * 3)             
            #adding middle score for 2nd favoutite candidate
            elif j == 1:
                if dataDictionary[key][j] == 'a':
                    arrayA.append(key * 2)        
                elif dataDictionary[key][j] == 'b':
                    arrayB.append(key * 2)
                elif dataDictionary[key][j] == 'c':
                    arrayC.append(key * 2) 
            #adding the worst score for the least favoute candidate
            elif j == 2:
                if dataDictionary[key][j] == 'a':
                    arrayA.append(key)        
                elif dataDictionary[key][j] == 'b':
                    arrayB.append(key)
                elif dataDictionary[key][j] == 'c':
                    arrayC.append(key)     
    #votes summing
    numberA = sum(arrayA)
    numberB = sum(arrayB)
    numberC = sum(arrayC)

    #each candidate votes sum return 
    return numberA, numberB, numberC

#Condorset function
def CondorsetVote(dataDictionary):
    
    #initializing arrays for pair candidate comparison
    arrayA_B = []
    arrayA_C = []
    arrayB_A = []
    arrayB_C = []
    arrayC_A = []
    arrayC_B = []
    
    #iterating through each voting group
    for key in dataDictionary:

        #iterating through each voting group and making and a pair compariosons between candidates
        for j in range(len(dataDictionary[key])):

            if dataDictionary[key][0] == 'a' and dataDictionary[key][1] == 'b' and dataDictionary[key][2] == 'c':

                arrayA_B.append(key)
                arrayA_C.append(key)
                arrayB_C.append(key)

            elif dataDictionary[key][0] == 'a' and dataDictionary[key][1] == 'c' and dataDictionary[key][2] == 'b':
                arrayA_C.append(key)
                arrayA_B.append(key)
                arrayC_B.append(key)

            elif dataDictionary[key][0] == 'b' and dataDictionary[key][1] == 'a' and dataDictionary[key][2] == 'c':
                arrayB_A.append(key)
                arrayB_C.append(key)
                arrayA_C.append(key)

            elif dataDictionary[key][0] == 'b' and dataDictionary[key][1] == 'c' and dataDictionary[key][2] == 'a':
                arrayB_C.append(key)
                arrayB_A.append(key)
                arrayC_A.append(key)

            elif dataDictionary[key][0] == 'c' and dataDictionary[key][1] == 'a' and dataDictionary[key][2] == 'b':
                arrayC_A.append(key)
                arrayC_B.append(key)
                arrayA_B.append(key)

            elif dataDictionary[key][0] == 'c' and dataDictionary[key][1] == 'b' and dataDictionary[key][2] == 'a':
                arrayC_B.append(key)
                arrayC_A.append(key)
                arrayB_A.append(key)

    #summing comparison scores and printing them
    numberA_B = sum(arrayA_B)
    numberA_C = sum(arrayA_C)
    numberB_A = sum(arrayB_A)
    numberB_C = sum(arrayB_C)
    numberC_A = sum(arrayC_A)
    numberC_B = sum(arrayC_B)
    print (numberA_B, numberA_C, numberB_A, numberB_C, numberC_A, numberC_B)

    #initializing variable slots and additional info about top 3 comparison scores between candidates
    selected1 = 0
    selected1Info = ''
    selected2 = 0
    selected2Info = ''
    selected3 = 0
    selected3Info = ''

    #finding out top 3 comparison scores
    if numberA_B > numberB_A:
        selected1 = numberA_B
        selected1Info = "A>B"
    else:
        selected1 = numberB_A
        selected1Info = "B>A"

    if numberA_C > numberC_A:
        selected2 = numberA_C
        selected2Info = "A>C"
    else:
        selected2 = numberC_A
        selected2Info = "C>A"

    if numberB_C > numberC_B:
        selected3 = numberB_C
        selected3Info = "B>C"
    else:
        selected3= numberC_B
        selected3Info = "C>B"

    #returning top3 candidate comprarison scoresa nd additional info about them
    return selected1, selected1Info, selected2, selected2Info, selected3, selected3Info

#Main function
def main():

    #reading file to dictionary with the help of readFromFileToDictionary function
    dataDictionary = readFromFileToDictionary("dataArray.txt")
    print("Given votes by priority:", dataDictionary)

    #calling BordaVote function
    numberA, numberB, numberC = BordaVote(dataDictionary)

    #printing BordaVote scores
    print("\nBorda vote")
    print("Voted for A candidate", numberA)
    print("Voted for B candidate", numberB)
    print("Voted for C candidate", numberC)
    
    #calling CondorsetVote function
    selected1, selected1Info, selected2, selected2Info, selected3, selected3Info = CondorsetVote(dataDictionary)

    #printing CondorsetVote scores
    print("\nCondorset vote")
    print ("Top results:", selected1, selected1Info, selected2, selected2Info, selected3, selected3Info)

#Main function execution
if __name__ == "__main__":
    main()