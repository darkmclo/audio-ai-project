from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.uic import loadUi
import os
import sys 
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('testgui.ui',self)
        self.btnImport.clicked.connect(self.browse_files)
        self.btnProcess.clicked.connect(self.process_files)

        global filenameSel
        filenameSel = ""

    def browse_files(self):
        fname = QFileDialog.getOpenFileName(self,'Importar audio','/home','WAV audio *.wav')
        self.txtFilename.setText(fname[0])
        global filenameSel
        filenameSel = self.txtFilename.text()
    
    def process_files(self):
        """
        cmd_conda = "cd ~/spleeter && . ~/miniconda3/etc/profile.d/conda.sh && conda activate && spleeter separate -o audio_output -p spleeter:5stems /home/chriss/projects/audio-ai-project/audio.wav"
        cmd = "conda activate && spleeter separate -o ~/audio_output -p spleeter:5stems "
        cmd_full = str(cmd) + str(self.txtFilename.text())
        cmd_test = "ls -l"
        stdouterr = os.popen(cmd_conda).read()
        """
        #self.lblOutput.setText(stdouterr)
        #subprocess.call("spleeter separate -o audio_output -p spleeter:5stems "+ str(self.txtFilename.text() ))
        if filenameSel:
            cmd_conda = "cd ~/spleeter && . ~/miniconda3/etc/profile.d/conda.sh && conda activate && spleeter separate -o audio_output -p spleeter:5stems "+ str(filenameSel) +""
            stdouterr = os.popen(cmd_conda).read()
            self.lblOutput.setText("Archivo procesado")
            #subprocess.call("spleeter separate -o audio_output -p spleeter:5stems "+ str(fname))
        else:
            self.show_dialog()

    def process_files_test(self):
        filenameSel = ""
        if filenameSel:
            cmd_test = "cd ~/spleeter && . ~/miniconda3/etc/profile.d/conda.sh && conda activate && spleeter separate -o audio_output -p spleeter:5stems /home/chriss/projects/audio-ai-project/audio.wav"
            subprocess.call(cmd_test, shell=True, executable='/bin/sh')
            #stdouterr = os.popen(cmd_test).read()
            #print(str(stdouterr))

            """
            cmd_test_2 = "spleeter"
            stdouterr_2 = os.popen(cmd_test_2).read()
            print(str(stdouterr_2))
            """

            self.lblOutput.setText("Archivo procesado")
            #subprocess.call("spleeter separate -o audio_output -p spleeter:5stems "+ str(fname))
        else:
            self.show_dialog()

    def show_dialog(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Mensaje de advertencia")
        dialog.setText("Por favor, seleccione un archivo.")
        dialog.exec_()

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