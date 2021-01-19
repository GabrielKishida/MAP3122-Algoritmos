def vectorsum(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

def vectormult(mult,vector):
    c = []
    for i in range(len(vector)):
        c.append(vector[i]*mult)
    return c

def vectordiv(div,vector):
    c = []
    for i in range(len(vector)):
        c.append(vector[i]/div)
    return c

def elimgauss(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            coef = -(matrix[j][i]/matrix[i][i])
            auxvector = vectormult(coef,matrix[i])
            matrix[j] = vectorsum(matrix[j],auxvector)
    matrix[n-1] = vectordiv(matrix[n-1][n-1],matrix[n-1])
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            coef = -(matrix[j][i]/matrix[i][i])
            auxvector = vectormult(coef,matrix[i])
            matrix[j] = vectorsum(matrix[j],auxvector)
    for i in range(n):
        matrix[i] = vectordiv(matrix[i][i],matrix[i])
    return matrix

matrix = [[1,-1,2,2],[2,1,-1,1],[-2,-5,3,3]]
print(elimgauss(matrix))