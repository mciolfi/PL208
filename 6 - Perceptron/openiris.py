def arq(name,ndata,types):
    import csv
    listt = []
    with open(name, newline='') as csvfile: # o módulo csv detectará novas linhas automaticamente
        if types == ' ':  text = csv.reader(csvfile, delimiter=' ') # separe por espaço
        if types == ',':  text = csv.reader(csvfile, delimiter=',') # separe por virgula
        if types == '\t': text = csv.reader(csvfile, delimiter='\t') # separe por tab
        for line in text:
            for t in range(len(line)-ndata): line.remove('')
            listt.append(line)
    return (listt)
lista = arq('iris.data.txt',5,',')
inputs = []
outputs = []
for cont in range(len(lista)):
    inputs.append([float(lista[cont][i]) for i in range(4)])
    # Define one value for each classification: Iris-setosa = 0,Iris-versicolor = 1, Iris-virginica = 2
    if lista[cont][4] == 'Iris-setosa': typef = 0
    if lista[cont][4] == 'Iris-versicolor': typef = 1
    if lista[cont][4] == 'Iris-virginica': typef = 2
    outputs.append(typef)
print (inputs)
print (outputs)
