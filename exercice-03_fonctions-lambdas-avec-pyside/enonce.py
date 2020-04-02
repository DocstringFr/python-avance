"""
Le but de l'exercice est d'afficher le mot 'Bonjour'
a l'aide de la methode 'afficher_mot' quand on clique sur
le bouton 'Print Bonjour!' et d'afficher 'Au revoir' quand
on clique sur le bouton 'Print Au Revoir!'
"""

from PySide import QtGui, QtCore


class MainUi(QtGui.QWidget):
    def __init__(self):
        super(MainUi, self).__init__()

        self.setWindowTitle('Printer')

        main_layout = QtGui.QHBoxLayout(self)
        button = QtGui.QPushButton('Print Bonjour!')
        button2 = QtGui.QPushButton('Print Au revoir!')
        main_layout.addWidget(button)
        main_layout.addWidget(button2)

        button.clicked.connect('INSERER CODE ICI')
        button2.clicked.connect('INSERER CODE ICI')

    def afficher_mot(self, mot):
        print(mot)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    win = MainUi()
    win.show()
    app.exec_()
