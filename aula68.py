"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""


# x = 1

# def escopo():
#     def outra_funcao():
#         y = 2
#         print(x, y)

#     outra_funcao()
#     print(x)

# escopo()

x = 1

def escopo():
    
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

# def escopo():
#     global x # Isso faz com que o valor de fora do x que era 1 seja alterado
#     x = 10

#     def outra_funcao():
#         x = 11
#         y = 2
#         print(x, y)

#     outra_funcao()
#     print(x)

# print(x)
# escopo()
# print(x)

# def escopo():
#     global x # Isso faz com que o valor de fora do x que era 1 seja alterado
#     x = 10

#     def outra_funcao():
#        global x # Isso faz com que o valor de fora do x que era 1 seja alterad
#         x = 11
#         y = 2
#         print(x, y)

#     outra_funcao()
#     print(x)

# print(x)
# escopo()
# print(x)
