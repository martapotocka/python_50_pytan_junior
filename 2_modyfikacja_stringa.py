# Pytanie 2 - modyfikacja stringa
# Co się stanie po wykonaniu poniższego kodu?

a = "abcdefg"
print(a[1])
# a[1] = 'X'            # operacja zakazana, skutuje wyświetleniem TypeError

a_lista = list(a)       # stwórz listę zawierającą poszczególne litery stringa
a_lista[1] = 'X'        # zmodyfikuj element pod indeksem 1 (listy można modyfikować!)
a = "".join(a_lista)    # połącz elementy listy tworząc nowego stringa
print(a)
