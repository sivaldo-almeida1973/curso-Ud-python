"""
Teste se um arquivo chamado livros.txt não exista pela abertura x, caso o arquivo ja exista abra com w+, utilize try/except nessa manipulação.Imprima na tela qual foi o modo de abertura,escreve no bloco o nome dos tres melhores livros que voce ja leu (um em cada linha) adicionando o arquivo, feche-o .Abra-o novamente e adicione mais um livro ao final do arquivo sem apaga-lo, por fim , leia a versão final.

"""
try:

  with open('Livros.txt','x')as arq:
    print("Abrimos no modo 'x'")
    arq.write('Geracao de valor')
    arq.write('\nOs segredo da mente milionaria')
    arq.write('\nO poder do habito')
except FileExistsError:
  with open('Livros.txt' ,'w+') as arq:
    print("Abrimos no modo 'w+'")
    arq.write('Geracao de valor')
    arq.write('\nOs segredo da mente milionaria')
    arq.write('\nO poder do habito')
#.Abra-o novamente e adicione mais um livro ao final do #arquivo sem apaga-lo, por fim , leia a versão final.
with open('Livros.txt', 'a+') as arq:
  arq.write('\nSherlock Holmes')
  arq.seek(0)
  print(arq.read())
