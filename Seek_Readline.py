"""
Seek : movimenta o cursor pelo arquivo


arquivo = open('Lucros.txt')
print(arquivo.read())


print(arquivo.read())#se tentar imprimir novamente não vai conseguir
arquivo.seek(0) #mover o cursor para o iicio do arquivo
print(arquivo.read())

ReadLine-------------------------------------------

"""


arquivo = open('Lucros.txt')
arquivo.seek(5)
print(arquivo.read())

