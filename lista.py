"""
Listas - colecão de ados muito poderosa e importante,diferente de tudo que voce ja viu.
C - Vetores e matrizes: Apenas um tipo de dado, tamanho unico.

listas-São dinamicas:podem receber qualquer tipo de dado,
tamanho limitado á memória disponível do seu PC.

Sintaxe: [elelemneto1, elemento2, ......., elementoN]


lista1 = [] #lista vazia
lista2 = [1,2,3,4,5,6,7,8,9]# lista de inteiros
lista3 = [1.2,2.5,3.9,4.7]# lista de numeros reais
lista4 = [True, False, True, False]
lista5 = ["Tatu","Roxo","Camelo"]
lista6 = list("sivaldo vieira de almeida") #converte uma string para lista
lista7 = [43, True, "Abacate", "Russia", "X", [1,2,34]]
#print(lista6)
#print(lista7)


#criando lista com variaveis
cor = "azul"
animal = "Pavão"
numero = 42
lista8 = [cor, animal, numero]
print(f'lista=8:',lista8)

#Adicionar valores em listas; Append

print(lista2)
lista2.append(21)
lista2.append("flamengo")
lista2.append("Maracana")

print(f'lista=2:',lista2)

"""



#exemplo de declaração de listas:





#Adicionar valores em listas; extend


lista1 = [] #lista vazia
lista2 = [1,2,3,4,5,6,7,8,9]# lista de inteiros
lista3 = [1.2,2.5,3.9,4.7]# lista de numeros reais
lista4 = [True, False, True, False]
lista5 = ["Tatu","Roxo","Camelo"]
lista6 = list("sivaldo vieira de almeida") #converte uma string para lista
lista7 = [43, True, "Abacate", "Russia", "X", [1,2,34]]


lista5.extend(['Abacaxi','1.99', 'KG'])
print(lista5)

lista4.extend(12)

