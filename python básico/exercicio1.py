"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
""" try:
    entrada  = int(input('digite um numero inteiro: '))
    par_impar = entrada %2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
        
        
    print(f'O numero {entrada} é {par_impar_texto}')    
except:
    print('voce escreveu um numero inteiro')
 """

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
 


""" try: 
    
        
    hora = float( input('olá, pode me dizer qui horas são? '))

    manha = hora <= 11
    tarde = hora >= 12 and hora <=17
    noite = hora >= 18 and hora <=23
    
    if manha:
        print(f'bom dia, são {hora} horas')
    if tarde:
        print(f'boa tarde, são {hora} horas') 
    if noite:
        print(f'boa noite, são {hora} horas ')       

except:
    print('digite uma hora decente')
 """




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Digite seu nome: ')
name = len(entrada)

if name <= 4:
    print('seu nome é curto')
elif name>=5 and name <= 6: 
    print('seu nome é muito normal ')        
elif name >= 6:
    print('seu nome é muito grande')
else:
    print('insira um nome decente')
    

