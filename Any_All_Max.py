"""
Any -= retorna True se qualquer elemento do iteravel for True
#Obs: neste caso , um iteravel vazio false:

#numeros inteiros no python são True
print(any([1,2,3,4,5,6,7,8,9])) #True
print(any('Programando ideias'))#true
print(any([0, False, {}, [], ()])) #False
print(any([0, False, {}, [], (), 1])) #True


#============================
numeros = [1,2,3,4,5,6]
#verificar se resto do valor dividido por 5 é igual a 0
print(list(num % 5 == 0 for num in numeros)) #coverter para lista o resultado
print(any(num % 5 == 0 for num in numeros))# se tiver ao menos um verdade sera verdade

-------------------------------------------------------------------
All: retorna true se todos os elementos do iteravel forem true 
#obs: neste caso , um iteravel vazio retorna true

#numeros inteiros no python são True
print(all([1,2,3,4,5,6,7,8,9])) #True
print(all('Programando ideias'))#true
print(all([0, False, {}, [], ()])) #False
print(all([0, False, {}, [], (), 1])) #false
print(all([])) #true



numeros = [2,3,5,6,8,10]
print(list(num % 2 == 0 for num in numeros))
print(all(num % 2 == 0 for num in numeros))#false


-------------------------------------------------------------------
Max

#Ex: Max -maior valor de um iteravel

num = [1,2,3,4,5,6,7,8,9]
print(max(num))

#outra maneira
print(max( [1,2,3,4,5,6,7,8,9]))


cores = {'azul':2, 'vermelho':5, 'yellow':3}
print(max(cores.values())) #ira retornar maior indice do dicionario
print(max(cores)) #ira retornar palavra com letra alfabeto mais proximo fim


-------------------------------------------------------------------
Min: menor elemento dos iteraveis

num = [1,2,3,4,5,6,7,8,9]
print(min(num))

#outra maneira
print(min( [1,2,3,4,5,6,7,8,9]))


cores = {'azul':2, 'vermelho':5, 'yellow':3}
print(min(cores.values())) #ira retornar maior indice do dicionario
print(min(cores)) #ira retornar ordem alfabeto




"""

alunos = [ 'xaximiliano','jose','guti','sivaldo','francisco']

print(max(alunos))
print(min(alunos))

#pagar o maior nome e o menor

print(max(alunos, key=lambda aluno: len(aluno)))
print(min(alunos, key=lambda aluno: len(aluno)))