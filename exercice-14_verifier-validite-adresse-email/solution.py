import re

adresses_mail = ['christian_martin@gmail.com',
                 'JaiOublieLarobasegmail.com',
                 'MarieHutchinson03523@yahoo.co.uk',
                 'UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com',
                 'ceciNestPasUneDresseMail']

for mail in adresses_mail:
    adresse_valide = re.search(r'.+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+', mail)
    print("L'adresse {} est {}".format(mail, 'valide' if adresse_valide else 'invalide'))
