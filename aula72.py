# Exercicios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor da variável

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar


def multiplica(*args):
    total = 1
    for numero in args:
       total *= numero
    return total

multiplica_1 = multiplica(1, 2, 3, 4, 5, 6)
print(multiplica_1)

print(1*2*3*4*5*6)

def par_impar(x):
    if x % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
    

par = par_impar(10)
impar = par_impar(11)
