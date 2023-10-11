def Cadastro():
  list = []
  for i in range(4):
    dicionario = dict(nome = input("Digite seu nome: "),
                      sexo = input("Digite M para masculino e F para feminino: "),
                      esporte = input("Escolha seu esporte favorito entre natacao, futebol, volei , tenis :"), 
                      idade = int(input("Digite sua idade:")))
    list.append(dicionario)
  return list

def aviso():
  print('Não tem homens que gostam de natacão')


lista = Cadastro()
cont = 0
soma = 0


for i in range(4):
  if lista[i]['sexo'] == 'M' and lista[i]["esporte"] == "natacao":
    soma = soma + lista[i]['idade']
    cont += 1
if cont == 0:
  aviso()
else:
  media = soma / cont
  print(f"A idade media de homens que gostam de natação é {media} ")