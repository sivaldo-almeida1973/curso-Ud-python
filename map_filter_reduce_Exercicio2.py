"""
Realizar calculo do IMC atraves de uma funacao utilizando Map.com os dados abaixo, sobre peso e altura, e salvar os resultados em outra lista. apos isso, apicar o filter para separar pessoas obesas (imc > 25).

dados:
indice 0 das tuplas: peso (kg)
indice 1 das  tuplas :altura (m)
listaAmostras = [(62, 1.75),(90, 1.86),(76, 2.12),(54, 1.56),(69, 1.76),(112, 1.63),(98, 1.59),]

"""

#Map----------------------
listaAmostras = [(62, 1.75),(90, 1.86),(76, 2.12),(54, 1.56),(69, 1.76),(112, 1.63),(98, 1.59),]

def calculoIMC(amostra):
  imc = amostra[0] / (amostra[1] ** 2)
  return imc #retorna valor imc calculado

imc = map(calculoIMC, listaAmostras)#passar funcao e iteravel como parametros

resultadoIMC = list(imc) #converter imc para uma lista(imc)
resultIMC  = [] # lista vazio vai rceber

for num in resultadoIMC:
  resultIMC.append(round(num))  #round faz arredondamento valores da lista "resultadoIMC" e adiciona cada um na lista "resultIMC"

print(resultIMC)

#tirar duvudas se esta certo
print(62 / (1.75 ** 2))
print(87 / (1.70 ** 2))
print(80 / (1.75 ** 2))


#filter

#imc MAIOR QUE 25
#testa se os valores da lista "resultIMMC", são maiores do que 25
sobrepeso = filter(lambda imc: imc > 25, resultIMC)
print(f"sobrepeso acima 25:",(list(sobrepeso)))