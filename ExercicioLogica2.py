print('------------Item 1--------------')

cod1 = int(input('cod1: '))
quantidade1 = int(input('qauntidade1: '))
preco1 = float(input('Preço1: '))

total1 = preco1 * quantidade1
print('------------total a Pagar item 1--------------')
print(f'{cod1} {quantidade1} {preco1} Total pagar {total1}',)

print('------------Item 2--------------')

cod2 = int(input('cod2: '))
quantidade2 = int(input('qauntidade2: '))
preco2 = float(input('Preço2: '))

total2 = preco2 * quantidade2

print('------------total a Pagar item 2--------------')
print(f'{cod2} {quantidade2} {preco2}Total Pagar {total2}')

print('------------Item 3--------------')

cod3 = int(input('cod3: '))
quantidade3 = int(input('qauntidade3: '))
preco3 = float(input('Preço3: '))


total3 = preco3 * quantidade3



print('------------total a Pagar item 3--------------')



print(f'{cod3} {quantidade3} {preco3} Total Pagar {total3}')

totalGeral = total1 + total2 + total3

print('------------Tota Geral--------------')
print(f'Tota geral {totalGeral}')