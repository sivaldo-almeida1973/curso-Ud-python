"""
Manipulando data e hora


#manipulando somente hora

jogo = datetime.time(16,0,0)
print(jogo)

#formatar data e hora: strftime()
#converter do formato americano para o brasil
horaAtual = datetime.datetime.now()
print(horaAtual)
horaAtual_BR = horaAtual.strftime('%d/%m/%Y')
horaAtual_BR = horaAtual.strftime('%d de %B de %Y')
print(horaAtual_BR)

#tabela de formatos do strftime:
#https://docs.python.org/3/library/datetime.html      # modulo-datetime


#================================================


# Dias da semana: weekday()
horaAtual = datetime.datetime.now()
print(horaAtual)
print(f"dia da semana",horaAtual.weekday())

fimSeculo = datetime.datetime(2100, 12,31,23,59,59)
print(fimSeculo)
print(fimSeculo.weekday())





"""

import datetime


#tempo de execução

import timeit

numQuadrado = str([x ** 2 for x in range(100000)])
print(timeit.timeit(numQuadrado, number=10000))