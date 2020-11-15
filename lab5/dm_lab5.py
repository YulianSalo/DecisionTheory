import nashpy as nash
import numpy as np
import gambit
from scipy.optimize import linprog

np.set_printoptions(suppress=True)



## Calculate saddle point in matrix a
def saddle_point(a) :

    min_vals = np.amin(a, axis=1)
    max_vals = np.amax(a, axis=0)
    maxmin = np.max(min_vals)
    minmax = np.min(max_vals)

    if maxmin != minmax :
        return "No saddle point exists............."
    else :
        
        saddle_points = "{"
        indices = np.argwhere(a == maxmin)
        for row in indices :
            saddle_points += "(" + str(row[0]+1) + "," +str(row[1]+1) + ")"
        
        saddle_points += "}"
        print("Saddle points are : ", saddle_points)
        return saddle_points
        

def reduceRowDim(a):

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

def main():
    A = np.array([[6, 13, 8, 11, 5], [6, 10, 12, 5, 11], [8, 12, 7, 13, 6], [8, 7, 5, 11, 9], [6, 13, 7, 5, 8]])
    B = A.transpose()
    print("\n-----------------------------------------------")

    print(-B)
    rps2 = nash.Game(A, B)
    print("\n-----------------------------------------------")

    print(rps2)

    print("\n-----------------------------------------------")

    game_played = (list(rps2.support_enumeration()))

    for game in game_played:
        print(game)

    print("\n-----------------------------------------------")

    for x1 ,x2  in game_played:
        row_util = np.dot(np.dot(x1, A), x2)
        col_util = np.dot(np.dot(x2, A), x1)
        print(row_util, col_util)

    x1_bnds = (0, 0, 0, 0, 0)
    bnd = [(None, 0),
        (None, 0),
        (None, 0),
        (None, 0),
        (None, 0)
        ] 

    bnd1 = [(0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None)]
    B_b = np.array([1, 1, 1, 1, 1])
    C_c = B_b

    print("\n-----------------------------------------------")
    print("A")
    print("\n")
    res = linprog(-C_c, A, B_b)
    print(res)

    print("\n-----------------------------------------------")
    print("B")
    print("\n")
    res2 = linprog(C_c, -B, -B_b, bounds=bnd1)
    print(res2)
    print("\n-----------------------------------------------")

    print(saddle_point(A))

if __name__ == "__main__":
    main()