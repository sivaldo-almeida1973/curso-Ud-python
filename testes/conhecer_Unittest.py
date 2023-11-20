"""
Unittest:

O que são?
-É um modulo para testar individualmente classes, funções, metodos....

Como Trabalhar :
-Inicialmente importa-se o módulo unittest e criamos classes que herdam TestCase(teste de caso) a partir desse módulo.Com isso é posssivel utilizar todos assertions contidos nele.
-Tabela com todos assertions presentes no módulo: https://docs.python.org/pt-br/3/library/unittest.html#assert-methods

Apresentada abaixo:


assertEqual(a, b) --->   a == b

assertNotEqual(a, b) --->  a != b

assertTrue(x) --->   bool(x) is True

assertFalse(x) --->   bool(x) is False

assertIs(a, b) --->  a is b

assertIsNot(a,   b) ---> a is not b

assertIsNone(x) ---> x is None

assertIsNotNone(x) --->  x is not None

assertIn(a, b) --->   a in b

assertNotIn(a, b) --->  a not in b

assertIsInstance(a, b) --->  isinstance(a, b)

assertNotIsInstance(a, b) ---> not isinstance(a, b)

#===============================Aplicando TDD==================================#=
#\Função que converte o padrão 24h para 12h

-EX:16:34 para 4:34 P.M



"""
def converte_padrao(hora, minuto):
  if hora >= 12:
    hora -= 12
    return f'{hora}:{minuto} P.M'
  return f'{hora}:{minuto} A.M'



#função que define se é Par ou Impar, caso for Par retorna True , se não retorna False

def par_impar(numero):
  if numero % 2 == 0:
    return True
  return False

#É conveniente desenvolver os testes em outro módulo separadamente.


