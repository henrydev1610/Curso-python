carros = ['hrv', 'golf', 'fusca']
marcas = ['honda', 'volvo', 'wolkvagen']

animais = ['gato', 'cachorro', 'vaca', 'cavalo', 'galinha']
selvagem = ['leão', 'tigre', 'elefante']


animais.insert(2, selvagem)
animais.extend(selvagem)
animais.remove('gato') 
""" .remove serve para remover apenas o indice x ou seja. o nome. se precsar remover varios da erro """

animais.pop(3)
""" .pop remove indice especific em uma lista sem o indice declarado ele remove o ultimo elemento da lista"""


animais.clear()
""" este método é o mais radical, onde excluimos todos os elementos de uma lista. voce pode utilizar em programas maiores para garantit que uma determinada lista seja esvaziada. seria equivalente ao delete. """


carros.append('fit')
carros.append('ferrari')
carros.append(marcas)


print('lista atalizada: ', carros)
print(animais) 


