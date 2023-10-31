"""Dicionarios

Quando usar?
-quando voce possui conjuntos de informacoes de um objeto ou pessoas

EX:
paula, 27, Programadora
Gabriel, 30, Engenheiro


#EX Listas------------------------- :
func = []
lista1 = ["Paula", 27,"Programadora"]
lista2 = ["Gabriel", 30,"Engenheiro"]
func.append(lista1)
func.append(lista2)

print(func)
print(func[0][1])


#EX Tuplas------------------------- :

tuple1 = ("Paula", 25, "Programadora")
tuple2 = ("Grabiel", 30, "Engenheiro")
funcionarios = (tuple1, tuple2)
print(funcionarios[0][1])
"""


#EX Dicionario------------------
#funcionario = []
funcionario = {}
dict1 = {"Nome":"Paula", "idade":27, "Funcao":"Programadora"}
dict2 = {"Nome":"Gabriel", "idade":30, "Funcao":"Engenheiro"}

#funcionario.append(dict1)
#funcionario.append(dict2)
#print(funcionario[0]["idade"])

funcionario['Paula'] = dict1
funcionario['Gabriel'] = dict2
#print(funcionario)
print(funcionario['Paula'] ['idade'])