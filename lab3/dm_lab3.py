dataDictionary= {}

with open('dataArray.txt') as f:
    dataDictionary = {int(pa[0]): pa[1:] for pa in map(str.split, f)}

print(dataDictionary)

def BordaVote(dataDictionary):
    
    arrayA = []
    arrayB = []
    arrayC = []

    for key in dataDictionary:

        for j in range(len(dataDictionary[key])):
            
            if j == 0:

                if dataDictionary[key][j] == 'a':
                    arrayA.append(key * 3)
                elif dataDictionary[key][j] == 'b':
                    arrayB.append(key * 3)
                elif dataDictionary[key][j] == 'c':
                    arrayC.append(key * 3)             

            elif j == 1:
                if dataDictionary[key][j] == 'a':
                    arrayA.append(key * 2)        
                elif dataDictionary[key][j] == 'b':
                    arrayB.append(key * 2)
                elif dataDictionary[key][j] == 'c':
                    arrayC.append(key * 2) 

            elif j == 2:
                if dataDictionary[key][j] == 'a':
                    arrayA.append(key)        
                elif dataDictionary[key][j] == 'b':
                    arrayB.append(key)
                elif dataDictionary[key][j] == 'c':
                    arrayC.append(key)     

    numberA = sum(arrayA)
    numberB = sum(arrayB)
    numberC = sum(arrayC)

    return arrayA, arrayB, arrayC, numberA, numberB, numberC

def ConcordeVote(dataDictionary):
    
    arrayA = []
    arrayB = []
    arrayC = []
    numberA = sum(arrayA)
    numberB = sum(arrayB)
    numberC = sum(arrayC)

    return arrayA, arrayB, arrayC, numberA, numberB, numberC

arrayA, arrayB, arrayC, numberA, numberB, numberC = BordaVote(dataDictionary)

print (arrayA, arrayB, arrayC, numberA, numberB, numberC )