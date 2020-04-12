# Pytanie 1 - lista niepowtarzalnych elementów
# Korzystając z podanej listy A
# stwórz listę B zawierającą tylko unikalne elementy z listy A

A = [1,2,3,3,2,1,2,3]

B = []                     # stwórz pustą listę B
for element in A:          # dla każdego elementu z listy A
    if element not in B:   # jeśli ten element nie znajduje się w B
        B.append(element)  # dodaj go do B
print(B)

B = list(set(A))           # a tu rozwiązanie sprytniejsze :)
print(B)
