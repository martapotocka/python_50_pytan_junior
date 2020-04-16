# wypisz wszystkie kombinacje elementow powyzszych list

A = ['a', 'A']
B = ['b', 'B']
C = ['c', 'C']

for a in A:
    for b in B:
        for c in C:
            print(a+b+c)
