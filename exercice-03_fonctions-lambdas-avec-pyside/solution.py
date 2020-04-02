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

        button.clicked.connect(lambda: self.afficher_mot('Bonjour'))
        button2.clicked.connect(lambda: self.afficher_mot('Au Revoir'))

    def afficher_mot(self, mot):
        print(mot)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    win = MainUi()
    win.show()
    app.exec_()
