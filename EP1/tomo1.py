import numpy as np
from numpy import load
import matplotlib.pyplot as plt
import sys

dir = "EP1_dados/"

def seidel(a, x, b, maxIter, err):       
    n = len(a)
    newx = x.copy()                
    while(maxIter > 0) :
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
        maxIter -= 1  
    return newx 

def addDelta(a,delta) :
    transposed = a.transpose()
    At_A = np.matmul(transposed,a)
    return At_A + delta*np.identity(len(At_A))

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

def plotOriginal(dir,imageNum) :
    original = plt.imread(dir + imageNum + "/" + imageNum + ".png")
    n = len(original)
    plt.subplot(1,4,1)
    plt.imshow(original)
    plt.title("Gráfico original",fontsize=7)
    f = np.zeros(n*n)
    for j in range(n):
        for i in range(n):
            f[n*j + i] = original[i][j]
    return f


def solveImage(dir,imageNum) :
    fOriginal = plotOriginal(dir,imageNum)
    p1 = load(dir + imageNum + "/p1.npy")
    n = int(len(p1)/2)
    A = buildMatrixA(n)
    Atp = np.matmul(A.transpose(),p1)
    plotmap = np.zeros((n,n))
    for i in range(-3,0,1) :
        delta = pow(10,i)
        A_Atdelta = addDelta(A,delta)
        f = np.ones(n*n)
        f = seidel(A_Atdelta,f,Atp,100,0.001)
        for j in range (0,n) :
            for k in range (0,n) :
                plotmap[k][j] = f[n*j + k] 
        fErr = fOriginal - f
        err = 100*(np.sqrt(np.matmul(fErr,fErr))/np.sqrt(np.matmul(fOriginal,fOriginal)))
        print("Erro para delta de " + str(delta) + " : " + str(err) )
        plt.subplot(1,4,i+5)
        plt.imshow(plotmap)
        plt.title("Gráfico com delta " + str(delta),fontsize=7)
    plt.show()
    return

imageNum = str(sys.argv[1])
solveImage(dir,imageNum)