# Jedno z najpopulraniejszych zadań na wszystkich poziomach rekrutacji
# sprawdź czy liczba 3 znajduje się w liście

P = [-10, -5, -3, 0, 3, 5, 68, 341, 500]  # lista musi być posortowana!
# K = ['Anna', 'Bartek', 'Kamil', 'Marta', 'Paweł', 'Stanisław', 'Zbigniew']

znaleziono = False
do_znalezienia = -11
licznik = 0
# for liczba in P:    # rozwiązanie nieefektywne, nie wykorzystuje faktu, ze lista jest posortowana
#     licznik += 1
#     if liczba == do_znalezienia:
#         znaleziono = True
#         break


dolny_indeks = 0
gorny_indeks = len(P)-1

while dolny_indeks <= gorny_indeks:
    licznik += 1
    aktualny_indeks = (dolny_indeks + gorny_indeks)//2
    if P[aktualny_indeks] == do_znalezienia:
        znaleziono = True
        break
    elif P[aktualny_indeks] > do_znalezienia:
        gorny_indeks = aktualny_indeks - 1
    else:
        dolny_indeks = aktualny_indeks + 1


if znaleziono == True:
    print(f"{do_znalezienia} znajduje się w liście.")
else:
  print(f"{do_znalezienia} nie znajduje się w liście.")
print(f"licznik: {licznik}")
