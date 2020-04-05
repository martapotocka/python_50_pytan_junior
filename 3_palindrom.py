# Palindrom to słowo, które czytane od początku do końca
# i od końca do początku brzmi tak samo.
# kajak - jest palindromem
# anakonda - nie jest palindromem

def sprawdz_czy_jest_palindromem(slowo):
    slowo_od_konca = slowo[::-1]
    if slowo == slowo_od_konca:
        return f"{slowo} jest palindromem."
    else:
        return f"{slowo} nie jest palindromem."

# def sprawdz_czy_jest_palindromem(slowo):
#     poczatek = 0
#     koniec = len(slowo) -1
#     while poczatek <= koniec:
#         if slowo[poczatek] != slowo[koniec]:
#             return f"{slowo} nie jest palindromem."
#         else:
#             poczatek += 1
#             koniec -= 1
#     return f"{slowo} jest palindromem."



print(sprawdz_czy_jest_palindromem('kajak'))
print(sprawdz_czy_jest_palindromem('anakonda'))
print(sprawdz_czy_jest_palindromem('anna'))
