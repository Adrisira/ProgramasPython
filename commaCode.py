spam = ['apples', 'bannas', 'tofu', 'cats']


def parseo(lista: list):
    fraseADevolver = ''
    for i in range(len(lista)):
        if(i == 0):
            fraseADevolver += "'"
            fraseADevolver += lista[i] + ', '
        elif(i == len(lista) - 1):
            fraseADevolver += lista[i]
            fraseADevolver += "'"
        else:
            fraseADevolver += lista[i] + ', '
    print(fraseADevolver)



    
parseo(spam)