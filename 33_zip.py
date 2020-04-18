# Pytanie 33 - dostajesz dwie listy: jedna zawiera osoby, druga zawiera
# wiek tych osób. Na ich podstawie stwórz słownik, w którym powiążesz
# osobę z jej wiekiem.
# Co się stanie jeśli lista zawierająca wiek osób będzie dłuższa niż lista osób?

osoby = ['Anna', 'Bartłomiej', 'Ewa', 'Filip', 'Grzegorz']
wiek = [25, 34, 51, 40, 18]
wiek = [25, 34, 51, 40, 18, 50, 61]

L = list(zip(osoby,wiek))
D = dict(zip(osoby,wiek))

print(L)
print(D)
