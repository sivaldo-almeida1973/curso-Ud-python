"""

import matplotlib.pyplot as grafico

import statistics

pontuacao = [7,11,10,10,9,12,10,14,18,21,24,19,24,18,11,16,12,31,38,41,45,53,55]

medias = []
soma = []

for num in pontuacao:
  soma.append(num)
  medias.append(statistics.mean(soma))


grafico.ylabel('pontuacao')
grafico.xlabel('geracao')
grafico.axis([0,25,5,60])                     
grafico.plot(pontuacao, 'g', medias,'r--')
#grafico.savefig('teste.png')#criar uu arquivo e salva o grafico
grafico.show()

#==============grafico Pizza========================= 

import matplotlib.pyplot as grafico

gols = [55,48,46,12,61,87]
jogadores = ['Messi','CR7','Neymar','Hazard','De bruyne', 'Gabigol']

#grafico.pie(gols, labels=jogadores)
grafico.pie(gols, labels=jogadores, autopct='%1.1f%%')
grafico.legend()
grafico.show()


"""



#Grafico de pizza
