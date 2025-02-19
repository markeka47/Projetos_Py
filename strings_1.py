curso = "Python"

# MAIÚSCULA
print(curso.upper())

# MINÚSCULA
print(curso.lower())

# TÍTULO
print(curso.title())

# Remover espaços em branco esquerda/direita
print(curso.strip())

# Remover espaços à esquerda
print(curso.lstrip())

# Remover espaços à direita
# + "." - adiciona ponto final à string
print(curso.rstrip() + ".")

# Centralizar elementos
# "10" - Quantidade de caracteres / "#" Caractere fantasma
print(curso.center(10, "#"))

# Junção - insere caracter a cada item da string
print(".".join(curso))

