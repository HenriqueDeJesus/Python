"""
For + Range
range -> range(start, stop, step)
"""
#numeros = range(10) #Termina com 10 de 0 á 9 porque começa do 0
# numeros = range(5, 10) # Inicia com 5 e termina no 10
# numeros = range(5, 10, 2) # Inicia com 5 e termina no 10 e pula de 2 em 2

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
