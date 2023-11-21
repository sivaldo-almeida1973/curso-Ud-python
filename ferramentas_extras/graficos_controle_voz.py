import matplotlib.pyplot as grafico

import statistcs

pontuacao = [7,11,10,10,9,12,10,14,18,21,24,19,24,18,11,16,12,31,38,41,45,53,55]

medias = []
soma = []

for num in pontucao:
  soma.append(num)
  medias.append(statistics.mean(soma))


grafico.ylabel('pontuacao')
grafico.xlabel('geracao')
                        
grafico.plot(pontuação, 'b', medias,'r--')

grafico.show()