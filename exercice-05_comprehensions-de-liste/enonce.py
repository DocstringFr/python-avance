# 1
liste = [1, 2, 3, 4, 5]
liste_double = []

for i in liste:
    liste_double.append(i * 2)

# 2
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double = []

for i in liste:
    if i > 0:
        liste_double.append(i * 2)

# 3
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double = []

for i in liste:
    if i > 0:
        liste_double.append(i * 2)
    else:
        liste_double.append(i * 3)

# 4
liste_finale = []
for a in range(10):
    for b in range(2):
        liste_finale.append((a, b))