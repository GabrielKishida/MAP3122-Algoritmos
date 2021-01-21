#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: January/2021

#Description : Algorithm that applies the method of Gaussian Elimination to linear systems.
#This version utilizes the numpy library to make things easier (and faster).

import numpy as np

#Functionality: this function switches line1 and line2 in a matrix.
def switchLines(matrix,line1,line2):
    auxvector = matrix[line1]
    matrix[line1] = matrix[line2]
    matrix[line2] = auxvector

#Functionality: this function subtracts a linear proportion (equal to coef) of a maintaned line
#from an eliminated line, making one element (matrix[lineEliminated][lineMaintaned]) equal to 0.
def lineElimination(matrix,lineMaintained,lineEliminated):
    coef = -(matrix[lineEliminated][lineMaintained]/matrix[lineMaintained][lineMaintained])
    matrix[lineEliminated] = matrix[lineEliminated] + matrix[lineMaintained]*coef

#Functionality: applies the gaussian elimination method, returning the solved matrix.
#Input: the input must be a matrix[n][n+1], where n is any integer > 0.
#Output: this function returns the identity matrix, with the n+1 row being the values of each variable.
def elimgauss(matrix):
    n = len(matrix)
    for i in range(n):
        #Before we start the method, we need to switch lines if matrix[i][i] = 0.
        if(matrix[i][i] == 0):
            allZeroes = True
            for k in range(i+1,n):
                if(matrix[i][k] != 0):
                    switchLines(matrix,i,k)
                    print("switchline")
                    print(matrix)
                    allZeroes = False
                    break
            if (allZeroes): return "System not solvable"
        #Firstly, this method "eliminates" the values in the lower triangle of the matrix.
        for j in range(i+1,n):
            lineElimination(matrix,i,j)
    if (matrix[n-1][n-1] == 0): return "System not solvable"
    matrix[n-1] = matrix[n-1]/matrix[n-1][n-1]
    #Then, this method works bottom-up, eliminating the values in the upper triangle of the matrix.
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            lineElimination(matrix,i,j)
    #Finally, this method must divide each row by its element on the main diagonal, constructing the
    #identity matrix.
    for i in range(n):
        matrix[i] = matrix[i]/matrix[i][i]
    return matrix

#Example test to which the algorithm runs.
matrix = np.array([[1.0,1.0,2.0,0.0,1.0],[2.0,-1.0,0.0,1.0,-2.0],[1.0,-1.0,-1.0,-2.0,4.0],[2.0,-1.0,2.0,-1.0, 0.0]])
print(elimgauss(matrix))
print("Expected values: x1 = 1, x2 = 2, x3 = -1, x4 = -2")
