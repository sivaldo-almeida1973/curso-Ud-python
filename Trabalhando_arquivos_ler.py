"""
Leitura de arquivos

#abrir um arquivo
#Função Open:Recebe como parametro obrigatorio o endereço em que se encontra o arquivo.
#obs:a abertura padrão é do modo leitura(mode 'r' - read)

arquivo = open('Lucros.txt')
print(arquivo)


#<_io.TextIOWrapper name='Lucros.txt' mode='r' encoding='cp1252'>

#ler arquivo funcao(read)
print(arquivo.read())


arq = arquivo.read()
print(type(arq)) #tipo string

--------------------------------------------------------
#outro modo leitura-------------------


arquivo = open('Lucros.txt')

print(arquivo.read(20))#qtd de caracter que vai imprimir

------------------------------------------------------------------

#fechar um arquivo funcao close()

arquivo = open('Lucros.txt')

print(arquivo.closed) #verifica se esta fechado (true ou false)
arquivo.close()#finaliza conexao entre o arquivo e vs code(streaming)
print(arquivo.closed)


print(arquivo.read())#se ler depois de fechado: ValueError: I/O operation on closed file.


"""


#Modo pythonico de trabalhar com arquivos.

with open('Lucros.txt') as luc:
  print(luc.read())

#se tentar ler novamente tera um erro
#depois que sai do bloco with fecha novamente
print(luc.read()) #ValueError: I/O operation on closed file.
