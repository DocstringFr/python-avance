from time import time
from random import randint
import os

cur_dir = os.path.dirname(__file__)
fichier = os.path.join(cur_dir, 'nombres_aleatoires.txt')

a = time()

nombres_aleatoires = []

for i in range(5000000):
    nombres_aleatoires.append(str(randint(0, 9999)))

with open(fichier, 'w') as f:
    f.write('\n'.join(nombres_aleatoires))

b = time()

print('Temps d\'execution: {}'.format(b - a))
