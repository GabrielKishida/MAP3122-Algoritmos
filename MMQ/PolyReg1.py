#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: February/2021

import numpy as np

#Description : Algorithm that applies linear regression for polynomials of first degree

def polynomialRegression1(x,y) :
    n = len(y)
    g = []
    g.append(np.ones(n))
    g.append(x)
    b = np.zeros(2)
    A = np.zeros((2,2))
    for i in range(2) :
        b[i] = np.matmul(g[i],y)
        for j in range(2) :
            A[i][j] = np.matmul(g[i],g[j])
    A = np.linalg.inv(A)
    b = np.matmul(A,b)
    return b

x = np.array([0,1,2,3])             # Insert here X points
y = np.array([1,2,4,8])             # Insert here Y points
print(polynomialRegression1(x,y))   # Prints result in a + bx