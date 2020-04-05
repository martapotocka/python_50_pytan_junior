A = [1,2,3,3,2,1,2,3]

print(list(set(A)))   # rozwiązanie sprytne

B = []

for number in A:      # rozwiązanie klasyczne
    if number not in B:
        B.append(number)

print(B)
