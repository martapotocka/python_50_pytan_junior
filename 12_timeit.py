import timeit

def zmien_mi_nazwe_na_lepsza():
    suma = 0
    for i in range(1000):
        for j in range(1000):
                suma += i*j
    return(suma)

print(timeit.timeit(zmien_mi_nazwe_na_lepsza()))
