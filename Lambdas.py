"""
Lambdas são funcoes sem nome


============================

#EX de funcao normal

def pot(x,y):
  print(x ** y)# ao quadrado

pot(2,3)

#-----------------------------------
def pot(x,y):
  return x ** y# ao quadrado

print(pot(2,3))

=====================================


#Exemplo Lambda----------------
#na lambda tem que passar para uma variavel
pot = lambda x, y: x ** y

print(pot(3,2))

#mesmo resultado==================

pot = lambda x, y: print( x ** y)#podemos passar o print aqui tambem

pot(3,2)


========================================

cadastro = lambda nome, idade: f'Nome: {nome.title()}\nIdade:{idade}'

print(cadastro('lucas', 23))
print(cadastro('sivaldo', 35))
print(cadastro('Alice', 33))




"""

#Exemplo 3 lambda

segGrau = lambda a, b, c, x: a * x ** 2 + b * x + c  # raiz quadratica

print(segGrau(1,5,8,3))

#outro modo do mesmo exemplo=================

def quadratica(a,b,c):
  return lambda x:  a * x ** 2 + b * x + c

segGrau = quadratica(1,5,8)
print(segGrau(3))  # esse 3 é para x

