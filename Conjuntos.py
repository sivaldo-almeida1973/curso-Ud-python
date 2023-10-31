"""
Sets = (conjuntos)

Nao ordenados,
nao aceita repetir, 
Sao representados por Chaves{ não possui relacao chave -dado}

como declarar?=====================

conjunto = {1,2,3,4,5,6,6,6,6,6,6,7,8,} #aceitara apenas um num 6
print(conjunto)
print(type(conjunto))

===========================segunda forma declarar==================
list = [1,2,3,4]
conjunto = set(list)
print(conjunto)

------------------------conjuntos são iteraveis------------------------
pares = {2,3,4,5,8,6,7,8}
for num in pares :
  print(num)

Metodo in(dentro)--------------------------------------

nome = {'Ana','Bruno','Flavio'}
if 'Ana'in nome:
  print('Tem uma Ana')
else:
  print('Sumiu')

Adicionar-------------------------

esporte = {'futebol','volei','futsal'}
esporte.add('natacao')
print(esporte)

Remover-----------------------------

esporte = {'futebol','volei','futsal'}
esporte.remove('volei')
print(esporte)

----------------------------------
esporte = {'futebol','volei','futsal'}
esporte.discard('volei')
print(esporte)

--------------------------------
esporte = {'futebol','volei','futsal'}
esporte.pop() #remove o primeiro elemento
print(esporte)

-----------------------------------
#limpar 
conjunto = {1,2,3,4,5,6,7}
conjunto.clear()
print(conjunto)

====================================================
#Intersecçao de conjuntos  Intersection()
EX:
notaFabio = {5,6,7}
notaCalra = {5,8,7}
print(notaFabio.intersection(notaCalra))

==============================================
#Interseccao usando o & comparacao

notaFabio = {6,7,8}
notaClara = {6,7,8}
print(notaFabio & notaClara)


==================================
#Uniao conjunto ===================forma terceiro conjunto
notaFabio = {6,7,10}
notaClara = {6,7,8}
print(notaFabio.union(notaClara))

============================================
#Uniao conjunto ===================forma terceiro conjunto
notaFabio = {6,7,10}
notaClara = {6,7,8}
print(notaFabio | notaClara)#usando o -> ou

-------------------------------------------------
#diferença==========================
#Uniao conjunto ===================forma terceiro conjunto
notaFabio = {6,7,10}
notaClara = {6,7,8}
print(notaFabio.difference(notaClara))#usando o -> ou

===========================

conjunto = {'Brasil', 'Patria', 'Amada'}
conjuntoNovo = conjunto.copy()
conjuntoNovo.add('Russia')
print(conjunto)
print(conjuntoNovo)



"""

valores = {1,4,6,7,8,91,234,654,0}
print(max(valores))
print(min(valores))
print(sum(valores))

