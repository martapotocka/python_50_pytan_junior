# Pytanie 1
# Co się stanie po wykonaniu poniższego kodu?

a = "abcdefg"
print(a[1])
# a[1] = 'B' # próba modyfikacji stringa skutkuje wypisaniem TypeError
print(a)

# Jeśli chcemy zmodyfikować string, najłatwiej zrobić to zamieniając go na chwilę w listę

a_lista = list(a)     # tworzenie listy zawierającej poszczególne litery stringa
a_lista[1] = 'B'      # modyfikacja elementu listy (modyfikowanie list jest legalne!)
a = "".join(a_lista)  # tworzenie nowego stringa z elementów listy
print(a)
