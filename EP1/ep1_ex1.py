import numpy as np
from numpy import load
import matplotlib.pyplot as plt

dir = "/home/gabriel/MAP3122/MAP3122-Algoritmos/EP1/EP1_dados/"

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
        n = len(p1)
        A = buildMatrixA(n)
        for j in range(-4,0,1) :
            if(j == -4) : delta = 0
            else : delta = pow(10,j)
            det = np.longdouble(np.linalg.det(addDelta(A,delta)))
            print("O determinante para a imagem " + str(i) + " com delta " + str(delta) + " é: " +str(det))

calculateDet(dir)