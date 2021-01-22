#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: January/2021

#Description : Algorithm that applies the method of LU decomposition to solve linear systems.

import numpy as np

#Functionality: this function calculates the sum of a multiplication, a value useful to the decomposition.
#l is the upper triangle matrix, u the lower, and i,j the line and row indexes.
def sumMultiplication(l,u,i,j) :
    result = 0
    for k in range(j) :
        result += l[i][k]*u[k][j]
    return result

#Functionality: this function subtracts a linear proportion (equal to coef) of a maintaned line
#from an eliminated line, making one element (matrix[lineEliminated][lineMaintaned]) equal to 0.
def lineElimination(matrix,lineMaintained,lineEliminated):
    if (matrix[lineMaintained][lineMaintained] != 0):
        coef = -(matrix[lineEliminated][lineMaintained]/matrix[lineMaintained][lineMaintained])
        matrix[lineEliminated] = matrix[lineEliminated] + matrix[lineMaintained]*coef

#Functionality: receives decomposition lu and answers b to the linear system, and solves it.
#Still under development
def luSolver(l,u,b,n) :
    lb = np.zeros((n,n+1))
    for i in range(n) :
        lb[i] = np.hstack((l[i],b[i]))
    #for i in range(n):
        #for j in range(i+1,n):
            #lineElimination(lb,i,j)

#Functionality: this function receives a matrix (n)x(n+1) and solves it using LU decomposition.
def luDecomposition(matrix) :
    n = len(matrix)
    u = np.zeros((n,n))
    l = np.zeros((n,n))
    for j in range(n) :
        u[0][j] = matrix[0][j]
    for i in range(n) :
        l[i][0] = matrix[i][0]/u[0][0]
    for i in range(1,n) :
        for j in range(i+1) :
            if (i == j) :
                l[i][i] = 1
            else :
                l[i][j] = (matrix[i][j] - sumMultiplication(l,u,i,j))/u[j][j]
        for j in range(i,n) :
            u[i][j] = matrix[i][j] - sumMultiplication(l,u,i,j)
    b = np.zeros(n)
    for i in range(n):
        b[i] = matrix[i][n]
    print(l)
    print(u)

matrix = np.array([[1.,1.,0.,3.,4.],[2.0,1.,-1.,1.,1.],[3.,-1.,-1.,2.,-3.],[-1.,2.,3.,-1., 4.]])
luDecomposition(matrix)

