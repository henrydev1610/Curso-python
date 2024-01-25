""" senha = '123456'
senha_degitada = ''
repeticoes = 0


while senha_degitada != senha:
    senha_degitada = input(f'sua senha {senha_degitada}x:')
    repeticoes +=1
    
    
print(repeticoes)
print('aquele laco acima pode ter inumeras repeticoes')    
    


 """

texto = 'faiz uh eli'
novo_texto = ''

for letra in texto:
    
    novo_texto += f'*{letra}'
    print(letra)
    
print(novo_texto) 