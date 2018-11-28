def main():
    #Dados do exercício
    a = []
    h = [69,67,71,65,72,68,74,65,66,72]
    s = [9.5,8.5,11.5,10.5,11,7.5,12,7,7.5,13]
    mA = (h,s)
    #tamanho dos lados da matriz
    tam = len(h)
    #Matriz em dados verticais
    x= []
    for col in range(tam):
        x.append([1,h[col]])
    print (x)
    #Criando matriz transposta
    mT=[]
    for col in range(tam):
        mT.append([0,0])
    for i in range(tam):
        for j in range(2):
            mT[i][j] = x[j][i]
    print (x)
    print (mT)
main ()

    #transposta
    #for i in range(tam):
    #    for j in range(tam):
    #        mT[i][j] = mA[j][i]
    #print ('\n')
    #for b in range(tam):
        #matriz1[b][0].append(h[b])
    #    matriz1.append(h[b])
    #print ('\n')
    #for i in range(tam):
    #    a.append(1)
    #matriz = (a,h)    
    #print (matriz)
    
