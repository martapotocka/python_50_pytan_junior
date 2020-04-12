# Pytanie 4 - jakiej struktury danych użyłbyś do zamodelowania
# szafki, która ma 3 szuflady, a w każdej z nich 3 przegródki?
# Stwórz taki model i umieść stringa "tutaj"
# w środkowej przegródce środkowej szuflady.

# Można tworzyć zarówno zagnieżdżone listy jak i tuple,
# ale jeśli chcemy modyfikować zawartość, musimy użyć listy,
# która jest mutowalna

# Lista zawierająca trzy listy, każda z nich zawiera równiez trzy listy
szafka = [[[],[],[]],[[],[],[]],[[],[],[]]]
szafka[1][1].append('tutaj')  # do drugiej przegródki drugiej listy dodaj string
print(szafka)

for szuflada in szafka:       # drukowanie wiersz po wierszu
    print(szuflada)
