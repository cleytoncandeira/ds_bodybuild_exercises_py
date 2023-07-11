#Challenge da validação do cpf

while True: 
  cpf = input('Digite seu cpf: ')
  if cpf == 'sair':
    break

  cpf1 = cpf[:-2]

  contador = 11
  soma = 0

  #primeira conta 

  for x in cpf1:
    contador -= 1
    i = int(x)*contador 
    soma += i

  digito1 = 11-(soma % 11)
  if digito1 > 9:
    digito1 = 0

  digito1 = str(digito1)
  cpf1 = cpf1 + digito1 

  #segunda conta

  count = 12
  sum = 0

  for y in cpf1: 
    count -= 1
    h = int(y)*count
    sum += h

  digito2 = 11-(sum % 11)
  if digito2 > 9:
    digito2 = 0

  digito2 = str(digito2)
  cpf1 = cpf1 + digito2

  if cpf1 == cpf:
    print('Você digitou um cpf válido!')
    break

  else:
    print('Você não digitou um cpf válido!')
    print('Por favor, digite um CPF válido, ou digite "sair" para sair do programa!')