def determinante(m):
    #det=+x[0][0]*x[1][1]*x[2][2]*x[3][3]
    #    +x[0][1]*x[1][2]*x[2][3]*x[3][0]
    #    +x[0][2]*x[1][3]*x[2][0]*x[3][1]
    #    +x[0][3]*x[1][0]*x[2][1]*x[3][2]
    #    -x[0][3]*x[1][2]*x[2][1]*x[3][0]
    #    -x[0][2]*x[1][1]*x[2][0]*x[3][3]
    #    -x[0][1]*x[1][0]*x[2][3]*x[3][2]
    #    -x[0][0]*x[1][3]*x[2][2]*x[3][1]
    # Definindo as variáveis
    a = 0
    b = 0
    c = len(x)-1
    mult1 = 1
    mult2 = 1
    loop = 0
    det = 0
    soma = []
    while loop == 0:
        mult1 = mult1*x[a][b]
        mult2 = mult2*x[a][c]        
        if a == len(x)-1 and b == len(x)-2:
            loop = 1
        a = a+1
        b = b+1
        c = c-1
        if a > len(x)-1:
            a = 0
            soma.append(mult1-mult2)
            # print (mult1,-mult2) #Apresenta os valores obteidos pela Regra de Sarrus
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
x = [[2,3],[0,5]]
det = determinante (x)
print ('determinante = ',det)
