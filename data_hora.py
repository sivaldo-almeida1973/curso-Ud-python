"""
Data e hora

-É utilizado o modulo integrado Datetime
-o formato padrão de data americano: aaaa/mm/dd


horario = datetime.datetime.now() # É possivel trabalhar com o fuso horario

print(horario)
print(type(horario))


horario = datetime.datetime.today() 

print(horario)
print(type(horario))


====================================================
#Constantes

print(repr(datetime.datetime.now()))
print(dir(datetime))

print(datetime.MAXYEAR) #constante
print(datetime.MINYEAR)

#==========================================================
horAtual = datetime.datetime.now()
print(horAtual)

print(horAtual.year)
print(horAtual.month)
print(horAtual.day)
print(horAtual.hour)
print(horAtual.minute)
print(horAtual.second)
print(horAtual.microsecond)

#=====================================================

# alterando hora atual (replace)

horaAtual = datetime.datetime.now()
print(horaAtual)
horaAtual = horaAtual.replace(year=1500,month=4,day=22,hour=10,minute=30,second=0,microsecond=0)

print(horaAtual)

#=================================================
dataUsuario = input('Escolha uma data (dd/mm/aaaa): ')
dataUsuario = dataUsuario.split('/')
print(dataUsuario)
dataUsuario = datetime.datetime(int(dataUsuario[2]) , int(dataUsuario[1]), int(dataUsuario[0]))

print(dataUsuario)

#=============================================

#Delta de data e hora

horaAtual = datetime.datetime.now()
fimSeculo = datetime.datetime(2100,12,31,23,59,59)
tempRestante = fimSeculo - horaAtual
print(tempRestante)
print(f'Restam {tempRestante.days} dias  para virar o século!')
print(f'Restam {tempRestante.days / 365:.0f} anos  para virar o século!')

#=======================================================

#Delta de data e hora

horaAtual = datetime.datetime.now()
print(horaAtual)
tempoTrabalho = datetime.timedelta(30) #30 dias
primeiroSalario = horaAtual + tempoTrabalho
print(primeiroSalario)

"""

import datetime

#Delta de data e hora

horaAtual = datetime.datetime.now()
print(horaAtual)
tempoTrabalho = datetime.timedelta(30) #30 dias
primeiroSalario = horaAtual + tempoTrabalho
print(primeiroSalario)