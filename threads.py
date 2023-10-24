
# Função para verificar se um número é primo
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

# Função para imprimir os números primos entre 0 e N usando threads
def print_primes(N):
  # Verificar se N é válido
  if N <= 0:
    print("Digite um valor positivo para N")
    return

  # Importar o módulo threading
  import threading

  # Criar uma lista para armazenar os threads
  threads = []

  # Criar uma função para imprimir os números primos em uma faixa de dez valores
  def print_range(start, end):
    for i in range(start, end + 1):
      if is_prime(i):
        print(i, end=" ")

  # Dividir o intervalo entre 0 e N em faixas de dez valores e criar um thread para cada faixa
  for i in range(0, N + 1, 10):
    start = i
    end = min(i + 9, N)
    t = threading.Thread(target=print_range, args=(start, end))
    threads.append(t)
    t.start()

  # Esperar todos os threads terminarem
  for t in threads:
    t.join()

  # Imprimir uma quebra de linha
  print()

# Testar o algoritmo com um exemplo
N = int(input("Digite o valor de N: "))
print_primes(N)



