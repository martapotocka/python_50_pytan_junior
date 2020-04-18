# Pytanie 34 - dostajesz listę stringów jakie klienci naszej firmy wprowadzili
# w pole "rok urodzenia" w formularzu. Niestety programista tworzący formularz
# nie zaimplementował mechanizmu sprawdzającego czy wpisane dane sa poprawne.
# Twoim zadaniem jest więc je oczyścić. Usuń z listy wszystkie elementy, które:
# - nie są liczbą
# - nie są z przedziału od 1900 do 2010

dane = [1990, 'xxx', 2002, 'nie wasza sprawa', 1983, 1989, 'pupa', 1410]

def sprawdz_poprawnosc(rok):
    if type(rok) is not int:
        return False
    elif not rok >= 1900 and rok <= 2010:
        return False
    else:
        return True

dane_oczyszczone = list(filter(sprawdz_poprawnosc, dane))
print(dane_oczyszczone)
