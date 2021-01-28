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

A = np.array([[4., 12., -16.],[12., 37., -43.],[-16., -43., 98.]])
print(A)
print(choleskyDecomposition(A))