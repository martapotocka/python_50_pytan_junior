# Pytanie 9 - dla danego stringa x stwórz słownik
# przechowujący informację ile razy dana litera wystąpiła w stringu

x = "myszydokazujągdykotanieczują"

L = {}
for litera in x:
    if litera not in L.keys():  # wystarczy samo L
        L[litera] = 1
    else:
        L[litera] += 1

print(L)
