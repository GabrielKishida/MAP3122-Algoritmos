#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: January/2021

#Description : Algorithm that applies the Cholesky Decomposition.

import numpy as np
import math

def choleskySum(L,i,j):
    sum = 0
    for k in range(j):
        sum += L[i][k]*L[j][k]
    return sum

def choleskySquareSum(L,i):
    sum = 0
    for k in range(i):
        sum += L[i][k] * L[i][k]
    return sum

def choleskyDecomposition(A) :
    n = len(A)
    L = np.zeros((n,n))
    L[0][0] = math.sqrt(A[0][0])
    for i in range(1,n):
        for j in range (i):
            L[i][j] = (A[i][j] - choleskySum(L,i,j))/L[j][j]
        L[i][i] = math.sqrt(A[i][i] - choleskySquareSum(L,i))
    return L

A = np.array([[4., -2., -6.],[-2., 10., 9.],[-6., 9., 14.]])
print(A)
print(choleskyDecomposition(A))