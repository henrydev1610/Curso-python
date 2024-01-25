nome  = input('digite seu nome: ')
altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
imc = peso / (altura * altura)

print(f'ola {nome}, seu imc é: {imc:.2f}')


## quando quiser formatar uma string, sempre coloque f. O F servira para avisar que tem uma formatação, e envolva as variáveis com chaves.