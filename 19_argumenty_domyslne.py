# Pytanie 19 - wyjasnij jak działa poniższa funkcja.
# Wyjaśnij skąd wzięły się wyniki zwrócone przez poszczególne wywołania funkcji.

def dodaj_do_listy(n, lista=[]):
    lista.append(n)
    print(lista)


dodaj_do_listy(1)
dodaj_do_listy(2,[4,5])
dodaj_do_listy(3)

# Rekruter sprawdza czy wiemy jak działają argumenty domyślne
# I czy wiemy jak Python traktuje argumenty domyślne
# Argument domyślny tworzony jest RAZ podczas definiowania funkcji,
# a nie za każdym razem gdy ją wywołujemy. Wartość argumentu domyślnego
# przechowywana jest w pamięci i jeśli jest on mutowalnym typem danych (jak lista)
# to jeśli zmienimy jego wartość podczas jednego wywołania funkcji,
# to wartość ta zostana zapamiętana i wykorzystana przy kolejnym jej wywołaniu.
