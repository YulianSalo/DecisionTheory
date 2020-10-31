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

def CondorsetVote(dataDictionary):
    
    arrayA_B = []
    arrayA_C = []
    arrayB_A = []
    arrayB_C = []
    arrayC_A = []
    arrayC_B = []
    for key in dataDictionary:

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

    numberA_B = sum(arrayA_B)
    numberA_C = sum(arrayA_C)
    numberB_A = sum(arrayB_A)
    numberB_C = sum(arrayB_C)
    numberC_A = sum(arrayC_A)
    numberC_B = sum(arrayC_B)

    selected1 = 0
    selected1Info = ''
    selected2 = 0
    selected2Info = ''
    selected3 = 0
    selected3Info = ''

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

    return selected1, selected1Info, selected2, selected2Info, selected3, selected3Info

arrayA, arrayB, arrayC, numberA, numberB, numberC = BordaVote(dataDictionary)

print (arrayA, arrayB, arrayC, numberA, numberB, numberC)

selected1, selected1Info, selected2, selected2Info, selected3, selected3Info = CondorsetVote(dataDictionary)

print ("Top results:", selected1, selected1Info, selected2, selected2Info, selected3, selected3Info)