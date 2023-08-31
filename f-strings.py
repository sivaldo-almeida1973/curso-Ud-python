nome = 'sivaldo vieira'
altura = 1.70000
peso = 86
imc = peso/(altura * altura)


linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'peso:{peso} quilos e seu imc é: '
linha_3 = f'{imc:.2f} '
print(linha_1)
print(linha_2)
print(linha_3)

print('=='*10)
#formatação de strings

print(f'Seu nome é: {nome}')
print(f'O seu peso é {peso}KG e sua altura é {altura:.2f}M por isso seu imc é: {imc}')