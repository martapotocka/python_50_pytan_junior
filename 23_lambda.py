# Pytanie 22 - czym jest lambda?
# Napisz przykładowy kod wykorzystujący lambdę.

D = [('Anna',82), ('Robert',33), ('Artur',40), ('Feliks',56)]
posortowane = sorted(D, key = lambda x: x[1])
print(posortowane)



# lambdy nazywane sa tez funkcjami anonimowymi, poniewaz nie posiadaja nazwy
# do zdefiniowania lambdy uzywamy slowa kluczowego 'lambda'
# lambda argument:expression

# square_x = lambda x:x**2  # niezalecane, lepiej uzyc def i zrobic normalna funkcje
#
# lambda x:x**2 # taki zapis absolutnie nic nie robi
#
# def square_x(x):
#     return x**2
#
# print(square_x(5))

# uzycie lambd: programowanie funkcyjne, a więc takie, gdzie funkcje
# pobierają inne funkcje jako parametr
# w Pythonie:
# - sorted (omówione wyżej)
# - filter i map (w kolejnych lekcjach)
