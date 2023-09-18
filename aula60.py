"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)

condicao1 = 10 == 11
variavel1 = 'Valor' if condicao1 else 'Outro Valor'
print(variavel1)


digito = 1 # > 9 =0
novo_digito = digito if digito <= 9 else 0
novo_digito1 = 0 if digito > 9 else digito
print(novo_digito)
print(novo_digito1)

print('Valor' if True else 'Outro Valor' if True else 'Fim')
print('Valor' if False else 'Outro Valor' if True else 'Fim')
print('Valor' if False else 'Outro Valor' if False else 'Fim')
