"""
Tipos erros mais comuns em Python

A) AttributeError: quando há falha de atribuição

EX:------------------------------------------------

dicionario = {'SP':"São Paulo",'RJ':"Rio Janeiro"}
dicionario.add('ES')
print(dicionario)

---------------------------------------------------

#Ex: IndexError

lista = [1,2,3,4,5]
print(lista[3])
print(lista[6])

----------------------------------------------------

#KeyError: 

dicionario = {'SP':"São Paulo",'RJ':"Rio Janeiro",}

print(dicionario ["RJ"] )
print(dicionario ["MG"] ) #chave MG não existe
--------------------------------------------------

# NameError : variavel ou funcao não existe no codigo

EX:
#NameError: name 'programar' is not defined
print(programar)

EX:

x()  funcao não existe ou não esta definida

--------------------------------------------------

#SintaxeError :

variavel =
10
break 100
def variavel = 5

#SyntaxError: invalid syntax

-----------------------------------------
#IndentationError: erro de indentação
x = 10
if x == 10:
x = 5

------------------------------------------
TypeError: Operacao com tipos incorretos

nome = "marc"
num = 10
nome_num = nome + num

---------------------------

#ValueError: ValueError: invalid literal for int() with base 10: 'a'

"""

valor = int(input('digite um numero inteiro:' ))
print(valor)

#se digitar letras : dara esse erro pois a função int() esta recebendo um parametro #de tipo certo (str), porem ,o valor dentro dela não,pois deve ser um numero #interio e não uma letra