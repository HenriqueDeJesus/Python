# \r\n return linefith -> CRLF usado em widows para quebra de linha
# \n -> LF usado em linux para quebra de linha

#sep usado para colacar separador nos espaços podendo ser qualquer caractere ou sem caractere
#end serve para fazer a quebra de linha com os argumentos \r\n ou \n quebra de linha ou colocar # que não dá quebra ded linha
#mas por padrão o print já separa e dá quebra de linha 
print(12, 34, 1011, sep="-", end='\n##') 
print(56, 78, sep='-', end='\n') 
print(9, 10, sep='-', end='\n') 