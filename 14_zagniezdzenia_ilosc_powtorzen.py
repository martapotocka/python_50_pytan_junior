# Co wydrukuje ponizszy kod?

licznik = 0
for i in range(10):
    for j in range(20,30): # (10 do 19 - 10 elementow)
        for k in ['a', 'b', 'c', 'd', 'e']:
            licznik += 1

print(licznik)
