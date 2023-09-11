"""
While (enquanto)
executa enquanto for verdade
loop infinito, quando codigo não tem fim.
"""


qtdeLinhas = 5
qtdeColunas = 5

linha = 1
while linha <= qtdeLinhas:
  coluna = 1
  print(f"{linha=}")

  while coluna <= qtdeColunas:
    print(f"{linha=} {coluna=}")

    coluna += 1
  linha += 1


print("fora do loop")
