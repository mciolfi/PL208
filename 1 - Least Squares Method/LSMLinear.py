#Least Squares Method linear
def arq(nome,ndados,tipo):
    import csv
    lista = []
    with open(nome, newline='') as csvfile: # o módulo csv detectará novas linhas automaticamente
        if tipo == ' ':
            texto = csv.reader(csvfile, delimiter=' ') # separe por espaço
        if tipo == ',':
            texto = csv.reader(csvfile, delimiter=',') # separe por virgula
        if tipo == '\t':
            texto = csv.reader(csvfile, delimiter='\t') # separe por tab
        for linha in texto:
            for t in range(len(linha)-ndados):
                linha.remove('')
            lista.append(linha)
    return (lista)

def LSMlinear():
    #Dados do exercício
    h = [69,67,71,65,72,68,74,65,66,72]
    s = [9.5,8.5,11.5,10.5,11,7.5,12,7,7.5,13]
    #tamanho dos lados da matriz
    tam = len(h)
    #Matriz em dados verticais
    x=[]
    for col in range(tam):
        x.append([1,h[col]])
    #Criando matriz transposta
    mT=[]
    for col in range(tam):
        mT.append(1)
    mT=(mT,h)
    #Multiplicando as matrizes para XtX
    XtX=[[0,0],[0,0]]
    for i in range(2):
        for k in range(2):
            soma = 0
            for j in range(tam):
                 soma = soma + mT[i][j] * x[j][k]
            XtX[i][k] = soma
    #Multiplicando as matrizes para XtY
    XtY=[0,0]
    for i in range(2):
        soma = 0
        for j in range(tam):
            soma = soma + mT[i][j] * s[j]
        XtY[i]= soma
    #Inversa da matriz XtX (inversão por matriz adjunta)
    det=XtX[0][0]*XtX[1][1]-XtX[0][1]*XtX[1][0]
    inv=[[0,0],[0,0]]
    inv[0][0]=XtX[1][1]/det
    inv[1][1]=XtX[0][0]/det
    inv[0][1]=-XtX[1][0]/det
    inv[1][0]=-XtX[0][1]/det
    #Encontrando ângulo Beta
    beta=[0,0]
    for i in range(2):
        soma = 0
        for j in range(2):
            soma = soma + inv[i][j] * XtY[j]
        beta[i]= soma
    print ('Altura das pessoas =',h)
    print ('Tamanho dos pés =',s)
    print ('beta = ',beta)
    if beta[1]>0:
        print ('relação positivamente linear')
    else:
        if beta[1]<0:
            print ('relação negativamente linear')
        else:
            print ('sem relação')
    altura = input('Informe a altura da pessoa ')
    #pe = input('Inform o tamanho do pé')
    tampe = beta[0]+int(altura)*beta[1]
    print ('Tamanho do pé é',tampe)
    #Plotando resultados entre os mínimos e máximos valores, caso precisasse a intersecção com o 0, ponto1=[0,hmax],ponto2=[beta[0],tampemax]
    hmin = min(h)
    hmax = max(h)
    hi= [hmin,hmax]
    tampemin = beta[0]+hmin*beta[1]
    tampemax = beta[0]+hmax*beta[1]
    tampei = [tampemin,tampemax]
    import matplotlib.pyplot as plt
    plt.plot(h,s,'go')
    plt.plot(hi,tampei,'r')
    plt.title('Height x Shoe Size')
    plt.grid(True)
    plt.xlabel("Altura")
    plt.ylabel("Tamanho do pé")
    plt.show()    
def LSM (dados):
    x = []
    y = []
    xt = []
    XtX=[[0]*len(dados[0])]*len(dados[0])
    XtY=[]
    for a in range(len(dados)):
        mat = (1,int(dados[a][0]),int(dados[a][1]))
        x.append(mat)
        y.append(int(dados[a][2]))
    #Transpondo a matriz
    for i in range(len(dados[0])):
        linha = []
        for j in range(len(dados)):
            linha.append(x[j][i])
        xt.append(linha)
    #Multiplicando matrizes
    for i in range(len(dados[0])):
        for k in range(len(dados[0])):
            soma = 0
            for j in range(len(dados)):
                soma = soma + x[j][k] * xt[i][j]
            XtX[i][k] = soma
            print (XtX[0][0])
            print (i,k,soma)
    print (XtX)
    for i in range(len(dados[0])):
        soma = 0
        for j in range(len(dados)):
            soma = soma + x[j][i] * y[j]
        XtY.append(soma)
    return (XtX,XtY)
def determinante(x):
    #Módulo para obtenção de determinante de matriz 2x2 ou 3x3
    # Definindo as variáveis
    a = 0
    b = 0
    c = len(x)-1
    mult1 = 1
    mult2 = 1
    loop = 0
    det = 0
    soma = []
    if len(x) == 2: d = len(x)-1 #Matriz 2x2
    if len(x) == 3: d = len(x)-2 #Matriz 3x3
    while loop == 0:
        mult1 = mult1*x[a][b]
        mult2 = mult2*x[a][c]
        if a == len(x)-1 and b == d: loop = 1
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
        if b > len(x)-1: b = 0
        if c < 0: c = len(x)-1
    for cont in range(len(soma)): det += soma[cont]
    return det
def matrizinv(x,det): #Faz inversão das matrizes com base no determinante
    #Definindo variáveis
    xt = []
    madj = []
    #Transpondo a matriz
    for i in range(len(x)):
        linha = []
        for j in range(len(x)):
            linha.append(x[j][i])
        xt.append(linha)
    #Obtendo a matriz adjunta atraves o determinante das matrizes menores 2x2, aplicando o sinal e 1/det
    for i in range(len(x)):
        if i == 0: a = 1
        else: a = 0
        if i == 2: b = 1
        else: b = 2
        linha = []
        for j in range(len(x)):
            if j == 0: c = 1
            else: c = 0
            if j == 2: d = 1
            else: d = 2
            #Adiciona os sinais conforme posição na matriz
            if (i+j)%2 == 0: calc = (xt[a][c]*xt[b][d]-xt[a][d]*xt[b][c])/int(det)
            else: calc = -(xt[a][c]*xt[b][d]-xt[a][d]*xt[b][c])/int(det)
            if calc == -0: calc = 0 #Corrige sinal negativo no zero
            linha.append(calc)
        madj.append(linha)
    return(madj)
dados = arq('Books_attend_grade.dat',3,'\t')
xtx,xty = LSM(dados)
print (xtx,xty)
det = determinante (xtx)
if det == 0: print ('Não existe matriz inversa')
else:
    print ('Matriz inversa possível, determinante = ',det)
    inv = matrizinv(xtx,det)
    print (inv)
