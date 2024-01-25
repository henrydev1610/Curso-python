""" Não usar else no while """



string =  'valor qualquer'

i = 0

while i < len(string):
    letra = string[i]
    print(letra)

    
    i +=1
    
else:
    print(' O else foi executado')    
    print('else executado de novo')