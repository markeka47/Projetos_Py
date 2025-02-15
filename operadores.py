# Operadores aritméticos

# Adição
print(1 + 1)

# Subtração
print(10 - 2)

# Multiplicação
print(4 * 3)

# Divisão (gera resultado do tipo float)
print(12 / 3)

# Divisão inteira (gera resultado do tipo inteiro)
print(12 // 3)

# Módulo (resto da divisão)
print(10 % 3)

#Exponenciação
print(2 ** 3)

# Exemplos de precedência matemática
print(10 - 5 * 2)

print((10 - 5) * 2)

print(10 ** 2 * 2)

print(10 ** (2 * 2))

print(10 / 2 * 4)

print(10 // 2 * 4)

# Operadores de Comparação

# Igualdade
saldo = 450
saque = 200

print(saldo == saque)

# Diferença
print(saldo != saque)

# Maior que / Maior ou igual
print(saldo > saque)

print(saldo >= saque)

# Menor que / Menor ou igual
print(saldo < saque)

print(saldo <= saque)

# Operadores de Atribuição

# Atribuição simples
saldo = 500

print(saldo)

# Atribuição com adição
saldo += 200

print(saldo)

# Atribuição com subtração
saldo -= 200

print(saldo)

# Atribuição com multiplicação
saldo *= 2

print(saldo)

# Atribuição com divisão
saldo /= 5

print(saldo)

# Atribuição com divisão inteira
saldo //= 5

print(saldo)

# Operadores Lógicos

# Exemplo
saldo = 1000
saque = 200
limite = 100

print(saldo >= limite)
print(saque <= limite)

# Operador E (and)
# verdadeiro / verdadeiro = True
# verdadeiro / falso = False   
print(saldo >= limite and saque <= limite)

# Operador OU (or)
print(saldo >= limite or saque <= limite)
# verdadeiro / verdadeiro = True
# verdadeiro / falso = True
# falso / verdadeiro = True
# falso / falso = False 

# Operador de Negação (not)

# Operador parênteses ()
# Segue a mesma regra da precedência matemática

# Operadores de identidade (is) e (is not = negação)
# Compara se dois objetos testados ocupam a mesma posição na memória
saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

# Operadores de associação (in) e (not in = negação)
# Utilizados para verificar se um objeto está presente em uma sequência
# Importante: operador é 'case sensitive', ou seja, busca exatamente a forma que o elemento está digitado
frutas = ['Limão', 'Uva']

print('uva' in frutas)

x = (22 - 10) * 3
print(x)


