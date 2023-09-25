"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# def soma(x, y):
#     # Definição
#     print(x + y)

# print(soma)
# print(soma(1, 2))
# soma(1, 2)

# def soma(x, y):
#      # Definição
#      print(f'{x=} y={y}', '|', 'x + y = ', x + y)


# soma(1, 2)
# soma(2, 1)
# soma(y=2, x=1)

def soma(x, y, z):
     # Definição
     print(f'{x=} y={y} {z=}', '|', 'x + y + z= ', x + y + z)

#soma # Nome da função
soma(1, 2, 3)
soma(3, 2, 1)
soma(y=2, x=1, z=3)

soma(1, 2, z=5)
soma(1, y=2, z=5)
# soma(1, y=2, 5) Tem que nomear depois que passa o paranmetro


print(1, 2, 3, sep='-')
