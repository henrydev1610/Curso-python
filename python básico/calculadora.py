




while True:
    
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('digite o operador (+/*-)')
    
    
    numeros_validos = None
    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
        numeros_validos = True
        
    except:
        numeros_validos = None
        if numeros_validos is None:
            print('Um ou ambos os numeros são invalidos.')  
            continue  
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador nao permitido')
        continue
    print('confira o resltado ')
    if operador == '+':
        print(f'{num_1} + {num_2} = ',num_1 + num_2)
    elif operador == '-':
        print(f'{num_1} - {num_2} = ',num_1 - num_2)
    elif operador == '*':
        print(f'{num_1} * {num_2} = ',num_1 * num_2)    
    elif operador == '/':
        print(f'{num_1} / {num_2} = ',num_1 / num_2)
    else:
        print('nunca deveria ter chegado aqui')

    sair = input('quer sair? [s]im ').lower().startswith('s')
    if sair is True:
        break
    
    
    