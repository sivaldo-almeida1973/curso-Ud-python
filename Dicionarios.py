"""
Sao apresentados por chaves {}
Qualquer tipo de dado
Nao ordenados. pelas chaves

declarar:
forma 1(mais usada)============================================

times_futebol = {'RJ':'Flamengo','SP':'Palmeiras'}

print(times_futebol)
print(type(times_futebol))


#===========================================================

times_futebol2 = {
  'RJ':'Flamengo',
  'SP':'Palmeiras',
  'SP':'Santos',
  'SP':'Corintians'
  
  }

print(times_futebol2)
print(type(times_futebol2))

#================================================================
# 2 usando comando dict()

times_futebol2 = {
  'RJ':'Flamengo',
  'SP':'Palmeiras',
  'SP':'Santos',
  'SP':'Corintians'
  
  }

print(times_futebol2)
print(type(times_futebol2))



#=============================================
# 3
time_futebol = {}.fromkeys('chave', 'dado')

print(time_futebol)


Sobre as chaves:
-dever ser unicas
-podem ser de qualquer tipo

Sobre dados;
-podem ser duplicados
-qualquer tipo


times_futebol  = {"RJ":'Flamengo', "SP":'Flamengo'}
print(times_futebol)

#nesse caso imprime so o segundo, pois não pode repetir a chave
times_futebol  = {"RJ":'Flamengo', "RJ":'Flamengo'}
print(times_futebol)

#Acessar elementos=========================================

times_futebol  = {"RJ":'Flamengo', "SP":'Flamengo'}
print(times_futebol)

print(times_futebol['RJ'])


# segunda maneira===============================================

times_futebol  = {"RJ":'Flamengo', "SP":'Flamengo'}
print(times_futebol)

print(times_futebol.get('BH'))# se não existir não dara erro com o get()



#=========================================

# 3 segunda maneira

times_futebol  = {"RJ":'Flamengo', "SP":'Flamengo'}
print(times_futebol)

print('BH' in times_futebol)
print('RJ' in times_futebol)

# None=
- é um tipo de dado sem tipo definido
- usado para declarar variaveis que voce ainda nao sabe o tipo que ira utilizar

EX:

dado = None
print(type(dado))

dado = 1
print(type(dado))


# Adicionar e alterar elementos================================
EX:
forma 1

sagas = {
  (1,2):"HP",
  (3,4):"PJ",
  (5,6):"JV",
  (7,8):"GG",
}
#adicionar
sagas[(9,10)] = "BR"

#alterar
sagas[(1,2)] = "Digimom"
print(sagas)


# forma 2 ==================================================

sagas = {
  (1,2):'HP',
  (3,4):'PJ',
  (4,6):'JV'
}

dado_novo = {(7,8) : 'MR'}

#ADICIONAR
sagas.update(dado_novo)
sagas.update({(1,2):'Digimon'}) #substituir elementos na chave 1,2 por digimon
print(dado_novo)
print(sagas)

# 1 Remover valores================================================

pokemon = {
  'Agua':'squirtle',
  'Fogo':'Chamander',
  'Grama':'Bulbassauro'
}


#Remover
print(pokemon)
pokemon.pop('Agua')

print(pokemon)



"""

pokemon = {
  'Agua':'squirtle',
  'Fogo':'Chamander',
  'Grama':'Bulbassauro'
}


#Remover==================================================
del pokemon['Agua']

print(pokemon)


