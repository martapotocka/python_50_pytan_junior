# Pytanie 6 - jakiej struktury danych użyłbyś do zapisania numerów telefonów
# wszystkich Polaków i odpowiadających im nazwisk?
# Dodatkowym wymaganiem jest, aby możliwe było szybkie sprawdzenie
# nazwiska przypisanego do danego numeru telefonu.

# Stwórz przykładową strukturę przechowującą poniższe informacje.
# Odczytaj nazwisko właściciela numeru 123456789

# numer 123456789 - Jan Kot
# numer 999888777 - Anna Lis
# numer 111222333 - Jan Kot

kontakty = {123456789: 'Jan Kot', 999888777: 'Anna Lis', 111222333: 'Jan Kot'}

print(kontakty[123456789])

# powiedzieć o tym co to jest klucz, co to jest wartość, key, value
# że klucze są unikatowe i dlatego nadaje sie do prezchowywania numeru telefonu
# co się stanie jak wpiszemy kilka takich samych kluczy (nadpisze się)
# i o czasie dostępu do słownika (jakoś w uproszeczniu)
