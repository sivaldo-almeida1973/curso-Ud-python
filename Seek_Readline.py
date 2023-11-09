"""
Seek : movimenta o cursor pelo arquivo


arquivo = open('Lucros.txt')
print(arquivo.read())


print(arquivo.read())#se tentar imprimir novamente não vai conseguir
arquivo.seek(0) #mover o cursor para o iicio do arquivo
print(arquivo.read())


-------------------

arquivo = open('Lucros.txt')
arquivo.seek(5)#ler apartir da posicao 5
print(arquivo.read())


ReadLine-------------------------------------------

#ler linha por linha
arquivo = open('lucros.txt')
linha = arquivo.readline()
print(linha)

linha = arquivo.readline()
print(linha)


linha = arquivo.readline()
print(linha)

ReadLines -------------------------------------





"""
#imprime uma lista, em que cada elemento é uma linha do arquivo

arquivo = open('lucros.txt')
listaLinhas = arquivo.readlines()
print(listaLinhas)
