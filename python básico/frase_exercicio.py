frase = 'O python é uma linguagem de programação ' \
    'multiparadigma. ' \
    ' python criada por seu ze na esquid do bar o fabinho cachaceiro'
    

print(frase.lower().count('a'))    
    
    
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''


while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == '':
        i+= 1
    
    
    quantas_letras = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < quantas_letras:
        qtd_apareceu_mais_vezes = quantas_letras
        letra_apareceu_mais_vezes = letra_atual
    i += 1

    
    


print('A letra que apareceu mais vezes foi ' f"{letra_apareceu_mais_vezes} que apareceu " f'{qtd_apareceu_mais_vezes}X')
    
    
       
    