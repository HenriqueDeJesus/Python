frase = 'O Python é uma linguagem de programação '\
'multiparadigma. '\
'Python foi criado prr Guido van Rossum'

i  = 0 
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase): # Conta quantas letras tem na variavel frase
    letra_atual = frase[i] # Este i vira um parametro para pegar a posição de cada letra da variavel frase

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual) # O count é usado para contar quantas vezes o letra atual na (frase / varivel) apareceu 

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)