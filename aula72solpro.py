# Exercicios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor da variável
# print(1*2*3*4*5)
def multiplicar(*args):
    total = 1
    for numero in args:
       total *= numero
    return total

multiplicação = multiplicar(10, 2, 3, 4, 5) # Pode colocar o nome dá variavel em python com acento mais não é recomendado além disso o código precisa ser escrito em inglês a não ser quando você está ensinando alguem 
print(multiplicação)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar
# O do par e ímpar o professor fez de três jeito diferente até mostrando que em alguns casos o else é redundante
def par_impar(numero):
    return numero % 2 == 0

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))
