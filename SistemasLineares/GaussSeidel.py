#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: January/2021

#Description : Algorithm that applies the iterative method of Gauss Seidel

import numpy as np

def sassenfeld(A):
    n = len(A)
    M = A
    b = []
    sum1 = 0.
    for i in range(1,n):
        sum1 += abs(A[0][i])
    sum1 = sum2 = 0.
    b.append(sum1/abs(A[0][0]))
    for i in range(1,n):
        for j in range(i):
            sum1 += abs(M[i][j]*b[j])
        for j in range(i+1,n):
            sum2 += abs(M[i][j])
        b.append((sum1+sum2)/abs(M[i][i]))
        sum1 = sum2 = 0
    
    if (max(b) < 1):
        return True
    else:
        return False

def gaussSeidel(A,x,maxIter,Err) :
    if(sassenfeld(A)):
        print("Converge de acordo com Sassenfeld.")
    n = len(A)
    newx = x.copy()
    var = np.array([])
    for k in range (maxIter):
        for i in range(n):
            sum = 0.
            for j in range(n):
                if (i != j) :
                    sum -= A[i][j] * newx[j]
                else :
                    sum += A[i][n]
            newx[i] = sum/A[i][i]
        print(newx)
        
        for i in range(0,n) :
            if (newx[i] != 0):
                var = np.append(var,abs(newx[i] - x[i])/abs(x[i]))
            elif (x[i] != 0):
                var = np.append(var,1)
            elif (x[i] == 0):
                var = np.append(var,0)
        maxval = np.amax(var)
        print("Erro da interacao ", k, " : ",maxval)
        if (maxval <= Err):
            break
        else:
            x = newx.copy()
            var = np.array([])

#Example test to which the algorithm runs.
matrix = np.array([[5.,3.,15.],[-4.,10.,19.]])
print(matrix)
x = np.array((1.,1.))
gaussSeidel(matrix,x,100,0.001)