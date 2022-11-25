from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QFileDialog, QMessageBox, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
import sys 
import subprocess
import time
import os.path
from pathlib import Path

import numpy as np
from glob import glob as glob
import librosa as lr

"""
class LoadWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.show()
"""

global filenameSel

class graficos(FigureCanvas):
    def __init__(self, dir_file: str):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        audio_files = glob(dir_file)

        audio, sfreq = lr.load(audio_files[0])
        time = np.arange(0, len(audio)) / sfreq

        self.ax.plot(time,audio)
        self.ax.set(xlabel="Tiempo",ylabel="Amplitud")


class graphic_1(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),sharey=True, facecolor='white')
        super().__init__(self.fig)

        nombres = ['15','25','30','35','40']
        colores = ['red','red','red','red','red']
        tamaño = [10,15,20,25,30]

        self.ax.bar(nombres,tamaño,color = colores)
        #self.fig.suptitle('Gráfica',size=9)

class graphic_2(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),sharey=True, facecolor='gray')
        super().__init__(self.fig)

        nombres = ['10','5','7','15','20','60','30','14','17','35','20','18']
        colores = ['blue','blue','blue','blue','blue']
        tamaño = [10,5,7,15,20,60,30,14,17,35,20,18]

        self.ax.bar(nombres,tamaño,color = colores)
        #self.fig.suptitle('Gráfica',size=9)

class graphic_3(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),sharey=True, facecolor='white')
        super().__init__(self.fig)

        nombres = ['41','19','31','9','7','14','69']
        colores = ['green','green','green','green','green']
        tamaño = [41,19,31,9,7,14,69]

        self.ax.bar(nombres,tamaño,color = colores)
        #self.fig.suptitle('Gráfica',size=9)

class graphic_4(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),sharey=True, facecolor='gray')
        super().__init__(self.fig)

        nombres = ['10','15','20','25','30','25','20','15','10']
        colores = ['cyan','skyblue','cyan','skyblue','cyan','skyblue','cyan','skyblue','cyan']
        tamaño = [10,15,20,25,30,25,20,15,10]

        self.ax.bar(nombres,tamaño,color = colores)
        #self.fig.suptitle('Gráfica',size=9)

class graphic_5(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),sharey=True, facecolor='white')
        super().__init__(self.fig)

        nombres = ['15','25','30','35','40']
        colores = ['red','red','red','red','red']
        tamaño = [10,15,20,25,30]

        self.ax.bar(nombres,tamaño,color = colores)
        self.fig.suptitle('Gráfica',size=9)

class ImportScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('import_gui.ui',self)

        global filenameSel
        filenameSel = ""
        self.btnImport.clicked.connect(self.browse_files)
        self.btnProcess.clicked.connect(self.process_files)
        self.btnTest.clicked.connect(self.abrirVentana)

        self.show()

    def show_graphic_on_window(self):
        fig, ax1 = plt.subplots()
        plt.subplots_adjust(hspace=0)

        x = range(0, 10)
        y1 = range(0, 10)
        y2 = range(10, 0, -1)

        ax1.plot(y1, y2)
        ax1.set(xlabel="Tiempo",ylabel="Amplitud")

    def abrirVentana(self):
        #self.loading_screen = LoadingScreen()
        #self.loading_screen.show()
        current_dir = os.getcwd()
        print(current_dir)

        self.main_screen = MainWindow()
        dir_file = "/home/chriss/spleeter/vocals.wav"
        dir_file2 = "/home/chriss/spleeter/vocals.wav"
        self.canvas_alternative = graficos(dir_file)
        self.canvas_2 = graficos(dir_file)
        self.canvas_3 = graphic_3()
        self.canvas_4 = graphic_4()

        #self.main_screen.label_7.setPixmap(self.canvas)
        #self.main_screen.frame_grafic_1.addWidget(self.canvas_1)
        #scroll_layout_1 = QtWidgets.QVBoxLayout(self)

        self.main_screen.frame_graphic_1.addWidget(self.canvas_alternative)
        self.main_screen.frame_graphic_2.addWidget(self.canvas_2)
        self.main_screen.frame_graphic_3.addWidget(self.canvas_3)
        self.main_screen.frame_graphic_4.addWidget(self.canvas_4)
        self.main_screen.show()

        self.cerrarVentana()

    """
    def graphic_1(FigureCanvas):
        def __init__(self, parent=None):
            self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),sharey=True, facecolor='white')
            super().__init__(self.fig)

            nombres = ['15','25','30','35','40']
            colores = ['red','red','red','red','red']
            tamaño = [10,15,20,25,30]

            self.ax.bar(nombres,tamaño,color = colores)
            self.fig.suptitle('Gráfica',size=9)
    """

    def cerrarVentana(self):
        self.close()

    def browse_files(self):
        global filenameSel
        fname = QFileDialog.getOpenFileName(self,'Importar audio','/home',"Archivos de audio (*.wav *.mp3)")
        self.txtFilename.setText(fname[0])
        #filenameSel = self.txtFilename.text()

    def process_files(self):
        filenameSel = self.txtFilename.text()
        if filenameSel:
            self.close()
            self.loading_screen = LoadingScreen()
            self.loading_screen.show()
            
            print("Contenido de la variable con el archivo seleccionado: "+ str(filenameSel))
            self.main_screen = MainWindow()
            self.main_screen.backend_processing(filenameSel)
            self.loading_screen.close()
            #self.backend_thread(filenameSel)
            #self.main_screen.show()
            
            #self.main_screen.backend_processing(filenameSel)
            #self.loading_screen.backend_processing()
        else:
            self.show_dialog()

    def backend_thread(self, filenameSel: str):
        t1=Thread(target=self.main_screen.backend_processing(filenameSel))
        t1.start()

    def backend_worker(self, filenameSel: str):
        self.thread[1] = ThreadClass(parent=None,index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.main_screen.backend_processing(filenameSel))

    def show_dialog(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Mensaje")
        dialog.setText("Ocurrió un error. Seleccione el archivo correcto.")
        dialog.exec_()


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('loading_gui.ui',self)

        loading_gif = QMovie('images/loading_screen.gif')
        self.lbl_gif.setMovie(loading_gif)
        loading_gif.start()

        #global filenameSel

        """
        self.setFixedSize(300,300)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)

        self.movie = QMovie('images/loading_screen.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)

        self.startAnimation()
        timer.singleShot(3000, self.stopAnimation)


        """
        #self.backend_processing()

    """

    def backend_processing(self):
        if filenameSel:
            current_timestamp = time.time()
            cmd_conda = ("cd ~ "
            +"&& mkdir -p spleeter "+
            "&& cd spleeter "+
            "&& . ~/miniconda3/etc/profile.d/conda.sh "+
            "&& conda activate "+
            "&& spleeter separate -o "+str(current_timestamp)+" -p spleeter:5stems '"+ str(filenameSel) +"'")
            stdouterr = os.popen(cmd_conda).read()
            cmd_output = "/home/chriss/spleeter/"+str(current_timestamp)+""
            print(cmd_output)
            estado_archivo = os.path.isdir(cmd_output)
            print("Folder flag: "+str(estado_archivo))

            if estado_archivo == True:
                self.close()
                #Abrir ventana principal
                self.main_screen = MainWindow()
                self.main_screen.show()
            else:
                self.show_dialog()
                self.close()
            #self.lblOutput.setText("Archivo procesado")
            #subprocess.call("spleeter separate -o audio_output -p spleeter:5stems "+ str(fname))
        else:
            self.show_dialog()

    """
    def show_dialog(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Mensaje")
        dialog.setText("Ocurrió un error.")
        dialog.exec_()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('testgui.ui',self)
        #self.btnImport.clicked.connect(self.browse_files)
        #self.btnProcess.clicked.connect(self.process_files)
        #self.btnGraphic.clicked.connect(self.show_graphic)

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
            cmd_conda = "cd ~/spleeter && . ~/miniconda3/etc/profile.d/conda.sh && conda activate && spleeter separate -o "+str(current_timestamp)+"/audio_output -p spleeter:5stems "+ str(filenameSel) +""
            stdouterr = os.popen(cmd_conda).read()
            self.lblOutput.setText("Archivo procesado")
            #subprocess.call("spleeter separate -o audio_output -p spleeter:5stems "+ str(fname))
        else:
            self.show_dialog()

    def process_files_test(self):
        filenameSel = ""
        if filenameSel:
            cmd_test = ("cd ~/spleeter "+
                "&& . ~/miniconda3/etc/profile.d/conda.sh "+
                "&& conda activate "+
                "&& spleeter separate -o audio_output -p spleeter:5stems /home/chriss/projects/audio-ai-project/audio.wav")
            subprocess.call(cmd_test, shell=True, executable='/bin/sh')

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

    def backend_processing(self,filenameSel: str):
        if filenameSel:
            print("Procesando...")
            current_timestamp = time.time()
            current_dir = os.getcwd()
            cmd_conda = ("cd ~ "
            +"&& mkdir -p spleeter "+
            "&& cd spleeter "+
            "&& . ~/miniconda3/etc/profile.d/conda.sh "+
            "&& conda activate "+
            "&& spleeter separate -o "+str(current_timestamp)+" -p spleeter:5stems '"+ str(filenameSel) +"'")
            stdouterr = os.popen(cmd_conda).read()
            home_folder = str(Path.home())
            cmd_output = str(home_folder) + "/spleeter/"+str(current_timestamp)+""
            print(cmd_output)
            estado_new_directorio = os.path.isdir(cmd_output)
            print("Folder flag: "+str(estado_new_directorio))

            if estado_new_directorio == True:
                #cmd_output_file1 = cmd_output + str(cmd_output)
                self.close()

                project_file_dir = str(cmd_output) + "/" + os.path.basename(filenameSel).split('.')[0]
                project_audio_1 = project_file_dir + "/" + "bass.wav"
                project_audio_2 = project_file_dir + "/" + "drums.wav"
                project_audio_3 = project_file_dir + "/" + "other.wav"
                project_audio_4 = project_file_dir + "/" + "piano.wav"
                project_audio_5 = project_file_dir + "/" + "vocals.wav"
                #Abrir ventana principal
                self.main_screen = MainWindow()

                #Gráfico 1
                self.main_screen.filelocation_1.setText(project_audio_1)
                self.canvas_1 = graficos(project_audio_1)
                self.main_screen.frame_graphic_1.addWidget(self.canvas_1)

                self.main_screen.filelocation_2.setText(project_audio_2)

                self.main_screen.filelocation_3.setText(project_audio_3)
                
                self.main_screen.filelocation_4.setText(project_audio_4)
                self.main_screen.show()
            else:
                self.show_dialog("Un error ha ocurrido")
                self.close()
            #self.lblOutput.setText("Archivo procesado")
            #subprocess.call("spleeter separate -o audio_output -p spleeter:5stems "+ str(fname))
        else:
            self.show_dialog("Ocurrió un error al procesar el elemento.")
            print("Contenido de la variable: " + str(filenameSel))

    def show_dialog(self,message: str):
        dialog = QMessageBox()
        dialog.setWindowTitle("Mensaje")
        dialog.setText(message)
        dialog.exec_()

if __name__=='__main__':
    app = QApplication(sys.argv)
    widget_import = ImportScreen()
    widget_import.show()
    app.exec_()

"""
mainwindow = LoadingScreen()
mainwindow.setFixedWidth(800)
mainwindow.setFixedHeight(600)
mainwindow.show()
"""



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