"""
slipt e join com list e str
split - divide uma string
join - une uma string
"""
frase = '    Olha só que   , coisa interessante     '
lista_frases = frase.split()
lista_frases_1 = frase.split(',')
lista_frases_2 = frase.split(', ')
print(lista_frases)
print(lista_frases_1)
print(lista_frases_2)

for i, frase in enumerate(lista_frases_1):
    print(lista_frases_1[i])

for i, frase in enumerate(lista_frases_1):
    print(lista_frases_1[i].strip()) # strip remove os espaços automaticamente esxiste o rstrip que corta o espaço da direita e o lstrip que corta o espaço da esquerda
print(lista_frases_1)

for i, frase in enumerate(lista_frases_1):
    lista_frases_1[i] = lista_frases_1[i].strip()

print(lista_frases_1)

#Embaixo segue o jeito certo de corrigir uma frase mesmo que o código fique maior

frase1 = '    Olha só que   , coisa interessante     '
lista_frases_crua = frase1.split(',')

lista_frases_novo = []
for i, frase in enumerate(lista_frases_crua):
    lista_frases_novo.append(lista_frases_1[i].strip())

print(lista_frases_crua)
print(lista_frases_novo)

#Join

frases_unidas = '-'.join('abc')
print(frases_unidas)

frases_unidas_1 = '-'.join(lista_frases_novo)
print(frases_unidas_1)
frases_unidas_2 = ', '.join(lista_frases_novo)
print(frases_unidas_2)
