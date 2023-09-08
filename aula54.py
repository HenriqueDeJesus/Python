"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()

    if  opcao == 'a':
        try:
            apagar = input('Escolha o índice para apagar: ')
            indice = int(apagar)
            del lista[indice]
        except:
            print('Não foi possivel apagar este indice')

    elif opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'l':
        if lista == []:
            os.system('cls')
            print('Nada para listar')
        else:
            os.system('cls')
            for indice, nome in enumerate(lista):
                print(indice, nome)

    else:
        print('Por favor, escolha i, a ou l')
