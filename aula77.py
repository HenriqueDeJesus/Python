# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]
os.system('cls')

pergunta1 = perguntas[0]['Pergunta']
resposta1 = perguntas[0]['Resposta']

pergunta2 = perguntas[1]['Pergunta']
resposta2 = perguntas[1]['Resposta']

pergunta3 = perguntas[2]['Pergunta']
resposta3 = perguntas[2]['Resposta']

escolha_opcao = 0
acertos = 0
print()
print(pergunta1)
print()
print('Opções:')
for chave in perguntas[0]['Opções']:
      print(f'{escolha_opcao}) {chave}')
      escolha_opcao += 1

try:
    alternativas1 = input('Escolha uma opção: ')
    alternativa1 = int(alternativas1)

    resposta_escolhida1 = perguntas[0]['Opções'][alternativa1]
    
    if resposta_escolhida1 == resposta1:
                print('Acertou')
                acertos += 1
    else:
                print('Errou')
                acertos += 0
except:
        print('Errou pois essa alternativa não existe')
        acertos += 0


escolha_opcao = 0
print()
print(pergunta2)
print()
print('Opções:')
for chave in perguntas[1]['Opções']:
      print(f'{escolha_opcao}) {chave}')
      escolha_opcao += 1

try:
    alternativas2 = input('Escolha uma opção: ')
    alternativa2 = int(alternativas2)

    resposta_escolhida2 = perguntas[1]['Opções'][alternativa2]
    if resposta_escolhida2 == resposta2:
                print('Acertou')
                acertos += 1
    else:
                print('Errou')
                acertos += 0
except:
        print('Errou pois essa alternativa não existe')
        acertos += 0


escolha_opcao = 0
print()
print(pergunta3)
print()
print('Opções:')
for chave in perguntas[2]['Opções']:
      print(f'{escolha_opcao}) {chave}')
      escolha_opcao += 1

try:
    alternativas3 = input('Escolha uma opção: ')
    alternativa3 = int(alternativas3)

    resposta_escolhida3 = perguntas[2]['Opções'][alternativa3]
    
    if resposta_escolhida3 == resposta3:
                print('Acertou')
                acertos += 1
    else:
                print('Errou')
                acertos += 0
except:
        print('Errou pois essa alternativa não existe')
        acertos += 0

print()
print(f'Você acertou {acertos} ')
print('de 3 Perguntas')