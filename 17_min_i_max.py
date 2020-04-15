# Pytanie 17 - znajdź różnicę między największą a najmniejszą wartością
# na poniższej liście.
# Zadbaj o to aby rozwiązanie było efektywne.

A = [4, 5, 7, -3, 2, 8, -10, 15]

# Rozwiązanie nieefektywne O(n*log_n):
A = sorted(A)
print(A[-1] - A[0])

# Rozwiązanie efektywne O(n):
najmniejszy = A[0]
najwiekszy = A[0]

for element in A:
    if element < najmniejszy:
        najmniejszy = element
    elif element > najwiekszy: # bez else, bo pozostałe przypadki nas nie interesują
        najwiekszy = element
print(najwiekszy - najmniejszy)

# Rozwiazanie efektywne i krótkie O(n):
print(max(A) - min(A))
