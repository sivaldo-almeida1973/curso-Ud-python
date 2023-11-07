"""
Criar um modulo customizado com duas funcoes(calculo de quant de num pares e impares em uma lsita qualquer).Em seguida, execute as funcões passando como argumento uma lista de num naturais.
"""

#Importando funções do outro modulo

from Mod_Cust_teste import contaPares as cp, contaImpares as ci

num = [4,5,6,7,8,9,12,33,44,55,21,11,44,22]


print(cp((num)))
print(ci(num))

