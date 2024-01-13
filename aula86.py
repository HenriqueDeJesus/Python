# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# for chave, valor in produto.items():
#     print(chave, valor)

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}  

# dc = {
#     chave: valor
#     if isinstance(valor, (int, float)) else valor.upper()
#     for chave, valor 
#     in produto.items()
# }  

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

# dc = {
#     chave: valor 
#     for chave, valor in lista
# }

print(dict(lista))
print(dc)

# Set comprehenssiion
s1 = {2 ** i for i in range(10)}
print(s1)
print(set(range(10)))