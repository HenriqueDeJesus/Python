lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)

lista1 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista1)

lista2 = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]
print(lista2)