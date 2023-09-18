"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


cpf =  '746.824.890-70'
mult = [10, 9, 8, 7, 6, 5, 4, 3, 2] 
cpf1 = cpf.split('-')
cpf_sem_ponto = cpf1[0].split('.')
cpf_unido = ''.join(cpf_sem_ponto)
listar_cpf = list(cpf_unido)
listar_cpf_numeros = list(map(int, listar_cpf))

cpf_usuario = cpf_unido + cpf1[1]

multiplicacao_0 = listar_cpf_numeros[0] * mult[0]
multiplicacao_1 = listar_cpf_numeros[1] * mult[1]
multiplicacao_2 = listar_cpf_numeros[2] * mult[2]
multiplicacao_3 = listar_cpf_numeros[3] * mult[3]
multiplicacao_4 = listar_cpf_numeros[4] * mult[4]
multiplicacao_5 = listar_cpf_numeros[5] * mult[5]
multiplicacao_6 = listar_cpf_numeros[6] * mult[6]
multiplicacao_7 = listar_cpf_numeros[7] * mult[7]
multiplicacao_8 = listar_cpf_numeros[8] * mult[8]

soma_todo_resultado_1 = multiplicacao_0 + multiplicacao_1 + multiplicacao_2 + multiplicacao_3 + multiplicacao_4 + multiplicacao_5 + multiplicacao_6 + multiplicacao_7 + multiplicacao_8 

mult_todo_resultado_1 = soma_todo_resultado_1 * 10

resto_div_1 = mult_todo_resultado_1 % 11

verificador_digito_1 = resto_div_1 if resto_div_1 <= 9 else 0

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

mult = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

multiplicacao_0 = listar_cpf_numeros[0] * mult[0]
multiplicacao_1 = listar_cpf_numeros[1] * mult[1]
multiplicacao_2 = listar_cpf_numeros[2] * mult[2]
multiplicacao_3 = listar_cpf_numeros[3] * mult[3]
multiplicacao_4 = listar_cpf_numeros[4] * mult[4]
multiplicacao_5 = listar_cpf_numeros[5] * mult[5]
multiplicacao_6 = listar_cpf_numeros[6] * mult[6]
multiplicacao_7 = listar_cpf_numeros[7] * mult[7]
multiplicacao_8 = listar_cpf_numeros[8] * mult[8]
multiplicacao_9 = verificador_digito_1 * mult[9]

soma_todo_resultado_2 = multiplicacao_0 + multiplicacao_1 + multiplicacao_2 + multiplicacao_3 + multiplicacao_4 + multiplicacao_5 + multiplicacao_6 + multiplicacao_7 + multiplicacao_8  + multiplicacao_9

mult_todo_resultado_2 = soma_todo_resultado_2 * 10
resto_div_2 = mult_todo_resultado_2 % 11

verificador_digito_2 = resto_div_2 if resto_div_2 <= 9 else 0

calculo_cpf = f'{cpf_unido}{verificador_digito_1}{verificador_digito_2}'
if calculo_cpf == cpf_usuario:
    print('CPF válido')
else:
    print('CPF inválido')
#cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
