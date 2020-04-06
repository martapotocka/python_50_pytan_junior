a = "moj_kod.py"
b = "moje_notatki.txt"

def sprawdz_czy_python(nazwa_pliku):
    if nazwa_pliku[-3:] == ".py":
        print(f"{nazwa_pliku} to plik Pythona.")
    else:
        print(f"{nazwa_pliku} to nie plik Pythona.")

sprawdz_czy_python(a)
sprawdz_czy_python(b)
