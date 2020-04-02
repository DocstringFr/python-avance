import os

cur_dir = os.path.dirname(__file__)

dossier_rendu_01 = os.path.join(cur_dir, 'rendus_01')
dossier_rendu_02 = os.path.join(cur_dir, 'rendus_02')

fichiers_01 = os.listdir(dossier_rendu_01)
fichiers_02 = os.listdir(dossier_rendu_02)

# INSERER CODE ICI