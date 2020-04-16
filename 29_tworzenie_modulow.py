# Pytanie 29 - jaki błąd popełniono w poniższym kodzie?
# Co zrobić aby go uniknąć?
# Stworz moduł kserokopiarka zawierający funkcję, która podany string wydrukuje dwa razy
# Użyj tej funkcji w kodzie poniżej

from drukarka import wydrukuj_imie
# from kserokopiarka import zrob_ksero

def wydrukuj_imie(imie):  #np robiąc rename na wydrukuj_imie_lokalnie
    print(imie)

wydrukuj_imie("Marta")
# zrob_ksero("Hello world!")
