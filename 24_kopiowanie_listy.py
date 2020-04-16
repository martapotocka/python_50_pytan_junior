# Pytanie 24 - co zostanie wypisane w wyniku wykonania poniższego kodu?

A = [1,2,3,4,5]
B = A
C = A[:]   # C = list(A)
B[0] = 111
print(B)
print(A)
print(C)
print(id(A), id(B), id(C))

# Rekruter sprawdza czy wiemy co dzieje się podczas operacji przyrównnia zmiennych do siebie.
# W takiej sytuacji kopiujemy referencję wskazującą na obiekt w pamięci, a nie sam obiekt.
# Takie samo zachowanie tyczyć będzie słowników oraz innych mutowalnych typów danych
# np obiektów klas. Aby utworzyć kopię WARTOŚCI słownika nalezy uzyć funkcji dict() analogicznie
# do list() użytego powyżej.
