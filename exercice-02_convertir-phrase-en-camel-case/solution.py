# Solution 1
phrase = 'Phrase en camel case'
mots = phrase.lower().split(' ')
phrase_convertie = mots[0]
for i, mot in enumerate(mots):
    if i > 0:
        phrase_convertie += mot.capitalize()
print(phrase_convertie)

# Solution 2
# Et pour ceux que cela intéresse, voici une façon plus optimisée mais qui n'utilise pas la fonction enumerate :
phrase = 'Phrase en camel case'
mots = phrase.lower().split(' ')
phrase_convertie = mots.pop(0)
for mot in mots:
    phrase_convertie += mot.capitalize()
print(phrase_convertie)
