#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: February/2021

import numpy as np

#Description : Algorithm that applies linear regression for polynomials of any degree

def polynomialRegressionK (x,y,k) :
    g = []
    b = np.zeros(k)
    for i in range(k) :
        g.append(np.power(x,i))
    A = np.zeros([k,k])
    for i in range(k) :
        b[i] = np.matmul(g[i],y)
        for j in range(k):
            A[i][j] = np.matmul(g[i],g[j])
    A = np.linalg.inv(A)
    b = np.matmul(A,b)
    return b

y = np.array([1,2,4,8])  #Insert here Y points
x = np.array([0,1,2,3]) # Insert here X points
print(polynomialRegressionK(x,y,2)) #Prints a + bx + cx² + ... + nx^k-1