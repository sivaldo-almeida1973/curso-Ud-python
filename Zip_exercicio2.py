#criar ters listas
companhias = ['Gol','Latam','Azul']
voo1 = [115,95,110]
voo2 = [195,88,225]

#zipar o numero de passageiros em cada voo
voos1e2 = zip(voo1, voo2)# junta os num de passag de cada companhia
maxPass = map(lambda voos: max(voos), voos1e2)#determ valor max de passag por companhia entre os voos 1 e 2
listaMaxPass = list(maxPass ) #converter para lista


#zip 
compMax = zip(companhias, listaMaxPass) #associar cada companhia ao num max passag
listaCompMax = list(compMax)#converter para lista



umaEst = list(filter(lambda valMax: valMax[1] < 100, listaCompMax))#filtra a companhia aerea que tem - 100 passag em seu valor maximo e converte para lista

duasEst = list(filter(lambda valMax: valMax[1] > 100 and valMax[1] <= 200, listaCompMax))#filtra a companhia aerea que tem +100 e 200 passag em seu valor maximo e converte para lista

tresEst = list(filter(lambda valMax: valMax[1] > 200 and valMax[1] <= 300, listaCompMax))#filtra a companhia aerea que tem + de 200 e  - 300 passag em seu valor maximo e converte para lista


print(f'Uma estrela: {umaEst[0][0]} - Max Passageiros : {umaEst[0][1]}')
print(f'Duas Estrela: {duasEst[0][0]} Max Passageiros: {duasEst[0][1]}')
print(f'Tres Estrela: {tresEst[0][0]} Max Passageiros: {tresEst[0][1]}')
