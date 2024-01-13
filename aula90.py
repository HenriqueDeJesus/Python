import sys 

# Genetor expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho','__iter__']
# iterator = iterable.__iter__() # tem __iter__e__next__
iterator = iter(iterable)
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# print(next(iterator))

