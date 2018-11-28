def Bayes ():
    import math
    #Definição de valores iniciais e tamanho das matrizes
    yes = [25.2, 19.3, 18.5, 21.7, 20.1, 24.3, 22.8, 23.1, 19.8]
    no = [27.3,30.1,17.4,29.5,15.1]
    mediay = 0
    median = 0
    desvy = 0
    desvn = 0
    #Calculo das medias
    for i in range (len(yes)):
        mediay += yes[i]
    mediay = mediay/len(yes)
    for i in range (len(no)):
        median += no[i]
    median = median/len(no)
    #Calculo do desvio padrao
    for i in range (len(yes)):
        desvy += (yes[i] - mediay)**2
    desvy = (desvy/len(yes))**0.5
    for i in range (len(no)):
        desvn += (no[i] - median)**2
    desvn = (desvn/len(no))**0.5
    #Saida de modelo Gaussiano
    x = 15 #input('Temperatura')
    Pyes = math.exp(-((x-mediay)**2)/(2*(desvy**2)))/(desvy*(2*math.pi)**0.5)
    Pno = math.exp(-((x-median)**2)/(2*(desvn**2)))/(desvn*(2*math.pi)**0.5)
    print (mediay,median,desvy,desvn,Pyes,Pno)
    if Pyes > Pno:
        print ('Sim')
    else:
        print ('Não')
Bayes ()
