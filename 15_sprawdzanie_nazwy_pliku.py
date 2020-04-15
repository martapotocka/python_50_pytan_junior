# Pytanie 14 - napisz funkcję, która sprawdzi czy podany string
# zaczyna się słowem "python" i kończy rozszerzeniem ".py"
# Przetestuj nią stringi:
a = "python_moj_kod.py"
b = "python_notatki.txt"

def sprawdz_czy_python(nazwa_pliku):
    if nazwa_pliku[:6] == "python" and nazwa_pliku[-3:] == ".py":
        return True
    else:
        return False
    # return True if nazwa_pliku[-3:] == ".py" else False

# W tym pytaniu rekruter sprawdza czy potrafimy praktycznie użyć sliców.

print(sprawdz_czy_python(a))
print(sprawdz_czy_python(b))
