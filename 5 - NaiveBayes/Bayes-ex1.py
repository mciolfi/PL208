def Bayes ():
    #Definição de valores iniciais e tamanho das matrizes
    #Yes = [25.2, 19.3, 18.5, 21.7, 20.1, 24.3, 22.8, 23.1, 19.8]
    #No = [27.3,30.1,17.4,29.5,15.1]
    name = ['Kate', 'Tom', 'Harry', 'Annika', 'Naomi', 'Joe', 'Chakotay', 'Neelix', 'Kes', 'B´Elanna']
    laptop = ['PC', 'PC', 'PC', 'Mac', 'Mac', 'Mac', 'Mac', 'Mac', 'PC', 'Mac']
    phone = ['Android','Android','Android','IPhone','Android','IPhone','IPhone','Android','IPhone','IPhone']
    android=0
    iphone=0
    #Se laptop = Mac, qual o telefone
    for i in range (len(laptop)):
        #Possibilidade de ser Android para Mac
        if laptop[i] == 'Mac' and phone[i] == 'Android':
            android = android + 1
        else:
            iphone = iphone + 1
    android = android/len(phone)
    iphone = iphone/len(phone)
    if android > iphone:
        print ('Pessoas com Laptop Mac possuem Android')
    else:
        print ('Pessoas com Laptop Mac possuem Iphone')
Bayes ()
