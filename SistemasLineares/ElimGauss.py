#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: January/2021

#Description : Algorithm that applies the method of Gaussian Elimination to linear systems.

#Functionality: adds two vectors, each element one by one and returns the sum.
def vectorsum(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

#Functionality: multiplies a vector by a constant "mult", and returns the new vector.
def vectormult(mult,vector):
    c = []
    for i in range(len(vector)):
        c.append(vector[i]*mult)
    return c

#Functionality: divides a vector by a constant "div", and returns the new vector.
def vectordiv(div,vector):
    c = []
    for i in range(len(vector)):
        c.append(vector[i]/div)
    return c

#Functionality: this function switches line1 and line2 in a matrix.
def switchlines(matrix,line1,line2):
    auxvector = matrix[line1]
    matrix[line1] = matrix[line2]
    matrix[line2] = auxvector

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
                    switchlines(matrix,i,k)
                    allZeroes = False
                    break
            if (allZeroes): return "System not solvable"
         #Firstly, this method "eliminates" the values in the lower triangle of the matrix.
        for j in range(i+1,n):
            if (matrix[i][i] == 0 ): return "System not solvable"
            coef = -(matrix[j][i]/matrix[i][i])
            auxvector = vectormult(coef,matrix[i])
            matrix[j] = vectorsum(matrix[j],auxvector)
            print(matrix)
    if (matrix[n-1][n-1] == 0): return "System not solvable"
    matrix[n-1] = vectordiv(matrix[n-1][n-1],matrix[n-1])
    #Then, this method works bottom-up, eliminating the values in the upper triangle of the matrix.
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            coef = -(matrix[j][i]/matrix[i][i])
            auxvector = vectormult(coef,matrix[i])
            matrix[j] = vectorsum(matrix[j],auxvector)
    #Finally, this method must divide each row by its element on the main diagonal, constructing the
    #identity matrix.
    for i in range(n):
        matrix[i] = vectordiv(matrix[i][i],matrix[i])
    return matrix

#Example test to which the algorithm runs.
matrix = [[1,1,2,0,1],[2,-1,0,1,-2],[1,-1,-1,-2,4],[2,-1,2,-1,0]]
print(elimgauss(matrix))
print("Expected values: x1 = 1, x2 = 2, x3 = -1, x4 = -2")
