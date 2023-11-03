"""
Exercicio:

"""
numeroInt = 1
listaNum = []

while numeroInt != 0: #se numerosInt for diferente de 0 , se for 0 sai
  numeroInt = int(input('Digite um numero inteiro: ')) #recebe do usuario e faz cast
  if numeroInt != 0: #numeroInt diferente de 0 
    listaNum.append(numeroInt)  #adiciona na listaNum

ordenada = sorted(listaNum)#ordena a lista
tamanho = len(listaNum)  #tamanho da lista

print(f'Maior valor: {ordenada[tamanho - 1]}') # O -1 é porque tamanho forma #quantidade de elementos na lista, ou seja , começando do 1 até o ultimo #elemento. mas os indices começam do 0,então ,o utlimo é o tamanho da lista -1.

invertdida = reversed(ordenada)#inverte a lista
listaInvertida = list(invertdida) #cria lista invertida

if tamanho % 2 == 1: #testa se valor da lista é impar ou pares
  print(f'Valor intermediario: {listaInvertida[tamanho // 2]}')
else:
  print(f'Valor Intermediario: '
        f'{(listaInvertida[tamanho // 2] + listaInvertida[(tamanho // 2) - 1])/2}')












