# Pytanie 20 - co otrzymamy w wyniku wyknania poniższego kodu?

L = [1,2,3,4,5,6]

L1 = [x*100 for x in range(5)]
L2 = [x**2 for x in L]
L3 = [x for x in L if x % 2 == 0]
L4 = ['Parzysta' if x%2 == 0 else 'Nieparzysta' for x in range(5)]
L5 = [(x, x+10) for x in L]
D1 = {x:x % 2 == 0 for x in L}

print(L1)
print(L2)
print(L3)
print(L4)
print(L5)
print(D1)
