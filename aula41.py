"""while/else"""
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei espaço na string.')
print('Fora do while.')

# O else só vai ser executado quando o while for excutado por completo,
# No exeplo o else não é executado porque dentro do while encontrou um espaço que faz o código parar através do if usando um break