"""
**kwargs = gera um dicionario

#Exemplo 1:
def idades(**kwargs):
  for nome, idade in kwargs.items():
    print(f'A idade de {nome} é {idade}')

idades(maria=40, marcos=30, pedro=60) # passar chave e dado

"""

#Exemplo 2:
def jogadas(nome,**kwargs):
  print(kwargs)
  for jogada in kwargs:
    if kwargs[jogada] == 10:
      return f"{nome} ganhou"
  return f"{nome} perdeu!"

print(jogadas("Marcelo", j=16,j2=3,j3=45))
print(jogadas("Marcos", j=16,j2=3,j3=45,j4=10))
