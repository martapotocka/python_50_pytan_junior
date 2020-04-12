# Pytanie 3 - napisz kod, który zaprezentuje
# najważniejsze różnice między listą a tuplą

# zacząć od nazewnictwa, że tupla to spolszczenie angielskiego tuple
# i poprawnie to jest krotka, ale mało osób tak mówi

# Powiedzieć, że listy i tuple mają wiele wspólnego, mogą przechowyać
# różne typy danych, mogą być zagnieżdżone, w identyczny sposób
# odczytujemy elementy

# powiedzieć, że różnica jet w zapisie [] vs ()
# oraz w mutowalności, bo tuple są niemutowalne

# Lista od tupli różni się zapisem
A = [1,2,3]  # listę zapisujemy w nawiasach kwadratowych
C = (1,2,3)  # tuplę zapisujemy w nawiasach okrągłych

# Lista jest mutowalna (modyfikowalna), a tupla nie.
# Najłatwiej to pokazać próbując zmodyfikować elementy obu struktur danych
A[0] = 111   # modyfikacja listy jest dopuszczalna i uda się
C[0] = 111   # modyfikacja tupli nie jest dupuszczalna i spowoduje wypisanie TypeError!
