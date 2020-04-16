# Pytanie 28 - zadaniem jest znalezienie graniastosłupa o bokach a, b, c
# będących elementami losowo wygenerowanych list integerów A, B i C.
# Ile operacji zostanie wykonane w wyniku uruchomienia poniższego kodu?
# W jaki sposób można by to zadanie rozwiązać efektywnej?

import random

A = [random.randint(0,100) for i in range(100)]
B = [random.randint(0,100) for i in range(100)]
C = [random.randint(0,100) for i in range(100)]


# max_v = 0
# licznik = 0
# for a in A:
#     for b in B:
#         for c in C:
#             licznik += 1
#             if a * b * c > max_v:
#                 max_v = a * b * c
# print(max_v)
# print(counter)

# print(max(A) * max(B) * max(C))
