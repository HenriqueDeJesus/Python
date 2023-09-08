"""
Introdução ao desempacotamento
"""

# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']

# nome1, *resto = ['Maria', 'Helena', 'Luiz']

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']

print(nome)
