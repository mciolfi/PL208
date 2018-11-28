def main():
    #Dados do exercício
    books=[0,1,0,2,4,4,1,4,3,0,2,1,4,1,0,1,3,0,1,4,4,0,2,3,1,0,3,3,2,2,3,2,2,3,4,4,3,1,2,0]
    attend=[9,15,10,16,10,20,11,20,15,15,8,13,18,10,8,10,16,11,19,12,11,19,15,15,20,6,15,19,14,13,17,20,11,20,20,20,9,8,16,10]
    grade=[45,57,45,51,65,88,44,87,89,59,66,65,56,47,66,41,56,37,45,58,47,64,97,55,51,61,69,79,71,62,87,54,43,92,83,94,60,56,88,62]
    quant=3
    #file=open ('Books_attend_grade.dat','r')
    #print (file)
    #x1 = file(:,1)
    #x2 = Books_attend_grade(:,2)
    #y = Books_attend_grade(:,3)
    #one = ones(40,1)
    #X = [one, x1,x2]

    #tamanho dos lados da matriz
    tamb = len(books)
    tama = len(attend)
    tamg = len(grade)
    #Verificando se as matrizes foram preenchidas corretamente
    if tamb == tama:
        if tamb == tamg:
            print ('em ordem')
        else:
            print('rever dados')
            quit()
    #Matriz em dados verticais
    x=[]
    for col in range(tamb):
        x.append([1,books[col],grade[col]])
    print ('x = ',x)
    #Criando matriz transposta
    mT=[]
    for col in range(tamb):
        mT.append(1)
    mT=(mT,books,attend)
    print ('mT = ',mT)
    #Multiplicando as matrizes para XtX
    XtX=[]
    for i in range(quant):
        if quant==2:
            XtX.append([0,0])
        if quant==3:
            XtX.append([0,0,0])
    for i in range(quant):
        for k in range(quant):
            soma = 0
            for j in range(tamb):
                 soma +=mT[i][j] * x[j][k]
            XtX[i][k] = soma
    print ('XtX = ',XtX)
    #Multiplicando as matrizes para XtY
    XtY=[]
    if quant==2:
        XtY = [0,0]
    if quant==3:
        XtY = [0,0,0]
    for i in range(quant):
        soma = 0
        for j in range(tamb):
            soma += mT[i][j] * grade[j]
        XtY[i]= soma
    #Inversa da matriz XtX (inversão por matriz adjunta)
    det=0
    b=0
    c=0
    if quant==2:
        det=XtX[0][0]*XtX[1][1]-XtX[0][1]*XtX[1][0]
        inv=[[0,0],[0,0]]
        inv[0][0]=XtX[1][1]/det
        inv[1][1]=XtX[0][0]/det
        inv[0][1]=-XtX[1][0]/det
        inv[1][0]=-XtX[0][1]/det
    if quant==3:
        for a in range(quant):
            b=a+1
            c=a+2
            if b>2:
                b=0
            if c>2:
                c=c-3
            det=det+XtX[0][a]*XtX[1][b]*XtX[2][c]-XtX[0][c]*XtX[1][b]*XtX[2][a]
        inv=[[0,0,0],[0,0,0],[0,0,0]]
        a=0
        for j in range(quant):
            a=i+1
            if a>2:
                a=0
            if j%2==0:
                b=-1
            else:
                b=1
            inv[0][j]=(XtX[a][1]*XtX[2][2]-XtX[a][2]*XtX[2][1])/(-b*det)
            inv[1][j]=(XtX[a][0]*XtX[2][2]-XtX[a][2]*XtX[2][0])/(b*det)
            inv[2][j]=(XtX[a][0]*XtX[2][1]-XtX[a][1]*XtX[2][0])/(-b*det)
    print ('inversa = ',inv)
    #Encontrando ângulo Beta
    if quant==2:
        beta = [0,0]
    if quant==3:
        beta = [0,0,0]
    for i in range(quant):
        soma = 0
        for j in range(quant):
            soma = soma + inv[i][j] * XtY[j]
        beta[i]= soma
    #print ('Livros =',books)
    #print ('Frequencia =',attend)
    #print ('Notas =',grade)
    livro = input('Informe o livro ')
    frequencia = beta[0]+int(livro)*beta[1]+int(livro)*beta[2]
    print ('A frequencia é',frequencia)
    #Plotando resultados
    bmin = min(books)
    bmax = max(books)
    bi= [bmin,bmax]
    tampemin = beta[0]+bmin*beta[1]+bmin*beta[2]
    tampemax = beta[0]+bmax*beta[1]+bmin*beta[2]
    tampei = [tampemin,tampemax]
    print (bmin,bmax)
    #from mpl_toolkits.mplot3d import Axes3D
    #import matplotlib.pyplot as plt
    #from matplotlib import cm
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #surf = ax.plot_surface(books,attend,grade, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    #plt.plot(books,attend,grade,'go')
    #plt.plot(bi,tampei,'r') 
    #plt.title('Books x Attend x Grade')
    #plt.grid(True)
    #plt.xlabel('Livros')
    #plt.ylabel('Frequencia')
    #plt.zlabel('Notas')
    #plt.show()
    #print (x)
    #print (XtX)
    #print (XtY)
    #print (inv)
    #print (beta)
main ()
