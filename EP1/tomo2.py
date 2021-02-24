####################################################
# MAP 3122 - Quadrimestral 1 - Exercício Programa 1
# Algoritmo para a tomografia 2
# Desenvolvido por: Gabriel Yugo Nascimento Kishida
# NUSP : 1125764 - Contato : gabriel.kishida@usp.br
#               Fevereiro de 2021
####################################################

### Importacoes ###
import numpy as np
from numpy import load
import matplotlib.pyplot as plt
import sys

### Valores constantes ###
# Este valor indica em que diretório se encontram os dados utilizados pelo programa
dir = "EP1_dados/"

### Funcoes do algoritmo ###
# Nome: gaussSeidel
# Parametros: matriz - a, solucao - x, resposta - b, maxIter - iteracoes maximas, err - Erro maximo
# Funcao: Aplica o algoritmo de Gauss Seidel ao sistema ax = b. Itera no maximo maxIter vezes e
# para execucao quando o erro for menor do que err.
def gaussSeidel(a, x, b, maxIter, err):       
    n = len(a)                              # n Tamanho do vetor solucao
    newx = x.copy()                         # Resposta da iteracao atual newx                  
    while(maxIter > 0) :                    # Itera um máximo de maxIter vezes
        var = np.array([])                  # Limpa o vetor de erro var
        for i in range(0, n):               # Esses dois 'for's concatenados aplicam o algoritmo        
            d = b[i]                   
            for j in range(0, n):      
                if(i != j): 
                    d-=a[i][j] * newx[j]    # Subtrai o somatório  
            newx[i] = d / a[i][i]           # Atualiza o vetor da nova solucao newx 
        # Este próximo 'for' cria o vetor var de erro para a iteracao atual
        for i in range (n) :
            if (newx[i] != 0) :
                var = np.append(var,abs((newx[i]-x[i])/newx[i]))
            elif (x[i] != 0) :
                var = np.append(var,1)  
            elif (x[i] == 0) :
                var = np.append(var,0)
        maxval = np.amax(var)               # O valor de erro escolhido é o maior valor de var
        if(maxval < err) :                  # Se o maior erro for menor que err, encerra a execucao
            break
        x = newx.copy()                     # Caso contrario, reinicia-se o ciclo
        maxIter -= 1    
    return newx                             # Ao final da execucao, retorna o novo vetor solucao

# Nome: addDelta
# Parametros: matriz - a, parametro de ajuste - delta
# Funcao: A partir de uma matriz 'a', calcula a multiplicacao entre a propria matriz e sua
# transposta ('at'*'a'), e ao final adiciona um multiplo (por delta) da matriz identidade ao resultado
def addDelta(a,delta) :
    transposed = a.transpose()                  # Transpoe a matriz 'a'
    At_A = np.matmul(transposed,a)              # Multiplica 'a' transposta por 'a'
    return At_A + delta*np.identity(len(At_A))  # Retorna a soma 'at_a' + delta*identidade 

# Nome: buildLowerA
# Parametros: variavel - n, matriz modelo - B
# Funcao: A partir de uma matriz modelo 'B', cria uma matriz para compor a matriz A da equacao
# Af = p , que sera utilizada para resolver o sistema linear.
def buildLowerA(n,B) :
    C = np.zeros((1,n))                                     # Matriz auxiliar C
    E = np.identity(n)                                      # Matriz identidade E
    A = np.array([[]])                                      # Matriz a ser devolvida A
    A1 = B.copy()                                           # Matriz A1 parcial de A
    for j in range (n) :
        for i in range(n) :
            if (i == 0) : pass
            elif(E[j][i] == 1) : A1 = np.vstack((A1,B))
            else : A1 = np.vstack((A1,C))
        if (j == 0) : A = A1.copy()
        else : A = np.hstack((A,A1))
        A1 = C.copy()
    return A

# Nome: buildMatrixA
# Parametros: parametro para o tamanho - n 
# Funcao: A partir de um numero inteiro n, cria a matriz 'A' que correlaciona os raios 'p' com
# a matriz de "obstaculos" f, de forma que Af = p
def buildMatrixA(n) :
    B = np.ones(n)
    C = np.identity(n)
    A1 = np.kron(B,C)                               # A1 e A2 sao as matrizes para os raios
    A2 = np.kron(C,B)                               # horizontais e verticais.
    A3 = buildLowerA(n,np.flip(np.identity(n),0))   # A3 e A4 sao para os raios diagonais.
    A4 = buildLowerA(n,np.identity(n))
    return np.array(np.concatenate((A1,A2,A3,A4),axis=0),dtype='float64')

# Nome: calculateDet
# Parametros: dir - diretorio dos dados
# Funcao: A partir dos dados providos, calcula o determinante das matrizes geradas pela funcao
# addDelta. Serve para analisar como o determinante cresce para maiores valores de delta
def calculateDet(dir) :
    for i in range(1,4) :                              # Itera sobre as imagens 1, 2 e 3
        p = load(dir + "im" + str(i) + "/p2.npy")      # Recebe o vetor p
        n = int((len(p) + 2)/6)                        # Calcula n a partir do tamanho de p
        A = buildMatrixA(n)                            # Constroi a matriz A a partir de n
        for j in range(-4,0,1) :                       # Calcula o determinante para diferentes valores
            if(j == -4) : delta = 0                    # de Delta
            else : delta = pow(10,j)
            det = np.longdouble(np.linalg.det(addDelta(A,delta)))
            print("O determinante para a imagem " + str(i) + " de tamanho " + str(n)+  " com delta " + str(delta) + " é: " +str(det))

# Nome: plotOriginal
# Parametros: dir - diretorio dos dados, imageNum - string com o numero da imagem
# Funcao: A partir dos dados providos, devolve o vetor f com os valores corretos, além de plotar
# uma imagem para comparacao visual.
def plotOriginal(dir,imageNum) :
    original = plt.imread(dir + imageNum + "/" + imageNum + ".png") # Carrega os dados da imagem
    n = len(original)                                               # Obtem n a partir da imagem
    plt.subplot(1,4,1)
    plt.imshow(original)                                            # Plota grafico original
    plt.title("Gráfico original",fontsize=7)
    f = np.zeros(n*n)
    for j in range(n):
        for i in range(n):
            f[n*j + i] = original[i][j]                             # Atribui valores ao vetor f
    return f

# Nome: solveImage
# Parametros: dir - diretorio dos dados, imageNum - string com o numero da imagem
# Funcao: A partir dos raios da tomografia p, constroi uma imagem f resolvendo o sistema Linear
# definido por (A_t*A + delta*I)f = A_t*p .
# Além disso, plota os valores para diferentes deltas, e imprime o erro de cada f obtido.
def solveImage(dir,imageNum) :
    fOriginal = plotOriginal(dir,imageNum) # Carrega o f original a partir da imagem fornecida
    p2 = load(dir + imageNum + "/p2.npy")  # Carrega os raios da tomografia p
    n = int((len(p2) + 2)/6)               # Calcula n a partir do tamanho do vetor p
    A = buildMatrixA(n)                    # Constrói a matriz A para o valor n obtido
    Atp = np.matmul(np.transpose(A),p2)    # Multiplica a A_t pelo vetor p, para o sistema linear
    plotmap = np.zeros((n,n))              # Prepara o mapa a ser plotado.
    for i in range(-3,0,1) :               # Itera para diferentes valores de delta
        delta = pow(10,i)
        A_Atdelta = addDelta(A,delta)                   # Calcula A_Atdelta para o valor de delta
        #f = np.matmul(np.linalg.inv(A_Atdelta),Atp)    # Resolve o sistema de forma mais rapida, usando a matriz inversa
        f = np.ones(n*n)                                # Assume que a primeira resposta de f é um vetor de 1
        f = gaussSeidel(A_Atdelta,f,Atp,100,0)          # Aplica o algoritmo de Gauss Seidel 100 vezes
        for j in range (0,n) :
            for k in range (0,n) :
                plotmap[k][j] = f[n*j + k]              # Constroi o plotmap a partir do f obtido
        fErr = fOriginal - f                            # Constroi o vetor do erro de f
        err = 100*(np.sqrt(np.matmul(fErr,fErr))/np.sqrt(np.matmul(fOriginal,fOriginal)))   # Calcula o erro relativo ao original
        print("Erro para delta de " + str(delta) + " : " + str(err) )   # Imprime o valor de erro para cada delta
        plt.subplot(1,4,i+5)                            # Plota o grafico da imagem obtida
        plt.imshow(plotmap)
        plt.title("Gráfico com delta " + str(delta),fontsize=7)
    plt.show()                                          # Apresenta ao usuario os graficos obtidos

### Funcao Main ###
imageNum = str(sys.argv[1])     # Obtem o numero da imagem a ser analisada a partir dos argumentos
solveImage(dir,imageNum)        # Resolve a imagem a ser analisada