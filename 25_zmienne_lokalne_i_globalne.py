# Pytanie 25 - co zostanie wypisane w wyniku wypisania poniższego kodu?

x = 10            # zmienna globalna

def f():
    print(x)
    x = 11        # zmienna lokalna
    y = 12        # zmienna lokalna
    print(f"x: {x}, y: {y}")

f()
print(f"x: {x}")   # ta linijka się wykona
print(f"y: {y}")   # ta linijka zwróci NameError - zmienna y nie jest dostępna poza funkcją

# Co zrobić, aby zmodyfikować zmienną globalną wewnątrz funkcji? global
# Co się stanie jeśli wewnątrz funkcji spróbujemy wydrukować zmienną globalną
# a potem stworzyć jej lokalny odpowiednik? UnboundLocalError
