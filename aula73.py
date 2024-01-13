"""
Higher Order Fuctions
Funções de primeira classe
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

# v = executa(saudacao, 'Bom dia', 'Luiz')
print(
    executa(saudacao, 'Bom dia', 'Luiz')
    )
print(
    executa(saudacao, 'Bom dia', 'Luiz')
    )


# def saudacao(msg):
#     return msg

# def executa(funcao, texto):
#     return funcao(texto)

# v = executa(saudacao, 'Bom dia')
# print(v)

# def executa(funcao):
#     return funcao()

# saudacao_2 = saudacao
# v = executa(saudacao_2)
# v = saudacao_2('Bom Dia')
# v = saudacao('Bom Dia')
# print(v)
# print(saudacao('Bom Dia'))

'''
Termos técnicos: Higher Order Functions e First-Class Functions
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
'''