def arq(nome,ndados,tipo):
    import csv
    lista = []
    with open(nome, newline='') as csvfile: # o módulo csv detectará novas linhas automaticamente
        if tipo == ' ':
            texto = csv.reader(csvfile, delimiter=' ') # separe por espaço
        if tipo == ',':
            texto = csv.reader(csvfile, delimiter=',') # separe por virgula
        if tipo == '\t':
            texto = csv.reader(csvfile, delimiter='\t') # separe por tab
        for linha in texto:
            for t in range(len(linha)-ndados):
                linha.remove('')
            lista.append(linha)
    print (lista)
    return (lista)
arq('Books_attend_grade.dat',3,'\t')
