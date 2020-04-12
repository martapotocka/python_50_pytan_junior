# Pytanie 3 - czym różni się lista od tupli

# zacząć od nazewnictwa, że tupla to spolszczenie angielskiego tuple
# i poprawnie to jest krotka, ale mało osób tak mówi

# Powiedzieć, że listy i tuple mają wiele wspólnego, mogą przechowyać
# różne typy danych, mogą być zagnieżdżone, w identyczny sposób
# odczytujemy elementy

# powiedzieć, że różnica jet w zapisie [] vs ()
# oraz w mutowalności, bo tuple są niemutowalne

A = [1,2,3]
B = [1, True, 'jakis_string', (4,5,6)]
C = (1,2,3)
D = (2, False, 'xxx', [7,8,9])

print(A[0], B[1], C[2], D[0])
A[0] = 111
C[0] = 111
