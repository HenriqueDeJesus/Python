# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy) é cópia raza
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Henrique Guilherme',
    'sobrenome': 'Jesus',
    # 'idade' : 900,
}

# print(len(pessoa))
# print(pessoa.__len__())

# print(pessoa.keys())
# print(tuple(pessoa.keys()))
# print(list(pessoa.keys()))
# for chave in pessoa.keys():
#     print(chave)

for chave in pessoa:
    print(chave)

print(list(pessoa.values()))
for valor in pessoa.values():
     print(valor)

# print(list(pessoa.items()))

# for chave, valor in pessoa.items():
#     print(chave, valor)

# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# d2 = d1 # o sinal de igual não copia o d1

# d2 = d1.copy()
# d2 = copy.copy(d1)
# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1)
# print(d2)

p1 = {
    'nome': 'Henrique',
    'sobrenome': 'Guilherme',
}

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem() # Não pode passsar valor deentro da chaves no popitem
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
tupla = ('nome', 'novo valor'), ('idade', 30) # Quando tiver apenas um item coloca a virgula no final dos parentes
# tupla = (('nome', 'novo valor'), ('idade', 30))
# p1.update((('nome', 'novo valor'), ('idade', 30)))
lista = [['nome', 'novo valor'], ['idade', 30]]
# p1.update(tupla)
p1.update(lista)
print(p1)