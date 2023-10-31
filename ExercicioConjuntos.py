"""
Sami e Dudu irão fazer uma competição de quem visita mais Estados no Brasil em um período de 6 meses,
até então Dudu já visitou o Espírito Santo e São Paulo, enquanto Sami visitou Rio de Janeiro e Bahia.
Crie dois conjuntos diferentes para simbolizar os estados que cada um foi. Após 6 meses Dudu visitou Bahia,
Acre, Santa Catarina e Sergipe, enquanto Sami visitou Bahia, Minas Gerais, Amazonas e Paraná, atualize
cada um dos conjuntos com os novos Estados. Responda:
- Quais Estados Dudu visitou que Sami não foi?
- Quais Estados ambos foram?
- Sendo 27 Estados no Brasil todo, qual porcentagem o vencedor visitou?
"""

estadoSami = {'BA','RJ'}
estadoDudu = {'ES','SP'}

#esse loop substitui o Add ,para adicionar os novos estados visitados
sair = ''
while sair != 'nao':
  estadoSami.add(input('Qual estado Sami visitou a mais? '))
  sair = input('Tem mais estados para adicionar?') #se resposta for não,saira desse loop

#esse loop substitui o Add , para adicionar os novos estados visitados
sair = ''
while sair != 'nao':
  estadoDudu.add(input('Qual estado Dudu visitou a mais? '))
  sair = input('Tem mais estados para adicionar?') #se resposta for não,saira desse loop

#diferenca entre estados 
print(f'diferença',estadoDudu.difference(estadoSami))
#intersection entre estados 
print(f'interseccao',estadoDudu.intersection(estadoSami))
#Union entre estados 
print(f'Uniao',estadoDudu.union(estadoSami))

#quem vivitou mas estados
if len(estadoSami) > len(estadoDudu):
  print(f'Sami ganhou e visitou {len(estadoSami)*100// 27}%')
elif len(estadoDudu) > len(estadoSami):
  print(f'Dudu ganhou e visitou {len(estadoDudu)*100// 27}%')
else:
  print(f'Deu empate e ambos visitaram {len(estadoDudu)*100//27}%')


