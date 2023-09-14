"""
fazer programa pra ler o codigo de uma peça 1, 
O numero de peças 1,
o valor unitario de cada peça 1.======
o codigo de uma peça 2,
o numero de uma peça 2
o valor unitario de uma peça 2
Calcule o total a ser pago
"""

print('===============Sistema de vendas=================')

print('--------------Peça 1----------------')

codigoPeca1 = int(input("Codigo P1: "))
QTDPeca1 = int(input("Quantidade peça 1: "))
valorUnitarioPeca1 = float(input('Valor UNT peça 1: '))



totalPeca1 = QTDPeca1 * valorUnitarioPeca1


print('--------------Peça 2-------------------')


codigoPeca2 = int(input("Codigo P2: "))
QTDPeca2 = int(input("Quantidade da peça 2: "))
valorUnitarioPeca2 = float(input('Valor UNT peça 2: '))

totalPeca2 = float( QTDPeca2 * valorUnitarioPeca2)

print('===============Total a Pagar=================')


totalPagar = float(totalPeca1 + totalPeca2)

print(f'total a ser pago {totalPagar}')