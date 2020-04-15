# Pytanie 16 - wypisz podaną listę imion przed każdym dodając kolejny numer.
# Zacznij numerowanie od 1.

imiona = ['Adam', 'Stanisław', 'Maria', 'Zofia', 'Mikołaj']

idx = 1
for imie in imiona:
    print(idx, imie)
    idx += 1


# for idx, imie in enumerate(imiona, 1):
#     print(idx, imie)


# W tym pytaniu rekruter sprawdza czy znamy i potrafimy używać funkcji enumerate
