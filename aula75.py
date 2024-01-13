# Exercicios 
# Crie funções que duplicam, triplicam e quadriplicam 
# o número recebido como parâmetro.

numero1 = input('Digite um número para duplicar, triplicar e quadriplicar: ')
numero_digitado = int(numero1)

def duplica(numero):
    total = numero * 2
    return f'O dobro de {numero} é: {total}'

def triplica(numero):
    total = numero * 3
    return f'O triplo de {numero} é: {total}'

def quadriplica(numero):
    total = numero * 4
    return f'O quadroplo de {numero} é: {total}'

duplicar = duplica(numero_digitado)
triplicar = triplica(numero_digitado)
quadriplicar = quadriplica(numero_digitado)

print(duplicar)
print(triplicar)
print(quadriplicar)