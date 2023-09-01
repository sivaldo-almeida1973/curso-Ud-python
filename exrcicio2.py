primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro = int(primeiro_valor)
int_segundo  = int(segundo_valor)

if int_primeiro > int_segundo:
  print(f'Primeiro valor {int_primeiro} é maior que segundo valor {int_segundo}')
elif int_segundo > int_primeiro:
  print(f'Segundo valor {int_segundo} é maior que primeiro valor {int_primeiro}!')
else:
  print(f'Valores digitados {int_primeiro} e {int_segundo} São iguais!')

