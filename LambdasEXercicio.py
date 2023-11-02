"""
Criar duas listas de mesmo tamanho

"""
#Criar duas listas de mesmo tamanho

lista1 = [10,20,30,40,50,60,70,80,90,100]
lista2 = [110,120,130,140,150,160,170,180,190,217]
lista3 = []
lista2.reverse() #inverter os valores da lista2

#soma os elelmentos das listas Ex:elemento 0 (10) + elemento 0 (217)
soma = lambda lista1, lista2: [lista1[ind] +  lista2[ind] for ind in range(0,10)]
result = soma(lista2, lista2)
lista3.append(result)
print(lista3)