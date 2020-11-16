import nashpy as nash
import numpy as np
from scipy.optimize import linprog

np.set_printoptions(suppress=True)

#File content to array conversion
def fileConvert(fileName):
    dataArray = np.loadtxt(fileName)

    return dataArray

# Calculate saddle point in matrix a
def saddle_point(a) :

    min_vals = np.amin(a, axis=1)
    max_vals = np.amax(a, axis=0)
    maxmin = np.max(min_vals)
    minmax = np.min(max_vals)

    if maxmin != minmax :
        saddle_points = "No saddle point exists."
        return saddle_points
    else :
        
        saddle_points = "{"
        indices = np.argwhere(a == maxmin)
        for row in indices :
            saddle_points += "(" + str(row[0]+1) + "," +str(row[1]+1) + ")"
        
        saddle_points += "}"
        print("Saddle points are : ", saddle_points)
        return saddle_points

# Row and column reduce function
def reduceRowColDim(a):

    strategyCheck = []
    
    for i in range(len(a[0])):
        for j in range(len(a[0])):
            
            for k in range(len(a[0])-i):
                if a[i][j] > a[i+k][j]:
                    strategyCheck.append([i, i+k, a[i][j]])
                elif a[i][j] < a[i+k][j]:
                    strategyCheck.append([i+k, i, a[i][j]])
                elif a[i][j] == a[i+k][j]:
                    strategyCheck.append([i+k, i, 0])

    return a                

# Function to check whether row or column reduce is needed
def reduceRowColNeeded(a):
    
    rowcolReduce=0
    a_rows = np.sum(a, axis = 1)

    for i in range(len(a[0])-1):
        for j in range(len(a[0])):  
            for k in range(i, len(a[0])):
                if a[i][j] <= a[k][j] and a_rows[i] <= a_rows[k]:
                    rowcolReduce+=1
        rowcolReduce=0

    return rowcolReduce

#main function
def main():
    
    #Converting txt file to matrix
    A = fileConvert("dataArray.txt")
    #Matrix transposing for the B player
    B = A.transpose()
    print("\n-----------------------------------------------")

    #Initializing game for players
    rps2 = nash.Game(A, B)
    print("\n-----------------------------------------------")

    #Showing both players
    print(rps2)
    print("\n-----------------------------------------------")

    #Checking both players for saddle point 
    resultSaddlePointA = saddle_point(A)
    resultSaddlePointB = saddle_point(B)

    #If saddle points exist pure strategy is applied. If saddle points don't exist mixed strategy is applied
    if resultSaddlePointA == "No saddle point exists." and resultSaddlePointB == "No saddle point exists.":

        #Call for reduceRowColNeeded function: A matrix
        rowReduceNeed = reduceRowColNeeded(A)
        if rowReduceNeed > 0:
            #If row reduce is needed reduceRowColDim is to be called
            print("Rows reduce needed")
            A = reduceRowColDim(A)

        else:
            print("Rows reduce is not needed")

        #Call for reduceRowColNeeded function: B matrix
        colReduceNeed = reduceRowColNeeded(B)
        if rowReduceNeed > 0:
            #If column reduce is needed reduceRowColDim is to be called
            print("Columns reduce needed")
            B = reduceRowColDim(B)

        else:
            print("Columns reduce is not needed")


        # game_played = (list(rps2.support_enumeration()))

        # for game in game_played:
        #     print(game)

        # print("\n-----------------------------------------------")

        # for x1 ,x2  in game_played:
        #     row_util = np.dot(np.dot(x1, A), x2)
        #     col_util = np.dot(np.dot(x2, A), x1)
        #     print(row_util, col_util)

        #Model creation for mixed strategy solution
        

        # bnd0 = [(None, 0),
        #     (None, 0),
        #     (None, 0),
        #     (None, 0),
        #     (None, 0)
        #     ] 

        # bnd1 = [(0, None),
        #     (0, None),
        #     (0, None),
        #     (0, None),
        #     (0, None)]
        

        #Right side boundries
        B_b = np.array([1, 1, 1, 1, 1])
        #Target function
        C_c = B_b

        #Result for player A
        print("\n-----------------------------------------------")
        print("Player A: X probalities")
        print("\n")
        #Linear programming solving
        res = linprog(-C_c, A, B_b)
        print(res)

        #Result for player B
        print("\n-----------------------------------------------")
        print("Player B: X probalities")
        print("\n")
        #Linear programming solving
        res2 = linprog(C_c, -B, -B_b)
        print(res2)
        print("\n-----------------------------------------------")
    
    else:
        #Result print for solving
        print("Saddle point for the 1st player: ", resultSaddlePointA)
        print("\n-----------------------------------------------")
        print("Saddle point for the 2nd player: ", resultSaddlePointB)
        print("\n-----------------------------------------------")        

#Main function execution
if __name__ == "__main__":
    main()