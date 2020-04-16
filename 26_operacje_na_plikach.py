# Pytanie 26
# - stwórz plik o nazwie "moj_plik.txt"
# - wpisz do niego liczby od 1 do 100, każdą w nowej linijce
# - otwórz plik i zapisz jego zawartosc do listy z_pliku

with open('moj_plik.txt','w') as f:
    for n in range(1,101):
        f.write(str(n) + '\n')
    # f.writelines([(str(x)+'\n') for x in range(1,101)])
    # metoda writelines ma myląca nazwę, nie wpisuje kolejnych linii, ale pobiera
    # obiekt iterowalny (iterable) stringów, czyli zwykle listę lub tuplę.
    # znak nowej linii nalezy dopisać samemu.

with open('moj_plik.txt','r') as f:
    z_pliku = f.readlines() # readlines() odczytuje każdą linijkę jako osobny element
                              # i dodaje do listy
    # z_pliku = f.read()        # read() odczytuje cały plik jako jeden string
    print(z_pliku)
