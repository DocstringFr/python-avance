import re

# Match valide : retourne 'item01'
re.match(r'[a-z]+\d{2}', 'item01')

# Match valide : retourne 'Pierre Dupont'
re.match(r'[a-zA-Z]+\s\w+', 'Pierre Dupont')

# Match invalide : on cherche un espace au début de la chaîne de caractère, mais elle commence par une lettre.
re.match(r'\s+', 'pierre dupont')

# Match valide : retourne 'pierre'
re.match(r'\w+', 'pierre dupont')

# Match valide : retourne 'pierre-'
re.match(r'\w+([-+=]?)', 'pierre-dupont')

# Match valide : retourne 'pierre'
re.match(r'\w+([-+=]?)', 'pierre/dupont')

# Match invalide : le + cherche si les caractères -, + ou = sont présents au moins une fois ou plus dans la chaîne de caractère.
# Aucun de ses éléments ne se retrouve dans la chaîne de caractère au moins une fois et donc le match n'est pas valide.
re.match(r'\w+([-+=]+)', 'pierre/dupont')
