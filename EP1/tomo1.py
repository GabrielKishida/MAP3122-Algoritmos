import numpy as np
from numpy import load
import matplotlib.pyplot as plt

dir = "EP1/EP1_dados/"

def seidel(a, x, b, maxIter, err):       
    n = len(a)
    newx = x.copy()                 
    for k in range(0,maxIter) :
        var = np.array([])
        for i in range(0, n):         
            # temp variable d to store b[j] 
            d = b[i]                   
            for j in range(0, n):      
                if(i != j): 
                    d-=a[i][j] * newx[j] 
            # updating the value of our solution         
            newx[i] = d / a[i][i] 
        # returning our updated solution  
        for i in range (n) :
            if (newx[i] != 0) :
                var = np.append(var,abs((newx[i]-x[i])/newx[i]))
            elif (x[i] != 0) :
                var = np.append(var,1)  
            elif (x[i] == 0) :
                var = np.append(var,0)
        maxval = np.amax(var)
        if(maxval < err) :
            break
        x = newx.copy()    
    return newx 

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
        f = seidel(A_Atdelta,f,Atp,100,0.001)
        for j in range (0,n) :
            for k in range (0,n) :
                plotmap[k][j] = f[n*j + k] 
        plt.subplot(1,3,i+4)
        plt.imshow(plotmap)
        plt.title("Gráfico com delta " + str(delta),fontsize=10)
    plt.show()
    return

solveImage(dir,3)