
"""
Exexrcicio
"""
#criar 4 listas -----------------

Nomes = ['Jessica','Bruno','Mateus','Ricardo','Maria']
provaCorrida = [2,7.7,9,8.67,6.8]
provaEscalada = [1,8,4,6.3,9.1]
provaNatacao = [0, 8.7, 5.8, 10, 4.3]

#lista vazia , vai receber nota total
listaNotas = []

#zipar as tres notas para cada participante
tabela = zip(provaCorrida, provaEscalada, provaNatacao)#agrupa as notas das 3 

#.fazer a soma das notas
for notas in tabela:
  listaNotas.append(sum(notas))#soma notas das 3 provas de cada um e coloca na lista 'listaNotas'.

#associar ao nome de cada um
tabelaFinal = zip(Nomes, listaNotas)# associa o nome de cadaparticipante com sua recpectiva nota final

#converter para dicionario
dicioFinal = dict(tabelaFinal)

vencedor = ''
pontos = 0

#iterar os itens do dicionario em chave e valor
for part, pts in dicioFinal.items():
  print(f'Participante : {part}, Pontos :{pts}')
  if pts > pontos: #verifica de qual nota é maior
    pontos = pts
    vencedor = part

print(f'\n-----Vencedor: {vencedor}, Pontos: {pontos}')