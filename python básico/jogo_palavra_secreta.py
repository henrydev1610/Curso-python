



palavra_secreta = 'galinha'
letras_acertadas = ''
numero_tentativas  = 0 
while True:
   
    letra_digitada = input('digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('digite epenas uma letra')
        continue
  
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada +='*'
    print('Palavra formada',palavra_formada)
               
    if palavra_formada == palavra_secreta:
        
        print('VC GANHOU!!!')
        print('A PALAVRA ERA: ', palavra_formada)
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
