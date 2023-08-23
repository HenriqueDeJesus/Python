primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro = int(primeiro_valor)
segundo = int(segundo_valor)

linha_1 = f" primeiro_valor='{primeiro}' é maior do que segundo_valor='{segundo}'"
linha_2 = f" segundo_valor='{segundo}' é maior do que primeiro_valor='{primeiro}'"
linha_3 = f" primeiro_valor='{primeiro}' é igual segundo_valor='{segundo}'"

if primeiro > segundo:
    print(linha_1)
elif segundo > primeiro:
    print(linha_2)
else:
    print(linha_3)

# Saída tem que mostar qual é o numero maior
# Exemplo:
# segundo_valor='2' é maior do que primeiro_valor='1'

#Outro jeito de fazer que foi feito pelo professor segue a baixo o código

"""
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
        )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )

"""