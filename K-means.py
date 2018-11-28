def Kmeans():
    #Definição de valores iniciais e tamanho das matrizes
    altura = [167,120,113,175,108]
    peso = [55,32,33,76,25]
    dist=[[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[1,1,1,1,1]]
    tam = len(altura)
    j=0
    #K-Means com K=2 e posicionamento conforme 2 e 3o item da matriz
    c1=altura[1],peso[1]
    c2=altura[2],peso[2]
    #Definição de gráfico e plote de dados originais
    import matplotlib.pyplot as plt
    plt.xlabel("Altura")
    plt.ylabel("Peso")
    plt.grid(True)
    plt.plot(altura,peso,'go')
    #Verifique distâncias entre posicionamentos do K e dados originais
    while (dist[0]!=dist[2] and dist[1]!=dist[3]):        
        #Zera as coordenadas dos centros e atribuir contador de interações
        c1x=[]
        c1y=[]
        c2x=[]
        c2y=[]
        j=j+1
        #Verificar distâncias euclidianas entre posicionamentos dos K e dados originais
        for i in range(tam):
            alt1=(c1[0]-altura[i])**2
            alt2=(c2[0]-altura[i])**2
            pes1=(c1[1]-peso[i])**2
            pes2=(c2[1]-peso[i])**2
            #Grava as distâncias anteriores
            dist[2][i]= dist[0][i]
            dist[3][i]= dist[1][i]
            #Calcula as novas distâncias
            dist[0][i]= (alt1+pes1)**(0.5)
            dist[1][i]= (alt2+pes2)**(0.5)
            #Classifica pontos com menor distância em relação a cada centro
            if dist[0][i] < dist[1][i]:
                c1x.append (altura[i])
                c1y.append (peso[i])
            else:
                c2x.append (altura[i])
                c2y.append (peso[i])
        #Confirma se houve alteração das distâncias em relação a intereção anterior para plotar resultados
        if (dist[0]!=dist[2] or dist[1]!=dist[3]):
            #Plota centros e indicações de cada interação
            plt.plot(c1[0],c1[1],'b+')
            plt.plot(c2[0],c2[1],'rx')
            plt.annotate('c1.'+str(j), xy=(c1[0]+0.05, c1[1]+0.05), xytext=(c1[0]+5, c1[1]+5), color='b',
                arrowprops=dict(facecolor='blue', shrink=0.05),
                )
            plt.annotate('c2.'+str(j), xy=(c2[0]-0.05, c2[1]+0.05), xytext=(c2[0]-10, c2[1]+5), color='r',
                arrowprops=dict(facecolor='red', shrink=0.05),
                )
            plt.title('Altura x Peso - no. de interações =' + str(j))
        #Novo Centro
        a=0
        b=0
        c=0
        d=0
        #Obter média das distâncias
        for i in range(len(c1x)):
            a+=c1x[i]
            b+=c1y[i]
        a=a/len(c1x)
        b=b/len(c1x)
        for i in range(len(c2x)):
            c+=c2x[i]
            d+=c2y[i]
        c=c/len(c2x)
        d=d/len(c2x)
        c1=a,b
        c2=c,d
    plt.show()
Kmeans()
