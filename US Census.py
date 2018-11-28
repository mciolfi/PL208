def main():
    #Dados do exercício e tamanho da matriz
    x = [1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]
    y = [75.9950,91.9720,105.7110,123.2030,131.6690,150.6970,179.3230,203.2120,226.5050,249.6330,281.4220]
    tam = len(x)
    #Definir tipo de matriz: 1 = linear, 2 = quadrática, 3 = com peso (w)
    tipo = 2
    w = 1
    #Matriz em dados verticais
    x1 = []
    x2 = []
    for col in range(tam):
        #x1.append([1,x[col]])
        #x1.append([1,x[col]])
        if tipo == 2:
            x2.append(x[col]**2)
            x1.append([1,x[col],x2[col]])
        else:
            x1.append([1,x[col]])
    #Criando matriz transposta
    mT = []
    for col in range(tam):
        mT.append(1)
    XtX = [[0]*(tipo+1)]*(tipo+1)
    mT=(mT,x,x2)
    #Multiplicando as matrizes para XtX
    for i in range(tipo+1):
        for k in range(tipo+1):
            soma = 0
            for j in range(tam):
                 soma = soma + mT[i][j] * w * x1[j][k]
            XtX[i][k] = soma
    #Multiplicando as matrizes para XtY
    XtY = [0]*(tipo+1)
    for i in range(tipo+1):
        soma = 0
        for j in range(tam):
            soma = soma + mT[i][j] * w * y[j]
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
    print ('Valor de X =',x)
    print ('Valor de Y =',y)
    print ('mT =',mT)
    print ('XtX =',XtX)
    print ('XtY =',XtY)
    print ('beta = ',beta)
    if beta[1]>0:
        print ('relação positivamente linear')
    else:
        if beta[1]<0:
            print ('relação negativamente linear')
        else:
            print ('sem relação')
    #xa = input('Informe valor de X ')
    #pe = input('Inform o tamanho do pé')
    #ya = beta[0]+int(xa)*beta[1]
    #print ('O Valor y é',ya)
    #Plotando resultados entre os mínimos e máximos valores, caso precisasse a intersecção com o 0, ponto1=[0,hmax],ponto2=[beta[0],tampemax]
    xmin = min(x)
    xmax = max(x)
    xi= [xmin,xmax]
    ymin = beta[0]+xmin*beta[1]
    ymax = beta[0]+xmax*beta[1]
    yi = [ymin,ymax]
    import matplotlib.pyplot as plt
    plt.plot(x,y,'go')
    plt.plot(xi,yi,'r')
    plt.title('X vs. Y')
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    #plt.show()    
main ()
