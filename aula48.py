"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índice e fatiameento
Métodos úteeeis: append, insertm pop, del, clear,extend, +
"""
#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
#print(bool([])) # falsy
#print(lista, type(lista))
# list cria uma lista tambem que nem []
#         0     1      2         3    4
#        -5    -4     -3        -2   -1
lista = [123, True, 'Henrique', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
print(lista[2].upper(), type(lista[2]))
