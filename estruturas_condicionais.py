#Estruturas condicionais

# if / else / elif (elseif)

saldo = 2000.0
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
  print('Realizando saque!')

else:
  print('Saldo insuficiente')

opcao = int(input('Informe uma opção: [1] Sacar \n[2] Extrato: '))

if opcao == 1:
  valor = float(input('Informe a quantia para o saque: '))
elif opcao == 2:
  print('Exibindo o extrato...')
else:
  sys.exit('Opção inválida')  


MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
  print('Maior de idade! Pode tirar CNH.')
if idade < MAIOR_IDADE:
  print('Ainda não pode tirar CNH.')

if idade >= MAIOR_IDADE:
  print('Maior de idade! Pode tirar CNH.')
else:
  print('Ainda não pode tirar CNH.')

if idade >= MAIOR_IDADE:
  print('Maior de idade! Pode tirar CNH.')

elif idade == IDADE_ESPECIAL:
  print('Pode fazer as aulas teóricas, mas não as práticas.')

else:
  print('Ainda não pode tirar CNH.')

# if ternário