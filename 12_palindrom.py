# Pytanie 11 - napisz funkcję sprawdzającą czy podane słowo jest palindromem
# Palindrom to słowo, które czytane od początku do końca
# i od końca do początku brzmi tak samo.
# kajak - jest palindromem
# anakonda - nie jest palindromem

def sprawdz_czy_jest_palindromem(slowo):
    slowo_od_konca = slowo[::-1]
    if slowo == slowo_od_konca:
        return True
    else:
        return False
    # return True if slowo == slowo_od_konca else False # alternatywny, krótszy zapis

# def sprawdz_czy_jest_palindromem(slowo):
#     poczatek = 0
#     koniec = len(slowo) -1
#     while poczatek <= koniec:
#         if slowo[poczatek] != slowo[koniec]:
#             return False
#         else:
#             poczatek += 1
#             koniec -= 1
#     return True

print(sprawdz_czy_jest_palindromem("kajak"))
print(sprawdz_czy_jest_palindromem("anakonda"))
