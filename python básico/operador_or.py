entrada = input('[E]ntrar [S]sair ')
senha_digitada = input('dgite a senha: ')

senha_permitida = '123456'


if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('entrou')
else: 
    print('saiu')