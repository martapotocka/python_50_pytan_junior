# Pytanie 35 - do czego w Pythonie służy __init__ ? Czym różni się od __init__.py ?
# Napisz fragment kodu wykorzystujący __init__.
#
# Rekruter sprawdza naszą podstawową wiedzę związaną z programowaniem obiektowym.
# Init to METODA klasy będąca jej konstruktorem, a więc pozwalająca tworzyć obiekty tej klasy.
# __init__.py (podac w ktorej lekcji to było) to plik, który umieszczony w katalogu informuje
# Pythona, ze ten katalog jest pakietem. Nie ma więc z __init__ nic wspolnego (poza wyglądem).

class Pies:
    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa

maly_pies = Pies("Pikuś", "ratlerek")
duzy_pies = Pies("Killer", "doberman")

print(maly_pies.imie, maly_pies.rasa)
print(duzy_pies.imie, duzy_pies.rasa)
