# Pytanie 8 - Co zostanie wypisane w wyniku wykonania poniższego kodu?

D = {1: 'Ala', 2: 'ma', 3: 'kota'}

# Pętla for iteruje zawsze po kluczach słownika
for key in D:       # dla kolejnego klucza w słowniku D
    print(D[key])   # wydrukuj wartość przechowywaną pod tym kluczem

# Odpowiedź: to zalezy od wersji Pythona
# Pythony do 3.5 - słowniki nie gwarantują kolejności
# Python     3.6 - słowniki powinny zachować kolejność
# Python  od 3.7 - słowniki gwarantują kolejność
