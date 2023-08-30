"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índice e fatiameento
Métodos úteeeis:
     append, insertm pop, del, clear,extend, +
Create Read Update Delete
Criar ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1   2   3   4  5
lista = [10, 20, 30, 40]
# lista[2] = 300 # Aqui está atualizando indice 2 da lista que era 30 agora vira 300
# del lista[2] # Deleta o indice 2 da lista que é o 300 porque foi atualizado
# print(lista)
# print(lista[2]) # O resultado vai ser 40 porque eu exclui o valor do indice 2 que era 300 então o pytho realoca a lista
lista.append(50) # Adiciona item no final da lista
lista.pop() # Remove o ultimo valor da lista nesse caso o 50 porque foi o ultimo a ser adicionado na lista porque o pytho le da esquerda para a direita de cima para baixo
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # remove o indice 3 da lista que é o 40
print(lista, 'Removido,', ultimo_valor)
