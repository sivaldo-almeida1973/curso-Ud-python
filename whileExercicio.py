"""
While (enquanto)
executa enquanto for verdade
loop infinito, quando codigo não tem fim.
"""

nome = "sivaldo vieira"

indice = 0
novoNome = ""


while indice < len(nome):
  letra = nome[indice]
  novoNome += f"*{letra}"

  indice += 1

novoNome += "*"
print(novoNome)


