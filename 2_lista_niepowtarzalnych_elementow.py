# Zadanie 2
# Zmodyfikuj podaną listę A tak, aby zawierała tylko elementy niepowtarzalne

A = [1,2,3,3,2,1,2,3]

B = []                    # stworz pustą listę B
for number in A:          # przeczytaj po kolei wszystkie elementy listy A
    if number not in B:   # jeśli elementu nie ma jeszcze na liście B
        B.append(number)  # to dodaj go go listy B
A = B                     # zawartość listy B przypisz na powrót do zmiennej A
print(A)

# A = list(set(A))          # rozwiązanie sprytne
# print(A)
