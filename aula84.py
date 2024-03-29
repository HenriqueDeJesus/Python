# List comprehension em Python
# List comprehension é uma forma para criar listas 
# a partir de iteráveis
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista2 = [
    numero
    for numero in range(10)
]
print(lista2)

lista3 = [
    numero * 2
    for numero in range(10)
]
print(lista3)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
# novos_produtos = [
#     produto
#     for produto in produtos
# ]

# novos_produtos = [
#     {'nome': produto['nome'], 'preco': produto['preco']}
#     for produto in produtos
# ]

# novos_produtos = [
#     {**produto, 'preco':produto['preco']* 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

# lista = [n for n in range(10) if n < 5] # Filtro
# print(lista)

novos_produtos = [
    {**produto, 'preco':produto['preco']* 1.05}
    if produto['preco'] > 20 else {**produto} # Mapeamento
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 # Filtro
]