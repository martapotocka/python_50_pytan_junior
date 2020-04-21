# Pytanie 12 - napisz funkcję sprawdzającą czy podane słowo jest palindromem.
# Uruchom funkcję aby sprawdzić czy palindromami są słowa "kajak" i "anakonda".

# Anna # gawron # radar

# def sprawdz_czy_palindrom(slowo):
#     return True if slowo == slowo[::-1] else False
#     # slowo_odwrocone = slowo[::-1]
#     # if slowo == slowo_odwrocone:
#     #     return True
#     # else:
#     #     return False

def sprawdz_czy_palindrom(slowo):
    poczatek = 0
    koniec = len(slowo) - 1
    while poczatek <= koniec:
        if slowo[poczatek] != slowo[koniec]:
            return False
        else:
            poczatek += 1
            koniec -= 1
    return True


print(sprawdz_czy_palindrom("kajak"))
print(sprawdz_czy_palindrom("anakonda"))
