# Pytanie 1
# Co się stanie po wykonaniu poniższego kodu?

a = "abcdefg"
print(a[1])
# a[1] = 'X' # próba modyfikacji stringa skutkuje wypisaniem TypeError
print(a)

# Jeśli chcemy zmienić zawratość stringa, musimy utworzyć nowy string
# który przypiszemy do zmiennej zawierającej pierwotny string

a_lista = list(a)     # tworzenie listy zawierającej poszczególne litery stringa
a_lista[1] = 'X'      # modyfikacja elementu listy (modyfikowanie list jest legalne!)
a = "".join(a_lista)  # tworzenie nowego stringa z elementów listy
print(a)
