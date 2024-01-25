""" variavel = 'ola mundo'

print(variavel[4:8]) """


nome = input('Escreva seu nome: ')
idade = input('digite sua idade: ')


if nome and idade:
    print(f'seu nome é: {nome}')
    print(f'seu nome invertido é: {nome[::-1]}')
    
    if ' ' in nome:
        print('seu nome contem espaços')
    else:
        print('seu nome não contem espaços')
        
        
    print(f'seu nome tem {len(nome)} de letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'a ultima letra do seu nome é: {nome[-1]} ')
else:
    print('dados inseridos incorretamente')
