


def desmembraIteravel(iteravel):
  iterador = iter(iteravel)  #converter  para iterador e, evitar erro
  while True:
    try:
      print(next(iterador))
    except StopIteration:  #tratar erro ao chegar no final da lista
      print('Chegamos ao ultimo elemento')
      break

desmembraIteravel([1,2,3,4,5,6,7,8,9])