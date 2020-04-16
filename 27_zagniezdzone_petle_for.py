# Pytanie 27 - wypisz wszystkie trzyelementowe kombinacje elementow powyzszych list
# np: abc, abC, aBc i tak dalej...
# Czy wiesz ile elementów zostanie wydrukowane?

# import itertools

A = ['a', 'A']
B = ['b', 'B']
C = ['c', 'C']

for a in A:
    for b in B:
        for c in C:
            print(a, b, c)

# product_list = itertools.product(A, B, C)
# print(list(product_list))

# A co jeśli list, z których mamy tworzyć kombinacje było by 20?

# for a in Pierwsza:
#     for b in Druga:
#         for c in Trzecia:
#             for d in Czwarta:
#                 for e in Piąta:
#                     for f in Szósta:
#                         for g in Siódma:
#                             for h in Ósma:
#                                 for g in Dziewiąta:
#                                     for i in Dziesiąta:
#                                         print("Czy na pewno tędy droga?")
