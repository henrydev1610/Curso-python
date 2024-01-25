""" numerate numera cada item da sua lista desde que a lista esteja em algum laço de repetição ou dentro de um metodo list() """



lista = ['Carlos', 'Maria', 'Jonas']
lista.append('Carleano')

print(lista)

lista_enumerada = enumerate(lista)
print(list(lista_enumerada))

for i in lista_enumerada:
    print(i)