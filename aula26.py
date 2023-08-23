"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígito>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esqquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes do zero
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O gexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
