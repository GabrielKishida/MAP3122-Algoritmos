import numpy as np
from numpy import load
import matplotlib.pyplot as plt

dir = "EP1/EP1_dados/"

def seidel(a, x ,b): 
    #Finding length of a(3)        
    n = len(a)                    
    # for loop for 3 times as to calculate x, y , z 
    for j in range(0, n):         
        # temp variable d to store b[j] 
        d = b[j]                   
          
        # to calculate respective xi, yi, zi 
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i] 
        # updating the value of our solution         
        x[j] = d / a[j][j] 
    # returning our updated solution            
    return x 

def addDelta(a,delta) :
    n = len(a)
    transposed = a.transpose()
    if(n < len(transposed)) : n = len(transposed)
    return np.matmul(transposed,a) + delta*np.identity(n)

def buildMatrixA(n) :
    B = np.ones(n)
    C = np.identity(n)
    A1 = np.kron(B,C)
    A2 = np.kron(C,B)
    return np.array(np.concatenate((A1,A2),axis=0),dtype='float64')

def calculateDet(dir) :
    for i in range(1,4) :
        p1 = load(dir + "im" + str(i) + "/p1.npy")
        n = int(len(p1)/2)
        A = buildMatrixA(n)
        for j in range(-4,0,1) :
            if(j == -4) : delta = 0
            else : delta = pow(10,j)
            det = np.longdouble(np.linalg.det(addDelta(A,delta)))
            print("O determinante para a imagem " + str(i) + " com delta " + str(delta) + " é: " +str(det))

def solveImage(dir,imNumber) :
    p1 = load(dir + "im" + str(imNumber) + "/p1.npy")
    n = int(len(p1)/2)
    A = buildMatrixA(n)
    Atp = np.matmul(A.transpose(),p1)
    plotmap = np.zeros((n,n))
    for i in range(-3,0,1) :
        delta = pow(10,i)
        print(delta)
        A_Atdelta = addDelta(A,delta)
        f = np.ones(n*n)
        for k in range(0,1000) :
            f = seidel(A_Atdelta,f,Atp)
        for j in range (0,n) :
            for k in range (0,n) :
                plotmap[k][j] = f[n*j + k] 
        plt.imshow(plotmap)
        plt.show()
    return
solveImage(dir,1)