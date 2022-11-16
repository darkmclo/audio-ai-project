from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QFileDialog, QMessageBox, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt
import os
import sys 
import subprocess
import time

"""
class LoadWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.show()
"""

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,300)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)

        self.movie = QMovie('images/loading_screen.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)

        self.startAnimation()
        timer.singleShot(3000, self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('testgui.ui',self)
        self.btnImport.clicked.connect(self.browse_files)
        self.btnProcess.clicked.connect(self.process_files)
        self.btnGraphic.clicked.connect(self.show_graphic)

        self.loading_screen = LoadingScreen()
        self.show()

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
            current_timestamp = time.time()
            cmd_conda = "cd ~/spleeter && mkdir -p "+ str(current_timestamp) + " && . ~/miniconda3/etc/profile.d/conda.sh && conda activate && spleeter separate -o "+str(current_timestamp)+"/audio_output -p spleeter:5stems "+ str(filenameSel) +""
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

    def show_graphic(self):
        fig, ax1 = plt.subplots()
        plt.subplots_adjust(hspace=0)

        x = range(0, 10)
        y1 = range(0, 10)
        y2 = range(10, 0, -1)

        ax1.plot(y1, y2)
        ax1.set(xlabel="Tiempo",ylabel="Amplitud")

        plt.show()

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