def main():
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
main ()
