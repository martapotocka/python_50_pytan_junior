# Pytanie 31 - jaką wartość przyjmie poniższe zdanie logiczne?
# Wyjaśnij proces jego ewaluacji i znaczenie poszczególnych słów: is, not, in.


print(1 is not True in [1,2,3])



# pamiętać o tym jak ewaluowane są dłuższe niż dwa wyrażenia zdania logiczne!
# print((not 2 is 2.0) and (2.0 in [0,2]))


# Powiedzieć, że ten SyntaxWarning to nowość w Pythonie 3.8 i można się nim sugerować
# ale nie zawsze ma rację. W tym wypadku chcieliśmy sprawdzić czy 1 i True
# są tym samym obiektem, a nie czy mają równą wartość
# (btw. jeśli dwa obiekty są tym samym obiektem wg Pythona, to ich wartość musi być równa)
# Przykład tego, że kompilator nie zawsze ma racje podpowiadając nam zamiane is na ==,
# bo te operatory mogą produkowąć odmienne rezultaty:
# print(1 is 1.0)
# print(1 == 1.0)

# is - sprawdza czy obiekty sa identyczne
# not - zwraca odwrotność boleeana z którym jest stosowany
# in - sprawdza czy obiekt jest w danym zbiorze obiektów (porównuje wartości, nie typy)
# dlatego True jest w zbiorze [1,2,3]
