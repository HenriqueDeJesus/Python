"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se ese número é par ou ímapar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um número: ')

# try:
#     numero_int = int(numero)

#     if numero_int % 2 == 0:
#         print('O número é par')
#     else:
#         print('O número é ímpar')
# except:
#     print('Isso não é um número inteiro')
    
# # Resolução do professor

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

# try :
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horario = input('Qual é a hora: ')

# try:
#     horario_atual = int(horario)

#     bom_dia = horario_atual >= 0 and horario_atual <= 11
#     boa_tarde = horario_atual >= 12 and horario_atual <= 17
#     boa_noite = horario_atual >= 18 and horario_atual <= 23

#     if bom_dia == True:
#         print('Bom dia 0-11')
#     elif boa_tarde == True:
#         print('Boa Tarde 12-17')
#     else:
#         print('Boa noite 18-23')

# except:
#     print('Isso não é um horário inteiro')


# Resolução do professor

# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Digite seu nome: ')

# nome_curto = len(nome) <= 4
# nome_normal = len(nome) == 5 or len(nome) == 6
# nome_grande = len(nome) >= 7

# if nome_curto == True:
#     print('Seu nome é curto')
# elif nome_normal == True:
#     print('Seu nome é normal')
# else:
#     print('Seu nome é muito grande')

# Resolução do professor

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')