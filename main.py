import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('testgui.ui',self)
        self.btnImport.clicked.connect(self.browse_files)

    def browse_files(self):
        fname = QFileDialog.getOpenFileName(self,'Importar audio','/home','WAV audio *.wav')
        self.txtFilename.setText(fname[0])

app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.setFixedWidth(800)
mainwindow.setFixedHeight(600)
mainwindow.show()

app.exec_()

"""
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
sys.exit(app.exec_())
"""