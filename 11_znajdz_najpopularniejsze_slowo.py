D = {'ala': 4, 'ola': 3, 'zosia': 2, 'jadwiga':1}

print(max(D.values()))

for item in D.items():
    if item[1] == 4:
        print(item[0])
