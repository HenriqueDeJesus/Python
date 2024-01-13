# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# s1 = set()
# print(s1, type(s1))

# s2 = set('Henrique')
# print(s2)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# s1 = {1, 2, 3, 3, 3, 3, 3, 1}
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(s1)
print(l2)
a = b = 1 # Isso pode no python
# s3 = {1, 2, 3, [123], {123}, (123)} # Não irá funcionar porque não pode existir uma lista ou o próprio set dentro do set porque são valores mútaveis
# Tupla pode dentro de um set
s4 = {1, 2, 3}
print(3 in s4)
for numero in s4:
    print(numero)

# Métodos úteis:
# add, update, clear, discard
s5 = set()
s5.add('Luiz')
s5.add(1)
# s1.add(1, 2) Isso não pode porque o add só adiciona um item de cada vez
s5.update('Olá mundo') # Aqui não foi colocado numa tupla então ele vai ler valor por valor
s5.update(('Olá mundo', 1, 2, 3, 4)) # No update pode mandar vário valores mas coloca numa tupla
# s5.clear() # Limpa o set
s5.discard('Olá mundo') # Descarta o valor passado nele
s5.discard('Luiz')
print(s5)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s6 = {1, 2, 3}
s7 = {2, 3, 4}
s8 = s6 | s7 
s9 = s6 & s7 
s10 = s6 - s7 
s11 = s7 - s6
s12 = s6 ^ s7 # Não importa a ordem
print(s8)
print(s9)
print(s10)
print(s11)
print(s12)