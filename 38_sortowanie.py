# Pytanie 24 - twoim zadaniem jest posortowanie listy integerów.
# Jak to zrobisz? Jakie znasz rodzaje sortowania w Pythonie?
#
# Odpowiedź: używam wbudowanej, efektywnej funkcji sort lub sorted,
# która wykonuje się w O(n * log_n) przy użyciu sortowania timsort.
# Ręczne pisanie sortowania nie ma sensu.
# Ale gdybyś miał napisac sortowanie?

A = [6,7,3,4,5,6,2,-5,3,-6]

# A.sort()    # lista.sort() modyfikuje listę, na której jest wywołany
B = sorted(A) # sorted(lista) tworzy nową listę, nie modyfikując oryginalnej
print(A)
print(B)
