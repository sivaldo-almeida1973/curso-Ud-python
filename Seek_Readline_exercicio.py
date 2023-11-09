"""
Crie um arquivo com conteúdo aleatório,em seguida abra o arquivo,leia-o 3 vezes a partir dos caracteres 5,9,14.Por fim, feche o arquivo.
"""

#abrir arquivo
arqCores = open('arquivo.txt')

#mover o cursor para a 5º posição
arqCores.seek(5)
print(f'\n\n{arqCores.read()}')


#mover o cursor para a 9º posição
arqCores.seek(9)
print(f'\n\n{arqCores.read()}')

#mover o cursor para a 14º posição
arqCores.seek(14)
print(f'\n\n{arqCores.read()}')

#fechar arquivo
arqCores.close()
