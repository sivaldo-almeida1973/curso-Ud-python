"""
Operadores lógicos

and(e)  = todos as condicoes verdades

or(ou)  = 

not(não)
"""

entrada = input('[E]ntrar  [S]air: ')
senha_Digitada = input('Senha: ')


senha_Permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_Digitada == senha_Permitida:
  print('Entrar')
else:
  print('Sair')




