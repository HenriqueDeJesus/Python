a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

string2 = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato2 = string2.format(nome1=a, nome2=b, nome3=c)

print(formato)
print(formato2)