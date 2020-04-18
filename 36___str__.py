# Pytanie 36 - wykorzystajmy klasę Pies i obiekt maly_pies z poprzedniego pytania.
# Co stanie się gdy wypiszemy print(maly_pies)?
# Co zrobiłbyś, aby wydrukowana w ten sposób informacja zawierała imie i rase psa?

class Pies:
    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa

# obiekt.__str__() jest wywoływane jeśli zawołamy print(obiekt) lub str(obiekt)

    def __str__(self):
        return f"Pies {self.imie} jest rasy {self.rasa}." # mozemy dodac formatowanie i co chcemy

maly_pies = Pies("Pikuś", "ratlerek")

print(maly_pies)
moj_pies = str(maly_pies)
print(moj_pies)
