# Pytanie 2 - modyfikacja stringa
# Co się stanie po wykonaniu poniższego kodu?

a = "abcdefg"
print(a[1])

a_lista = list(a)
a_lista[1] = 'X'
a = "".join(a_lista)
print(a)
