#Least Squares Method linear
def arq(nome,ndados,tipo): # Função para captação de dados de arquivos Dataset
    import csv #Modulo para abertura de arquivo tipo CSV
    lista = [] #Matriz onde os dados do arquivo serão aplicados
    with open(nome, newline='') as csvfile: # o módulo csv detectará novas linhas automaticamente
        if tipo == ' ': texto = csv.reader(csvfile, delimiter=' ') # separe por espaço
        if tipo == ',': texto = csv.reader(csvfile, delimiter=',') # separe por virgula
        if tipo == '\t': texto = csv.reader(csvfile, delimiter='\t') # separe por tab
        for linha in texto:
            for t in range(len(linha)-ndados): linha.remove('') #Remove dados nulos na matriz
            lista.append(linha) #Adiciona À matriz lista os dados do arquivo
    return (lista) #Retorna os dados do arquivo para o programa principal

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
    
# Função para obter valores através do método dos mínimos quadrados
def LSM (dados):
    x = []                                                              # Define x como matriz de entrada
    y = []                                                              # Define y como matriz de saíde
    xt = []                                                             # Define xT (x transposta) como matriz
    XtX = []                                                            # Define multiplicação das matrizes xT e x como matriz
    XtY = []                                                            # Define multiplicação das matrizes xT e y como matriz
    for mat in range(len(dados[0])): XtX.append([0]*len(dados[0]))      # Define tamanho da matriz de multiplicação
    for i in range(len(dados)):
        matx = []                                                       # Define e limpa a matriz x
        matx.append(1)                                                  # Adiciona o Bias
        for j in range(len(dados[0])-1): matx.append(dados[i][j])       # Inclui dados x a matriz com Bias
        maty = dados[i][len(dados[0])-1]                                # Inclui dados y para a matriz a ser multiplicada
        x.append(matx)                                                  # Atribui valores para matriz x com bias
        y.append(maty)                                                  # Atribui valores para matriz y
    # Transpor a matriz X
    for i in range(len(dados[0])):
        matx = []                                                       # Define e limpa a matriz de entrada de valores de X
        for j in range(len(dados)): matx.append(x[j][i])                # Transpoe a matriz x
        xt.append(matx)                                                 # Atribui valores para matriz xT
    #Multiplica matrizes
    for i in range(len(dados[0])):
        soma = 0                                                            # Define como numérica e limpa a variável soma
        for j in range(len(dados[0])):
            for k in range(len(dados)):
                soma = soma + float(x[i][j]) * float(xt[j][k])                             # Soma a multiplicação de cada linha por coluna entre matrizes
            print (x[i][j], xt[j][k],soma)
            XtX[i][j] = soma                                                     # Atribiu valores da matriz multiplicação axb
    
    #for i in range(len(dados[0])):
    #    for k in range(len(dados[0])):
    #        soma = 0                                                    # Define como numérica e limpa a variável soma
    #        print (x[j][k],xt[i][j])
    #        for j in range(len(dados)): soma = soma + x[j][k] * xt[i][j]# Soma a multiplicação de cada linha por coluna de x por xT
    #        XtX[i][k] = soma                                            # Atribiu valores da matriz multiplicação xT.x
    for i in range(len(dados[0])):
        soma = 0                                                        # Define como numérica e limpa a variável soma
        for j in range(len(dados)): soma = soma + float(x[j][i]) * float(y[j])        # Soma a multiplicação de cada linha por coluna de y por xT
        XtY.append([soma])                                              # Atribiu valores da matriz multiplicação xT.y
    return (XtX,XtY)

# Função de obtenção de determinante da matriz 2x2 ou 3x3
def determinante(x):
    i = 0                                                               # Define linha como numérico
    j = 0                                                               # Define coluna1 como numérico
    k = len(x)-1                                                        # Define coluna2 como numérico
    mult1 = 1                                                           # Define multiplicação positiva como numérico
    mult2 = 1                                                           # Define multiplicação negativa como numérico
    loop = 0                                                            # Define finalização do ciclo de cálculo como numérico
    det = 0                                                             # Define determinante como numérico
    soma = []                                                           # Define a matriz de soma para a Regra de Sarrus
    if len(x) == 2: d = len(x)-1                                        # Confirma se a matriz é 2x2
    if len(x) == 3: d = len(x)-2                                        # Verifica se a matriz é 3x3
    while loop == 0:                                                    # Inicia o ciclo de multiplicação
        mult1 = mult1 * x[i][j]                                         # Multiplica valores positivos
        mult2 = mult2 * x[i][k]                                         # Multiplica valores negativos
        if i == len(x)-1 and j == d: loop = 1                           # Encerra o ciclo de calculo
        i = i + 1                                                       # Aumenta o valor da linha
        j = j + 1                                                       # Aumenta o valor da coluna1
        k = k - 1                                                       # Reduz o valor da coluna2
        if i > len(x)-1:                                                # Se o valor da linha for maior que o tamanho da matriz -1
            i = 0                                                       # Zera o valor da linha
            soma.append(mult1-mult2)                                    # Adiciona a matriz soma os valores obtidos pela Regra de Sarrus 
            mult1 = 1; mult2 = 1                                        # Retorna as variáveis de multiplicação ao estado inicial
            j = len(soma)                                               # Define a coluna1 com o tamanho da matriz soma
            k = len(x)-len(soma)-1                                      # Define a coluna2 como a diferença dos tamanhos das matrizes
        if j > len(x)-1: j = 0                                          # Retorna a variável para o estado inicial
        if k < 0: k = len(x)-1                                          # Retorna a variável para o estado inicial
    for loop in range(len(soma)): det += soma[loop]                     # Atribui valores ao determinante
    return det                                                          # Retorna com o valor do determinante

def matrizinv(dados,det): #Faz inversão das matrizes com base no determinante
    #Definindo variáveis
    xt = []
    madj = []
    if len(dados) == 2:
        madj = [[0,0],[0,0]]
        madj[0][0] = dados[1][1]/det
        madj[0][1] = -dados[0][1]/det
        madj[1][0] = -dados[1][0]/det
        madj[1][1] = dados[0][0]/det
    if len(dados) == 3:
        #Transpondo a matriz
        for i in range(len(dados[0])):
            matx = []                                                       # Define e limpa a matriz de entrada de valores de X
            for j in range(len(dados)): matx.append(dados[j][i])            # Transpoe a matriz dados
            xt.append(matx)                                                 # Atribui valores para matriz xt
        #Obtendo a matriz adjunta atraves o determinante das matrizes dos cofatores 2x2, aplicando o sinal e 1/det
        for i in range(len(dados)):
            if i == 0: a = 1
            else: a = 0
            if i == 2: b = 1
            else: b = 2
            linha = []
            for j in range(len(dados)):
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

# Função para transpor matrizes
def transposta(dados):
    xt = []                                                                 # Define xt como matriz
    for i in range(len(dados[0])):
        matx = []                                                           # Define e limpa a matriz de entrada de valores de X
        for j in range(len(dados)): matx.append(dados[j][i])                # Transpoe a matriz dados
        xt.append(matx)                                                     # Atribui valores para matriz xt
    return (xt)

# Função multiplica matrizes
def multiplica (a,b):
    ab = []
    for mat in range(len(b)): ab.append ([0*len(b)]) # Define o tamanho da matriz de multiplicação
    print (ab)        
    for i in range(len(a)):
        soma = 0                                                            # Define como numérica e limpa a variável soma
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                soma = soma + a[i][j] * b[j][k]                             # Soma a multiplicação de cada linha por coluna entre matrizes
        ab[i][k] = soma                                                     # Atribiu valores da matriz multiplicação axb
    return(ab)

# Função plotar resultados
def plot(dados,beta,nome,x,y):
    import matplotlib.pyplot as plt
    #Plotando resultados entre os mínimos e máximos valores, caso precisasse a intersecção com o 0, ponto1=[0,hmax],ponto2=[beta[0],tampemax]
    dadosmin = min(transposta(dados)[0])                                               # Define os mínimos valores de dados
    dadosmax = max(transposta(dados)[0])
    dadosi= [float(dadosmin),float(dadosmax)]
    tampemin = beta[0][0] + float(dadosmin) * beta[1][0]
    tampemax = beta[0][0] + float(dadosmax) * beta[1][0]
    tampei = [tampemin,tampemax]
    plt.plot(float(transposta(dados)[0]),float(transposta(dados)[1]),'go')
    plt.plot(dadosi,tampei,'r')
    plt.grid(True)
    plt.title(nome)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()


# Programa principal utilizando método dos mínimos quadrados
dados = arq('Books_attend_grade.dat',3,'\t')
print (dados)
#h = [[69,67,71,65,72,68,74,65,66,72], [9.5,8.5,11.5,10.5,11,7.5,12,7,7.5,13]]
#dados = transposta(h)                                                   # Transpoe a matriz de entrada
#print (dados,'/n')
xtx,xty = LSM(dados)                                                    # Obtém os valores de mínimos quadrados e atribui às matrizes de multiplicação
print ('XtX =', xtx, 'XtY =',xty)
det = determinante (xtx)                                                # Atribui o determinante da matriz
if det == 0: print ('Não existe matriz inversa')                        # Verifica se a matriz pode ser invertida
else:
    print ('Matriz inversa possível, determinante = ',det)
    xtxinv = matrizinv(xtx,det)
    print ('XtXinv = ',xtxinv)
    beta = multiplica(xtxinv,xty)
    print ('beta = ',beta)
plot (dados,beta,'Height x Shoe Size','Altura','Tamanho do pé') 
