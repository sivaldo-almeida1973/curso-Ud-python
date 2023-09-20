jogos = ["Mario Bros","Fifa", "Pes 2023", "GTA", "GOW"] #jogos pra venda
precoVendas = [50,100, 150, 120, 80] #preços pra venda
precoEstoque = [30,60, 80, 70, 40] #preços de compra da fabrica
quantidade = [3,6, 8, 7, 4] #quantidade disponivel estoque.
vendas = [] # vendas registrads
compraDeEstoque = [] # compras de estoque registradas

#menu interativo
op = 0

while op != 4:
  print("1-Registrar venda\n2-Compra de estoque\n3-Resumo da loja\n4-Sair")
  op = int(input("Opção: "))

  if op == 1:
    jogoVendido = input("Jogo vendido: ")
    quantidadeVendida = int(input("Quantidade vendida: "))
    if quantidadeVendida <= quantidade[jogos.index(jogoVendido)]:#testa se quantidade que o cliente deseja esta disponivel em estoque. jogos.index(jogoVendido)retorna o indice #do jogo escolhido na lista 'jogos' pra verificar seu preco na lista 'precoVenda'
      print(f"\n{jogoVendido} Vendido!")
      quantidade[jogos.index(jogoVendido)] -= quantidadeVendida #remove do estoque #quantidade vendida
      vendas.append(precoVendas[jogos.index(jogoVendido)]* quantidadeVendida)# adiciona #na lista vendas o valor do jogo vendido,encontrado em precosVenda[jogos.index(jogoVendido)]
    else:
      print("\nNão ha essa quantidade disponivel em estoque!!\n")#caso não houver a qdt dispon.

#compra de estoque===================================================================
  elif op == 2:
    jogoComprado = input("Jogo comprado: ")
    quantidadeComprada = int(input("Quantidade comprada: "))
    print(f"\n{jogoComprado} comprado")
    quantidade[jogos.index(jogoComprado)] += quantidadeComprada #adiciona ao estoque qtd #quantidade comprado na fabrica.
    compraDeEstoque.append(precoEstoque[jogos.index(jogoComprado)] * quantidadeComprada)
    #adiciona a lista o valor do jogo copmrado

  elif op == 3:
    print("\n\nQuantidade de jogos em estoque: ")
    for jogo in jogos:
      print(f"{jogo}: {quantidade[jogos.index(jogo)]}")#apresenta a lista de jogos e a #qtd disponível.
#apresentar os lucros ==============================================================
    print(f"Lucros: R${sum(vendas)}")#soma dos valore da lista "vendas"
    print(f"Despesas:R${sum(compraDeEstoque)}")#soma dos valores da lista "copmraEstoque"
    print(f"Caixa: R${sum(vendas) - sum(compraDeEstoque)}\n")#determina3 a receita total da #loja pela subtração dos lucros pelas despesas.
print("\n\nCaixa fechado!")












  









