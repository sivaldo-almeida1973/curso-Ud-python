"""
Forma limpar e analisar todos os problemas no seu codigo.
Obs: Na pratica usar o print para tratar erros aos poucos ao longo do codigo áuma pratica ruim.


#EX:
def boasVindas(nome):
  print(nome)  #apenass para verificar se variavel esta correta
  print(f'Seja bem vindo/a {nome}')

boasVindas('Sivaldo')


----------------------------------------------------------------

#Forma profissional/Pythonica de corrigir erros:
A)PDB: Python Debugger
  - Para usar , devemos importar uma bibliotec: PDB -Funcao: set_Trace()

1) l(list) : apresenta onde esta no codigo
2)n(next): Pular para proxima linha
3) p(print): imprime uma variavel
4)c(continiue): continua execucao do codigo até o final do programa ou prox set_Trace()
==============================================================          
obs: evitar usar letras no codigo indenticas a ->( l,n,c,p)

import pdb

x = 2
y = 3
pdb.set_trace()
z = x * y
nome = 'clara'
frase = nome * z
print(fr

#========================================A partir da versao 3.7 do python não precsa importar pdb, foi incorporada aos Built-in com o nome breakpoint()


x = 2
y = 3
z = x * y
nome = 'clara'
frase = nome * z
print(frase)



===============================


"""


x = 2
y = 3
breakpoint()
z = x * y
nome = 'clara'
frase = nome * z
print(frase)
