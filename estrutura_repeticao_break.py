while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

# Expressão "% 2" - exibe somente numeros impares
#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
