# 1
liste = [1, 2, 3, 4, 5]
liste_double = [i * 2 for i in liste]

# 2
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double = [i * 2 for i in liste if i > 0]

# 3
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double = [i * 2 if i > 0 else i * 3 for i in liste]

# 4
[(a, b) for a in range(10) for b in range(2)]
