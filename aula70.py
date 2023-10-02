"""
Retorno de valores das funções (return)
Somente função e metódo tem a palavra (return)
"""
# variavel = print('Henrique')
# # a função print de python é None porque ela não recebe valor apenas imprimi o que é mandado pelo desenvolvedor
# print(variavel)

# def soma(x, y):
#     print(x + y)

# variavel = soma(1, 2)
# variavel = int('1')

# soma1 = soma(2, 2)
# soma2 = soma(3, 3)
# print(soma1 + soma2) dá erro porque o print não guarda valor

def soma(x, y):
     print('Olha')
     print('só')
     print('que')
     print('legal')
     if x > 10:
          return 10, 20
     return x + y # em python o retun acaba a execução dessa função
     print(1+1) # O print não é executado porque ele não é alcançado por causa do return
     # Mas antes do return é possível usar print ou outra coisa função, métodos e etc.

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)
print(soma1)
print(soma2)
print(soma(11, 55))
