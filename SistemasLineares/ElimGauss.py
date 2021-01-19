#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: January/2021

#Description : Algorithm that applies the method of Gaussian Elimination to linear systems.

#functionality: adds two vectors, each element one by one and returns the sum.
def vectorsum(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

#functionality: multiplies a vector by a constant "mult", and returns the new vector.
def vectormult(mult,vector):
    c = []
    for i in range(len(vector)):
        c.append(vector[i]*mult)
    return c

#functionality: divides a vector by a constant "div", and returns the new vector.
def vectordiv(div,vector):
    c = []
    for i in range(len(vector)):
        c.append(vector[i]/div)
    return c

#functionality: applies the gaussian elimination method, returning the solved matrix.
#input: the input must be a matrix[n][n+1], where n is any integer > 0.
#output: this function returns the identity matrix, with the n+1 row being the values of each variable.
def elimgauss(matrix):
    n = len(matrix)
    #Firstly, this method "eliminates" the values in the lower triangle of the matrix.
    for i in range(n):
        for j in range(i+1,n):
            coef = -(matrix[j][i]/matrix[i][i])
            auxvector = vectormult(coef,matrix[i])
            matrix[j] = vectorsum(matrix[j],auxvector)
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
matrix = [[1,-1,2,2],[2,1,-1,1],[-2,-5,3,3]]
print(elimgauss(matrix))