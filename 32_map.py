# Pytanie 32
# Otrzymujesz listę nazwisk zapisanych w różny sposób.
# Korzystając z funkcji map() przerób tę listę tak, aby zawierała tylko nazwiska zapisane
# poprawnie, z wielkimi literami tylko na początku imienia i nazwiska.

nazwiska = ['jan kot', 'ANNA KRÓL', 'jÓzef BYK', 'ROBERT wąŻ']

# map(funkcja, obiekt iterowalny) -> zwraca obiekt map
# użycie z funkcją, użycie z lambdą

def wyczysc(nazwisko):
    return nazwisko.lower().title()

print(list(map(wyczysc, nazwiska)))
print(list(map(lambda x: x.lower().title(), nazwiska))) # lub z lambdą

# Użyj funkcji map aby zamienić poniższą listę na listę booleanów
# informujących czy element w liście pierwotnej był czy nie był podzielny przez 2

A = [1,3,4,2]

def check_if_even(n):
    return True if n%2 == 0 else False

print(list(map(check_if_even, A)))
# print(list(map(lambda x: x%2==0, A)))


# Co otrzymamy w wyniku wykonania poniższego kodu?

A = [1,2,3,4,5,6,7,8,9]

B = list(map(lambda x: x / 4, A))
print(B)

# a) [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
# b) [False, False, False, True, False, False, False, True, False]
# c) [4, 8, 12, 16, 20, 24, 28, 32, 36]
