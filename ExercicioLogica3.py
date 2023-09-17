jogos = ["Mario Bros","Fifa ", "Pes 2023", "GTA", "GOW"] #jogos pra venda
precoVendas = [50,100, 150, 120, 80] #preços pra venda
precoEstoque = [30,60, 80, 70, 40] #preços de compra da fabrica
qtdEstoque = [3,6, 8, 7, 4] #quantidade disponivel estoque.
vendas = [] # vendas registrads
compraDeEstoque = [] # compras de estoque registradas


#menu interativo

op = 0

while op != 4:
  print("1 Registra venda\n2-Compra de estoque\n3-Resumo da loja\n4-Sair")
  op = int(input("Opção: "))


  if op == 1:
    jogoVendido = input("Jogo vendido: ")
    quantidadeVendida = int(input("Quantidade vendida: "))
    if quantidadeVendida <= qtdEstoque[jogos.index(jogoVendido)]:#testa se quantidade que o cliente deseja esta disponivel em estoque
      print(f"{jogoVendido} Vendido!")
      qtdEstoque[jogos.index(jogoVendido)] -= quantidadeVendida #remove do estoque quantidade vendida
      vendas.append(precoVendas[jogos.index(jogoVendido)]* quantidadeVendida)# adiciona na lista vendas o valor do jogo vendido
    else:
      print("\Não ha eesa quantidade disponivel em estoque")
  elif op == 2:
    jogoComprado = input("Jogo comprado")
    quantidadeComprada = int(input("Quantidade comprada"))
  









