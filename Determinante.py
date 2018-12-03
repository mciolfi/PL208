def determinante(m):
    #Módulo para obtenção de determinante de matriz 2x2 ou 3x3
    #det2x2=+x[0][0]*x[1][1]
    #       -x[0][1]*x[1][0]
    #det3x3=+x[0][0]*x[1][1]*x[2][2]
    #       +x[0][1]*x[1][2]*x[2][0]
    #       +x[0][2]*x[1][0]*x[2][1]
    #       -x[0][2]*x[1][1]*x[2][0]
    #       -x[0][1]*x[1][0]*x[2][2]
    #       -x[0][0]*x[1][2]*x[2][1]
    # Definindo as variáveis
    a = 0
    b = 0
    c = len(x)-1
    mult1 = 1
    mult2 = 1
    loop = 0
    det = 0
    soma = []
    if len(x) == 2:
        d = len(x)-1
    if len(x) == 3:
        d = len(x)-2
    while loop == 0:
        mult1 = mult1*x[a][b]
        mult2 = mult2*x[a][c]
        if a == len(x)-1 and b == d:
            loop = 1
        a = a+1
        b = b+1
        c = c-1
        if a > len(x)-1:
            a = 0
            soma.append(mult1-mult2)
            # print (mult1,-mult2) #Apresenta os valores obtidos pela Regra de Sarrus
            mult1 = 1
            mult2 = 1
            b = len(soma)
            c = len(x)-len(soma)-1
        if b > len(x)-1:
            b = 0
        if c < 0:
            c = len(x)-1
    for cont in range(len(soma)):
        det += soma[cont]
    return det
x = [[4,2],[1,1]]
det = determinante (x)
print ('determinante = ',det)
