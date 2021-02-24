#Developer: Gabriel Yugo Nascimento Kishida
#Contact: gabriel.kishida@usp.br
#Date: February/2021

import numpy as np

#Description : Algorithm that applies linear regression for polynomials of second degree

def polynomialRegression2 (x,y) :
    n = len(y)
    g = []
    g.append(np.ones(n))
    g.append(x)
    g.append(np.ones(n))
    b = np.zeros(3)
    for i in range(n) :
        g[2][i] = g[1][i]*g[1][i]
    A = np.zeros([3,3])
    for i in range(3) :
        b[i] = np.matmul(g[i],y)
        for j in range(3):
            A[i][j] = np.matmul(g[i],g[j])
    A = np.linalg.inv(A)
    b = np.matmul(A,b)
    return b

y = np.array([192.,180.,150.,115.,72.]) #Insert here Y points
x = np.array([1.,2.,3.,4.,5.]) # Insert here X points
print(polynomialRegression2(x,y)) #Prints a + bx + cx² fitting