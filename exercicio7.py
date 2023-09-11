
n1 = 999
res = 0

while n1 != 99:
  n2 = n1
#eese loop realiza 999*n2, 998*n2, 997*n2
  while n2 != 99:
#eese loop realiza 999*n2, 998*n2, 997*n2,....até b2 = 0
    numero = str(n1 * n2)
    inverteNumero = numero[::-1]
    if inverteNumero == numero:
      num = int(numero)
      if res < num:
        res = num
        n2 -= 1
      else:
        n2 -= 1
    else:
      n2 -= 1
  n1 -= 1
print(res)

