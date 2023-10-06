"""
Exercícios:
1 - Kiko precisa invadir uma prisão de segurança extremamente alta para
resgatar Jaiminho. Porém, existem 3 portões protegidos por senhas do TIPO
TUPLA. Cada portão oferece uma dica para descobrir a senha. A dica é
composta por uma tupla contendo algumas dezenas, e uma frase indicando
o processo a ser realizado. Kiko deve criar um programa que imprima na tela
as três senhas no seguinte formato: print(f'Portão X: {senha_do_portão_X}').

# Dicas
Portão 1 = (29, 54, 45) [Alterar todas as dezenas para 0]

Portão 2 = (12, 28, 37, 54) [A soma dos elementos 2 e 3 é o primeiro elemento
da senha, a soma dos elementos 1 e 4 é o segundo elemento da senha]

Portão 3 = (16, 86, 78, 32, 85, 12) [O valor mínimo é o primeiro elemento da
senha, o valor máximo é o segundo elemen
"""

portao1 = (29,54,25)
portao2 = (12,28,37,54)
portao3 = (16,86,78,32,85,12)


#portao1=====================================================
#converter tupla para lista , para poder alterar elementos
senha1 = list(portao1)
for id in range(0, 3): # 0,1,2
  senha1[id] = 0

#coverter para tupla novamente
portao1 = tuple(senha1)
print(f'Portão 1: {portao1}')

#Portão 2=====================================================

portao2 = (portao2[1] + portao2[2], portao2[0] + portao2[3]) 
print(f"Portão 2: {portao2}")

#portão 3===============================================

portao3 = (min(portao3), max(portao3))

print(f'Portao 3: {portao3}')

