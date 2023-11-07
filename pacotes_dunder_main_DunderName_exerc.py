"""
1_ crie uma pasta, uma subpasta em em seguida um modulo na subpasta contendo uma função qualquer.
Acesse o mdulo no programa principal e execute a função.

Obs: no modulo criado,estabeleça uma condição para a função ser acessada apenas se o modulo for importado e executado em outro. Ou seja, quando o modulo em questão não é o principal (main)
"""

#
from pacotefora.pacoteDentro.moduloDentro import preverFuturo
from random import choice as ch

idade = [27,44,66,77,44,33,22,23,19,49,55]
formacao = ['eng software', 'Programação', 'Advogado','Analista dados','medico','biologia']
trabalho = ['Analista senior', 'Programador','Juiz', 'delegado', 'Policial','medico']
pais = ['frança', 'Turquia','Israel','Portugal','italia','espanha']
animal = ['cachorro','Galo','Piriquito','arara','Tartaruga','coelho','gato']
nome = input('Digite um nome: ')

preverFuturo(nome,ch(idade), ch(formacao), ch(trabalho), ch(pais), ch(animal))
