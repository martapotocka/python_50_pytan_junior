# Pytanie 1 - lista niepowtarzalnych elementów
# Korzystając z podanej listy A
# stwórz listę B zawierającą tylko unikalne elementy z listy A

A = [1,2,3,3,2,1,2,3] # -> [1,2,3]

B = []
for element in A:
    if element not in B:
        B.append(element)
print(B)

S = set(A)
