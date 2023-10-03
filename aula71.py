"""
args - Argumento não nomeado
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#       return x + y

def soma(*args):
    total = 0
    for numero in args:
       # print('Total', total, numero)
       total += numero
        # total = total + numero
        # print('Total', total)
    # print(total)
    return total

# soma(1, 2, 3, 4, 5, 6)
soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6  = soma(4, 5, 6)
print(soma_4_5_6)

# outra_soma = soma(1, 2, 3, 4, 5, 6, 7, 78, 10)
# print(outra_soma)

# numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
# outra_soma = soma(numeros) # Assim dá errado porque ele cria uma tupla dentro de outra tupla
# print(outra_soma)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) # Se colocar o * ele desempacota a tupla aí dá certo
print(outra_soma)

# print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10)))
print(numeros)
print(*numeros)
print(sum(numeros)) # o sum só funciona com dois argumentos e para que a variavel numeros fizesse a soma de tudo é necessário desmpacotar primeiro com o *
