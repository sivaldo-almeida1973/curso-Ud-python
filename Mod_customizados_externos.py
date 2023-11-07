"""
Modulos customizados externos

# importar modulo criado por nós (customizado)
import Mod_teste


Mod_teste.imparPar(80)
Mod_teste.imparPar(81)

print(Mod_teste.lista)
for num in Mod_teste.lista:
  print(num * 10)


==================================================================

#Modulos externos:Da internet
#obs: deixa codigo mais visivel, organizado e acessivel.

#todos os modulos oficias extrenos podem ser encontardos em : https://pypi.org/



"""

#colorama
from colorama import init
init()



from colorama import Fore, Back
print(Fore.RED + 'Sou o deadpool')
print(Fore.BLACK + 'Sou o deadpool')
print(Back.GREEN + 'Sou Hulk')


