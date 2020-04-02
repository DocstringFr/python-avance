import os
from pprint import pprint

cur_dir = os.path.dirname(__file__)

dossier_rendu_01 = os.path.join(cur_dir, 'rendus_01')
dossier_rendu_02 = os.path.join(cur_dir, 'rendus_02')

fichiers_01 = os.listdir(dossier_rendu_01)
fichiers_02 = os.listdir(dossier_rendu_02)

fichiers_rendus = set(fichiers_01) | set(fichiers_02)
toutes_les_images = set([str(i).zfill(4) + '.jpg' for i in range(1, 101)])

images_manquantes = toutes_les_images - fichiers_rendus
pprint(sorted(list(images_manquantes)))
