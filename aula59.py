# Desempacotamento em chamadas 
# de métodos e funções
string = 'ABCD'
lista = ['Marila', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena',], # 0
    # 0
    ['Elaine',], # 1
    # 0       1       2          Tupla
    ['Luiz', 'João', 'Eduarda', ], # 2
]
# Desempacotamento

# for nome in lista:
#     print(nome, end=' ') #Esse end muda a quebra de linha para espaço

# Desempacotamento através do print
print(*lista)
print(*string)
print(*tupla)

print(*salas, sep='\n')
# Exemplo da lista
# lista1 = ['Marila', 'Helena', 'Eduarda']
# a, b, c = lista1 
# print(a, c)

# lista2 = ['Marila', 'Helena', 1, 2, 3, 4, 'Eduarda']

# a, b, c, *_ = lista2 # *_ é o resto da lista
# print(a, c)

# lista3 = ['Marila', 'Helena', 1, 2, 3, 4, 'Eduarda']

# p, b, *_, ap, u = lista3 # *_ é o resto da lista 
# # p = primeiro, ap = anti-penultimo, u = ultimo, mas são só nomes podia ser a,b,c... é só para ficar mais fácil a compreensão 
# print(p, u, ap)
