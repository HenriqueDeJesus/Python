"""
Closure e funções que retornam outras funções
"""

# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome}!'
#     return saudar

# s1 = criar_saudacao('Bom dia', 'Henrique')
# s2 = criar_saudacao('Bom noite', 'Henrique')

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

# s1 = criar_saudacao('Bom dia')
# s2 = criar_saudacao('Bom noite')
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom noite')

for nome in ['Maria', 'Joana', 'Henrique', 'João']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

# print(falar_bom_dia('Henrique'))
# print(falar_boa_noite('Henrique')) # closure é isso você precisa fechar o parenteses para retornar o valor salvo na memória da função


# def criar_saudacao(saudacao, nome):
#     return f'{saudacao}, {nome}!'

# s1 = criar_saudacao('Bom dia', 'Henrique')
# s2 = criar_saudacao('Bom noite', 'Henrique')

# print(s2)