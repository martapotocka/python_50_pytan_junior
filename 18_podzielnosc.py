# Pytanie 18 - napisz funkcję, która będzie pobierać dwie liczby
# i sprawdzać czy pierwsza z nich jest podzielna przez drugą

def sprawdz_podzielnosc(a, b):
    return(a % b == 0)

print(sprawdz_podzielnosc(10,5))
print(sprawdz_podzielnosc(11,5))

# % dzielenie modulo - zwraca resztę z dzielenia dwóch liczb
# np. 11 % 5 zwróci 1 (bo wynik to 2, reszty 1)

# W tym zadaniu rekruter sprawdza czy potrafimy napisać prostą funkcję
# czy wiemy jak działa dzielenie modulo
# i czy potrafimy użyć go do sprawdzenia podzielności
# Przydatne zwłaszcza przy szukaniu liczb parzystych (podzielnych prez 2)
