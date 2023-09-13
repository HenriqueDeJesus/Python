"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena',], # 0
    # 0
    ['Elaine',], # 1
    # 0       1       2          Tupla
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 44)], # 2
]

print(salas[1])
print(salas[1][0])
print(salas)
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][2])

salas_1 = [
    # 0        1
    ['Maria', 'Helena',], # 0
    # 0
    ['Elaine',], # 1
    # 0       1       2          Tupla
    ['Luiz', 'João', 'Eduarda', ], # 2
]

for sala in salas_1:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
