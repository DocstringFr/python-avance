import string

prenom = 'Astrid'
indices = [string.ascii_lowercase.index(x) for x in prenom.lower()]
combinaison = zip(prenom, indices)
resultat = ['{} -> {}'.format(x[0], x[1] + 1) for x in combinaison]

resultat_formate = '\n'.join(resultat)
print(resultat_formate)
