"""
Dicionarios

EX:
funcionario = {}
dict1 = {'nome':'Paula','idade':25, 'funcao':'Programador'}
dict2 = {'nome':'Antonio','idade':35, 'funcao':'Engenheiro'}

funcionario['Paula'] = dict1
funcionario['Antonio'] = dict2
print(funcionario)
print(funcionario['Paula']['nome'])

#Limpar dicionarios com o metodo clear():--------------

dicionario = {'Programar':"ideias"}
dicionario.clear()# apenas limpa , não apaga o dicionario
print(dicionario)

dicionario['Programar'] = 'ideias'
print(dicionario)


Deep Copy(copia profunda): copy():

dicionario = {'Programar':'ideias'}
novo = dicionario.copy() #novo sera uma copia de dicionario
novo['melhor'] = 'do mundo' # novo chave melhor valor: do mundo
print(f'Novo:',novo)
print(f'Dicionario:', dicionario)


#shallow Copy (copia superficial)====================

dicionario = {'Programar':'ideias'}
novo = dicionario
novo['melhor'] = 'do mundo'#nesse caso o que foi adicionado no novo tambem altera em dicionario
print(novo)
print(dicionario)

#Iterar dicionarios (desmembrar)=====================

personagem = {'nome': 'Mario', 'funcao':'programador', 'idade':35}

for item in personagem:
  print(f'chave:', item) #Retorna as chaves
for item in personagem:
  print(f'Dados:', personagem[item])#retorna os elementos

#Metodo Keys():------------------------------------

personagem = {'nome': 'Mario', 'funcao':'programador', 'idade':35}
print(personagem.keys()) # retorna uma lista com as cha


#Metodo values():=========================================


personagem = {'nome': 'Mario', 'funcao':'programador', 'idade':35}
print(personagem.values()) # retorna uma lista com os dados

#Metodo items():=========================================

personagem = {'nome': 'Mario', 'funcao':'programador', 'idade':35}
print(personagem.items()) # retorna uma lista de tuplas onde cada indice com chaves e dados
for item in personagem.items():
  print(item)

========================

#imprimir separados (desmembrar)
personagem = {'nome': 'Mario', 'funcao':'programador', 'idade':35}

for chave , dado in personagem.items(): #desmembrar 
  print(chave)
  print(dado)

#Metodo len() -------------------------------------------

personagem = {'nome': 'Mario', 'funcao':'programador', 'idade':35}

print(len(personagem))# qtd de indices


"""

#Max, Min, Sum  (trabalha com numeros)
dados = {'a':23,'b':45,'c':67}

print(max(dados.values()))# maior elemento ,tem que usar metodo values
print(min(dados.values()))# menor elemento
print(sum(dados.values()))# soma tudo