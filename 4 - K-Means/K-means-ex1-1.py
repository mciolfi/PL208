def Kmeans():
    #Definição de valores iniciais e tamanho das matrizes
    x = [1.9,3.4,2.5,1.5,3.5,2.2,3.4,3.6,5,4.5,6,1.9,1,1.9,0.8,1.6,1]
    y = [7.3,7.5,6.8,6.5,6.4,5.8,5.2,4,3.2,2.4,2.6,3,2.7,2.4,2,1.8,1]
    cor = ['b','g','r','c','m','y','k']
    #x= [0,0,1,1]
    #y= [0,1,0,1]
    tam = len(x)
    #Define o tamanho da seta no gráfico
    seta=(max(x)-min(x))/(3*len(x))
    contador = 0
    interacao = 0
    dist = []
    ct = []
    #K-Means com K=3, geração de matriz k*2 linhas e posicionamento nos primeiros itens da matriz
    k=3
    for i in range(k):
        dist.append([i]*tam)
        dist.append([i]*tam)
        ct.append([x[i]]+[y[i]])
    #Definição de gráficos e plotagem de dados originais
    import matplotlib.pyplot as plt
    plt.figure(2)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.figure(1)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.plot(x,y,str(cor[k])+'o')
    #Executa até que não haja mudança de distâncias entre centros
    while contador < k:
        #Atribui contador de interações
        interacao = interacao+1
        #Atribui um valor limite para evitar loop
        if interacao == 10:
            break
        #Define o tamanho das matrizes cx e cy
        cx = []
        cy = []
        for i in range(k):
            cx.append([])
            cy.append([])
        #Verifica distâncias euclidianas entre posicionamentos dos K e dados originais
        for k1 in range(k):
            #Grava as distâncias anteriores
            for j in range(tam):
                dist[k1+k][j] = dist[k1][j]
                #Calcula as novas distâncias
                deltax = ((ct[k1][0]-x[j])**2)
                deltay = ((ct[k1][1]-y[j])**2)
                dist[k1][j] = (deltax+deltay)**(0.5)
        #Verifica se houve alteração entre centros
        for k1 in range(k):
            if dist [k1] == dist[k1+k]:
                contador = contador + 1
                #Plota valores originais e centros finais
                if contador == k:
                    plt.figure(2)
                    for k1 in range(k):
                        plt.plot(ct[k1][0],ct[k1][1],str(cor[k1])+'x')
                        plt.annotate('c'+str(k1+1)+'.'+str(interacao-1), xy=(ct[k1][0]+seta, ct[k1][1]), xytext=(ct[k1][0]+seta*5, ct[k1][1]-seta*5), color=cor[k1],
                            arrowprops=dict(facecolor=cor[k1], shrink=0.005),
                            )
                    plt.figure(1)
        #Classifica pontos com menor distância em relação a cada centro desde que haja alteração entre as distâncias
        if contador < k:
            for i in range(tam):
                lista = []
                for k1 in range(k):
                    lista.append(dist[k1][i])
                menor = lista.index(min(lista))
                cx[menor].append(x[i])
                cy[menor].append(y[i])
            #Plota centros e indicações de cada interação
            for k1 in range(k):
                plt.plot(ct[k1][0],ct[k1][1],str(cor[k1])+'x')
                plt.annotate('c'+str(k1+1)+'.'+str(interacao), xy=(ct[k1][0]+seta, ct[k1][1]), xytext=(ct[k1][0]+seta*5, ct[k1][1]-seta*5), color=cor[k1],
                    arrowprops=dict(facecolor=cor[k1], shrink=0.005),
                    )
                plt.figure(2)
                plt.plot(cx[k1],cy[k1],str(cor[k1])+'o')
                plt.figure(1)
            plt.figure (2)
            plt.title('Gráfico K-Means - no. de interações =' + str(interacao))
            plt.figure (1)
            plt.title('Gráfico K-Means - no. de interações =' + str(interacao))
            #Define novos centros e obtem média das distâncias
            for k1 in range(k):
                a = 0
                b = 0
                for i in range(len(cx[k1])):
                    a += cx[k1][i]
                    b += cy[k1][i]
                if len(cx[k1])>1:
                    a = a/len(cx[k1])
                    b = b/len(cx[k1])
                #Define novo centro K
                ct[k1][0] = a
                ct[k1][1] = b
            print (interacao, ct)
            print (cx)
    plt.show()
Kmeans()
