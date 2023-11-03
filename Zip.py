"""
Zip: 
Retorna um obj zip com elementos dos iteraveis passados como parametros.
-Pode receber qualquer tipo de iteravel


#exemplos 1 de Zip: 
# junta elementos de iteraveis diferentes ,de acordo com indices

alunos = ['bianca','vitor','ariel']

notas = (10,6,8)

juntarTudo = zip(alunos, notas)

print(type(juntarTudo))
print(juntarTudo)
#print(list(juntarTudo))#converte para lista
#print(dict(juntarTudo))#converte para dicionario
print(tuple(juntarTudo))#converte para dicionario


------------------------------------


#exemplos 2 de Zip: 
# junta elementos de iteraveis diferentes ,de acordo com indices

alunos = ['Bianca','Vitor','Ariel', 'Jose']
idade = (18,34,55,43, 9, 13)
cidade = {'Sao Paulo','Vitoria','Sao Luis'}#comnjunto não tem ordenacao
estado = {1:'SP', 2:'ES', 3:'RJ', 4:'MA'}

print(list(zip(alunos, idade, cidade, estado.values())))



"""
#exemplo 3 zip:
lugar = [('RS','Sao Paulo'),("PR", "Vitoria"),("AM", 'Sao Luiz')] #lista e tupla
print(list(zip(*lugar)))

#
