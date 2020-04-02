from PySide import QtGui, QtCore


class MainUi(QtGui.QWidget):
    def __init__(self):
        super(MainUi, self).__init__()

        self.setWindowTitle('Calculatrice')

        main_layout = QtGui.QHBoxLayout(self)
        button = QtGui.QPushButton('Calcul')
        a = QtGui.QLineEdit('1')
        b = QtGui.QLineEdit('5')
        label_plus = QtGui.QLabel('+')
        c = QtGui.QLineEdit()
        label_egal = QtGui.QLabel('=')
        main_layout.addWidget(a)
        main_layout.addWidget(label_plus)
        main_layout.addWidget(b)
        main_layout.addWidget(label_egal)
        main_layout.addWidget(c)
        main_layout.addWidget(button)

        button.clicked.connect(lambda: c.setText(str(int(a.text()) + int(b.text()))))

        # Autre methode
        ra = a.text
        rb = b.text
        s = c.setText
        button.clicked.connect(lambda: s(str(int(ra()) + int(rb()))))


if __name__ == '__main__':
    app = QtGui.QApplication([])
    win = MainUi()
    win.show()
    app.exec_()
