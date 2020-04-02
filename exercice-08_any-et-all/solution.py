fichiers = ['C:/dossier_test/fichier01.jpg',
            'C:/dossier_test/fichier02.tif',
            'C:/dossier_test/fichier03.png',
            'C:/dossier_test/fichier04.jpg',
            'C:/dossier_test/fichier05.jpg']

au_moins_un_png = any(x.endswith('.png') for x in fichiers)
tous_des_jpg = all(x.endswith('.jpg') for x in fichiers)

print(au_moins_un_png)
print(tous_des_jpg)
