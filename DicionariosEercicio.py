
"""

Chegou o famoso dia dos namorados, Mateus deixou para decidir o presente em cima da hora.
Ele resolveu comprar um tipo de flor, um presente e escolher um lugar para saírem, ele anotou todas as opções abaixo:
           Flores
     Tipo	       Preço
Rosas Vermelhas	  145,00
Girassóis	      125,00
Margaridas	      120,00
Flores do campo	  140,00

          Presente
     Tipo	       Preço
Urso de Pelúcia	   55,00
Caixa de Bombom	   60,00
Colar	           75,00
Roupas	           40,00

           Lugar
      Tipo	         Preço
Praia	             70,00
Sair para jantar	150,00
Parque de diversões	120,00
Hotel	            180,00

- Crie um programa que descubra qual a combinação mais cara, em seguida mais barata e a média opção.
Imprima a combinação em cada caso.
- Use um dicionário para cada item (flor, lugar e presente).
"""

#Declaração dos dicionários

#primeiro criar o dicionario com 

flores = {'Rosas':145, 'Girassoi':125, 'Margarida':120, 'flores do Campo':140}
presentes = {'Uso de pelucia':55, 'Caixa Bombom':60, 'Colar':75, 'Roupas':40}
lugares = {'Praia':70, 'Jantar':150, 'Parque Diversão':120, 'Hotel':180}

#combinacao mas cara entres os dicionarios
#criar variaveis que irão receber os valores das combinacoes
precoTotal = 0
florCara = ''
presenteCaro = ''
lugarCaro = ''

flores = {'Rosas':145, 'Girassoi':125, 'Margarida':120, 'flores do Campo':140}
presentes = {'Uso de pelucia':55, 'Caixa Bombom':60, 'Colar':75, 'Roupas':40}
lugares = {'Praia':70, 'Jantar':150, 'Parque Diversão':120, 'Hotel':180}

#combinacao mas cara entres os dicionarios
#criar variaveis que irão receber os valores das combinacoes
precoTotal = 0
florCara = ''
presenteCaro = ''
lugarCaro = ''

for flor, valor in flores.items():
  for presente, preco in presentes.items():
    for lugar, custo in lugares.items():
      precoAtual = valor + preco + custo # recebe o preco atual de cada produto
      if precoAtual > precoTotal: #se preco atual for maior que precoTotal
        precoTotal = precoAtual #precoTotal recebe precoAtual
        florCara = flor # florCara recebe preco atual de flor do teste
        presenteCaro = presente #presenteCaro recebe preco atual de presente do teste
        lugarCaro = lugar   # lugarCaro recebe preco atual de lugar do teste

print(f'Custo total mas caro: {precoTotal} Flor: {florCara}, Presente: {presenteCaro}, lugar: {lugarCaro}')
      
#encontar a combinacao mas barata

aux = 0  #variavel para mostrar que o primeiro loop foi feito
precoTotal = 0
florBarata = ''
presenteBarato = ''
lugarBarato = ''


for flor, valor in flores.items():
  for presente, preco in presentes.items():
    for lugar, custo in lugares.items():
      if aux == 0: # sevre para reinicializar o loop
        precoTotal = valor + preco + custo
        aux += 1  # serve para não entrar mas nesse if
      else:
        precoAtual = valor + preco + custo
        if precoAtual < precoTotal: #se preco atual for maior que precoTotal
            precoTotal = precoAtual #precoTotal recebe precoAtual
            florBarata = flor # florCara recebe preco atual de flor do teste
            presenteBarato = presente #presenteCaro recebe preco atual de presente
            lugarBarato = lugar   #


print(f'Custo total Mas barato: {precoTotal} Flor: {florBarata}, Presente: {presenteBarato}, lugar: {lugarBarato}')
      
#Achando opção de preco media

precoTotal = 0 # resetando valor para zero
list = [] #criar lista vazia
#mesma iteração
for flor, valor in flores.items():
  for presente, preco in presentes.items():
    for lugar, custo in lugares.items():
      list.append(valor+preco+custo)  #adicionar valores na lista

list.sort()  #organiza em ordem crescente
precoTotal = list[len(list) // 2]

for flor, valor in flores.items():
  for presente, preco in presentes.items():
    for lugar, custo in lugares.items():
      if valor + preco + custo == precoTotal:
        print(f'Custo total: {precoTotal} Flor: {flor}, Presente: {presente}, lugar: {lugar}')
        





