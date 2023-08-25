"""
Iterável 
Iterador -> quem sabe entregar um valor por vez  
next -> me entregue o próximo valor
iter -> me entregue se iterador
"""
#for letra in texto
texto = 'Henrique' # iterável

# O for gunciona como esse while por baixo dos panos
# Iteratador = iter(texto) # iterador

# while True:
#     try       :
#         letra = next(Iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
    
