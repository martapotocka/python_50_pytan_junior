# Pytanie: czym różnią się od siebie operatory is i == ?

print(1 == 1)
print(1 == 10 - 9)   # == porównuje WARTOŚCI
print(1 == True)

print(1 is 1)
print(1 is 10 - 9)   # is porównuje czy lewa strona JEST TYM SAMYM co prawa
print(1 is True)     # id(1) == id(True)

print(id(1))
print(id(True))

A = [1,2,3]
B = [1,2,3]
print(A == B)
print(A is B)
print(id(A), id(B)) #zobaczysz inne id niz ja! Zmieni się przy kazdym uruchomieniu

a = 'kotek'
b = 'kotek'
print(a == b)
print(a is b)
print(id(a), id(b))

# Zmienne zawierające identyczne obiekty mutowalne (lista, słownik, set)
# NIE SĄ tym samym obiektem.
# Zmienne zawierające identyczne obiekty niemutowalne (int, float, bool, string, tuple)
# SĄ tym samym obiektem!
