"""
criar duas listas:
uma do carrinho do supermercado que ira receber produtos comprados
outra para preço dos produtos.
utilizando um loop.
preencha as listas com 5 produtos e 5 preços

"""

listaCarrinho = [] # cirando a lista que vai receber os produtos
listaPreços = []  #criando a lista que vai receber os preços
contaProdutos = 0 #Criação de variaveis
valorTotal = 0 
produto = ''

while contaProdutos < 5:#loop para acrescentar 5 itens nas listas
  produto = input('Produto: ')
  listaCarrinho.append(produto) # adicionando elelmento a lista
  preco = float(input('Preço:'))# casting
  listaPreços.append(preco)
  contaProdutos += 1

for id in range(0, 5):# 0,1,2,3,4
  valorTotal += listaPreços[id]#somando todos os elementos  da lista

#obs: o acesso aos elementos está sendo acessado via indice.a variavel id terá os valores 0,1,2,3,4 de acordo com o range(0,5)
#portanto por baixo dos panos, o loop esta realizando o seguinte:
#listaPrecos[0] + listaPrecos[1] + listaPrecos[2] + listaPrecos[3] + listaPrecos[4]

print(f'Produto comprados:{listaCarrinho}')
print(f'Valor tota: R${valorTotal}')
