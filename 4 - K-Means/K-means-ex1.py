def Kmeans():
    #Definição de valores iniciais e tamanho das matrizes
    x = [1.9,3.4,2.5,1.5,3.5,2.2,3.4,3.6,5,4.5,6,1.9,1,1.9,0.8,1.6,1]
    y = [7.3,7.5,6.8,6.5,6.4,5.8,5.2,4,3.2,2.4,2.6,3,2.7,2.4,2,1.8,1]
    cor = ['b','g','r','c','m','y','k']
    #x= [1,2,3,4,5,6,7,8,9,10]
    #y= [11,12,13,14,15,16,17,20,19,18]
    tam = len(x)
    #Define o tamanho da seta no gráfico
    seta=(max(x)-min(x))/(3*len(x))
    contador = 0
    interacao = 0
    dist = []
    ct = []
    checkand = ''
    checkor = ''
    #K-Means com K=3 e posicionamento nos primeiros itens da matriz
    k=3
    #checkand = '('
    #checkor = '('
    for i in range(k):
        for j in range(k):
            dist.append([' ']*tam)
        ct.append([x[i]]+[y[i]])    
        if i != (k-1):
            checkand += 'dist['+str(i)+']!=dist['+str(i+k)+'] and '
            checkor += 'dist['+str(i)+']!=dist['+str(i+k)+'] or '
        else:
            checkand += 'dist['+str(i)+']!=dist['+str(i+k)+']'
            checkor += 'dist['+str(i)+']!=dist['+str(i+k)+']'
    #Definição de gráfico e plotagem de dados originais
    import matplotlib.pyplot as plt
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.plot(x,y,str(cor[k])+'o')
    #Verifica distâncias entre posicionamentos do K e dados originais
    while contador < 3:
        #Zera a lista de pontos próximos e atribuir contador de interações
        interacao = interacao+1
        #if dist[0]!=dist[3] and dist[1]!=dist[4] and dist[2]!=dist[5]:
        
        #    print (interacao,checkand)
        #if checkand:
        #    print (interacao,checkand)
        if interacao==10:
            break
        #Define o tamanho das matrizes cx e cy
        cx = []
        cy = []
        for i in range(k):
            cx.append([])
            cy.append([])
        #Verifica distâncias euclidianas entre posicionamentos dos K e dados originais
        for k1 in range(k):
            if dist [k1] == dist[k1+k]:
                contador = contador + 1
            #Grava as distâncias anteriores
            for j in range(tam):
                dist[k1+k][j] = dist[k1][j]
            #print (dist[3])
            for j in range(tam):
                deltax = ((ct[k1][0]-x[j])**2)
                deltay = ((ct[k1][1]-y[j])**2)
                #Calcula as novas distâncias
                dist[k1][j] = (deltax+deltay)**(0.5)
        #print (dist)
        #print ('dist0 =', dist[0],'\n','dist3 =', dist[3],'\n')
        #Classifica pontos com menor distância em relação a cada centro
        for i in range(tam):
            lista=[]
            for k1 in range(k):
                lista.append(dist[k1][i])              
                menor=lista.index(min(lista))
                cx[menor].append(x[i])
                cy[menor].append(y[i])
        #Confirma se houve alteração das distâncias em relação a intereção anterior para plotar resultados
        if checkor:
            #Plota centros e indicações de cada interação
            for k1 in range(k):
                plt.plot(ct[k1][0],ct[k1][1],'rx')
                plt.annotate('c'+str(k1)+'.'+str(interacao), xy=(ct[k1][0]+seta, ct[k1][1]+seta), xytext=(ct[k1][0]+seta*5, ct[k1][1]+seta*5), color=cor[k1],
                    arrowprops=dict(facecolor=cor[k1], shrink=0.005),
                    )
            plt.title('Gráfico K-Means - no. de interações =' + str(interacao))
        #Novo Centro
        a=0
        b=0
        c=0
        d=0
        #Obter média das distâncias
        for k1 in range(k):
            for i in range(len(cx[k1])):
                a+=cx[k1][i]
                b+=cy[k1][i]
                c+=cx[k1][i]
                d+=cy[k1][i]
            if len(cx[k1])>1:
                a=a/len(cx[k1])
                b=b/len(cx[k1])                
                c=c/len(cx[k1])
                d=d/len(cx[k1])
            ct[k1][0] = a
            ct[k1][1] = b
    plt.show()
Kmeans()
