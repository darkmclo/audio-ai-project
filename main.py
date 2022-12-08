from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QFileDialog, QMessageBox, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QTimer, QThread
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
import webbrowser
import speech_recognition as sr

import numpy as np
from glob import glob as glob
import librosa as lr
import librosa.display

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

class cargar_espectrograma(FigureCanvas):
    def __init__(self, filename: str):
        y, sr = lr.load(filename)
        D = lr.amplitude_to_db(np.abs(lr.stft(y)), ref=np.max)
        self.fig, self.ax = plt.subplots(figsize=(15, 3))
        super().__init__(self.fig)
        img = lr.display.specshow(D, y_axis='log', x_axis='time', sr=sr)
        self.ax.label_outer()
        #plt.colorbar()

class graphic_1(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),sharey=True, facecolor='white')
        super().__init__(self.fig)

        nombres = ['15','25','30','35','40']
        colores = ['red','red','red','red','red']
        tamaño = [10,15,20,25,30]

        self.ax.bar(nombres,tamaño,color = colores)
        #self.fig.suptitle('Gráfica',size=9)


class WorkerThread(QThread):
    def run(self):
        self.backend_processing("/home/chriss/projects/audio-ai-project/audio_samples/set_a/My_December_Clip.mp3")

    def backend_process(self):
        print("Se ha comenzado el proceso de backend personalizado.")
        for x in range(1000000):
            print(x)

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
                #self.close()

                #Files
                project_file_dir = str(cmd_output) + "/" + os.path.basename(filenameSel).split('.')[0]
                
                project_audio_1 = project_file_dir + "/" + "bass.wav"
                print("bass.wav: "+str(project_audio_1))

                project_audio_2 = project_file_dir + "/" + "drums.wav"
                print("drums.wav: "+str(project_audio_2))

                project_audio_3 = project_file_dir + "/" + "other.wav"
                print("other.wav: "+str(project_audio_3))

                project_audio_4 = project_file_dir + "/" + "piano.wav"
                print("piano.wav: "+str(project_audio_4))

                project_audio_5 = project_file_dir + "/" + "vocals.wav"
                print("vocals.wav: "+str(project_audio_5))

                ### VENTANA
                #Abrir ventana principal
                self.main_screen = MainWindow()

                self.main_screen.label_file.setText(os.path.basename(filenameSel))

                #Gráfico 1
                self.main_screen.filelocation_1.setText(project_audio_1)
                self.main_screen.filelocation_1.setEnabled(False)
                self.canvas_1 = graficos(project_audio_1)
                self.main_screen.frame_graphic_1.addWidget(self.canvas_1)

                #Grafico 2
                self.main_screen.filelocation_2.setText(project_audio_2)
                self.main_screen.filelocation_2.setEnabled  (False)
                self.canvas_2 = graficos(project_audio_2)
                self.main_screen.frame_graphic_2.addWidget(self.canvas_2)

                #Grafico 3
                self.main_screen.filelocation_3.setText(project_audio_3)
                self.main_screen.filelocation_3.setEnabled(False)
                self.canvas_3 = graficos(project_audio_3)
                self.main_screen.frame_graphic_3.addWidget(self.canvas_3)

                #Grafico 4
                self.main_screen.filelocation_4.setText(project_audio_4)
                self.main_screen.filelocation_4.setEnabled(False)
                self.canvas_4 = graficos(project_audio_4)
                self.main_screen.frame_graphic_4.addWidget(self.canvas_4)

                #Grafico 5
                self.main_screen.filelocation_5.setText(project_audio_5)
                self.main_screen.filelocation_5.setEnabled(False)
                self.canvas_5 = graficos(project_audio_5)
                self.main_screen.frame_graphic_5.addWidget(self.canvas_5)

                #Boton de Proyecto
                self.main_screen.btnFolder.clicked.connect(lambda: self.open_folder(project_file_dir))
                #self.main_screen.btnGenSpectrum.clicked.connect(lambda: cargar_espectrograma(project_audio_1))

                #self.spectrogram_screen = GraphicScreen()
                #self.spectro_canvas = cargar_espectrograma(project_audio_5)
                #self.spectrogram_screen.spectrogramLayout.addWidget(self.spectro_canvas)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                #self.main_screen.btnGenSpectrum.clicked.connect(self.spectrogram_screen.show)

                #Spectogram Bass
                self.spectrogram_screen_2 = GraphicScreen()
                self.spectro_canvas_2 = cargar_espectrograma(project_audio_1)
                self.spectrogram_screen_2.spectrogramLayout.addWidget(self.spectro_canvas_2)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumBass.clicked.connect(self.spectrogram_screen_2.show)

                #Spectogram Drums
                self.spectrogram_screen_3 = GraphicScreen()
                self.spectro_canvas_3 = cargar_espectrograma(project_audio_2)
                self.spectrogram_screen_3.spectrogramLayout.addWidget(self.spectro_canvas_3)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumDrums.clicked.connect(self.spectrogram_screen_3.show)

                #Spectogram Other
                self.spectrogram_screen_4 = GraphicScreen()
                self.spectro_canvas_4 = cargar_espectrograma(project_audio_3)
                self.spectrogram_screen_4.spectrogramLayout.addWidget(self.spectro_canvas_4)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumOther.clicked.connect(self.spectrogram_screen_4.show)

                #Spectogram Piano
                self.spectrogram_screen_5 = GraphicScreen()
                self.spectro_canvas_5 = cargar_espectrograma(project_audio_4)
                self.spectrogram_screen_5.spectrogramLayout.addWidget(self.spectro_canvas_5)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumPiano.clicked.connect(self.spectrogram_screen_5.show)

                #Spectogram Vocals
                self.spectrogram_screen_6 = GraphicScreen()
                self.spectro_canvas_6 = cargar_espectrograma(project_audio_5)
                self.spectrogram_screen_6.spectrogramLayout.addWidget(self.spectro_canvas_6)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumVocals.clicked.connect(self.spectrogram_screen_6.show)

                self.main_screen.btnSpeechReg.clicked.connect(lambda: self.text_to_speech(project_audio_5))

                #self.main_screen.btnGenSpectrum.clicked.connect(self.show_graphic())
                self.main_screen.show()
            else:
                self.show_dialog("Un error ha ocurrido")
                #self.close()
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

class ImportScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('import_gui.ui',self)

        global filenameSel
        filenameSel = ""
        self.btnImport.clicked.connect(self.browse_files)
        self.btnProcess.clicked.connect(self.process_files)
        self.btnTest.clicked.connect(self.evt_btnStartProcessing)

        self.show()

    """
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    """

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

    def evt_btnStartProcessing(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.evt_btnFinishedProcessing)

    def evt_btnFinishedProcessing(self):
        QMessageBox.information(self, "Finalizado.","Se ha realizado el proceso.")

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
            
            print("Dirección del archivo seleccionado: "+ str(filenameSel))
            self.main_screen = MainWindow()
            self.main_screen.backend_processing(filenameSel)
            self.loading_screen.close()
            #self.backend_thread(filenameSel)
            #self.main_screen.show()
            
            #self.main_screen.backend_processing(filenameSel)
            #self.loading_screen.backend_processing()
        else:
            self.show_dialog()

    def process_files_testing(self):
        filenameSel = self.txtFilename.text()
        if filenameSel:
            self.close()
            self.loading_screen = LoadingScreen()
            self.loading_screen.show()
            
            print("Dirección del archivo seleccionado: "+ str(filenameSel))
            self.main_screen = MainWindow()
            self.evt_btnStartProcessing()
            self.loading_screen.close()
            #self.backend_thread(filenameSel)
            self.main_screen.show()
            
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

    """
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    """

class GraphicScreen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('spectrogram.ui',self)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('main.ui',self)
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

    def load_spectrogram(self,filename:str):
        y, sr = lr.load(filename)
        D = lr.amplitude_to_db(np.abs(lr.stft(y)), ref=np.max)
        fig, ax = plt.subplots(figsize=(15, 3))
        img = lr.display.specshow(D, y_axis='log', x_axis='time', sr=sr)
        ax.set(title='Logarithmic-frequency power spectrogram')
        ax.label_outer()
        plt.colorbar()
        plt.show()

    def text_to_speech(self,filename:str):
        if filename:
            r = sr.Recognizer()
            audio_file = sr.AudioFile(filename)
            with audio_file as source:
                #print("Start talking: ")
                r.adjust_for_ambient_noise(source)
                audio = r.record(source)
                #print("Stop talking.")
            try:
                text = r.recognize_google(audio, language='en-US') #, show_all=True
                print(text)
                self.show_dialog(str(text))
            except Exception as e:
                #print("I am here")
                print (e)
        else:
            self.show_dialog("No se puede reconocer el archivo de audio para obtener el texto.")

    def show_graphic(self):
        fig, ax1 = plt.subplots()
        plt.subplots_adjust(hspace=0)

        x = range(0, 10)
        y1 = range(0, 10)
        y2 = range(10, 0, -1)

        ax1.plot(y1, y2)
        ax1.set(xlabel="Tiempo",ylabel="Amplitud")

        plt.show()

    def open_folder(self,file_dir:str):
        webbrowser.open(file_dir)

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

                #Files
                project_file_dir = str(cmd_output) + "/" + os.path.basename(filenameSel).split('.')[0]
                
                project_audio_1 = project_file_dir + "/" + "bass.wav"
                print("bass.wav: "+str(project_audio_1))

                project_audio_2 = project_file_dir + "/" + "drums.wav"
                print("drums.wav: "+str(project_audio_2))

                project_audio_3 = project_file_dir + "/" + "other.wav"
                print("other.wav: "+str(project_audio_3))

                project_audio_4 = project_file_dir + "/" + "piano.wav"
                print("piano.wav: "+str(project_audio_4))

                project_audio_5 = project_file_dir + "/" + "vocals.wav"
                print("vocals.wav: "+str(project_audio_5))

                #Abrir ventana principal
                self.main_screen = MainWindow()

                self.main_screen.label_file.setText(os.path.basename(filenameSel))

                #Gráfico 1
                self.main_screen.filelocation_1.setText(project_audio_1)
                self.main_screen.filelocation_1.setEnabled(False)
                self.canvas_1 = graficos(project_audio_1)
                self.main_screen.frame_graphic_1.addWidget(self.canvas_1)

                #Grafico 2
                self.main_screen.filelocation_2.setText(project_audio_2)
                self.main_screen.filelocation_2.setEnabled  (False)
                self.canvas_2 = graficos(project_audio_2)
                self.main_screen.frame_graphic_2.addWidget(self.canvas_2)

                #Grafico 3
                self.main_screen.filelocation_3.setText(project_audio_3)
                self.main_screen.filelocation_3.setEnabled(False)
                self.canvas_3 = graficos(project_audio_3)
                self.main_screen.frame_graphic_3.addWidget(self.canvas_3)

                #Grafico 4
                self.main_screen.filelocation_4.setText(project_audio_4)
                self.main_screen.filelocation_4.setEnabled(False)
                self.canvas_4 = graficos(project_audio_4)
                self.main_screen.frame_graphic_4.addWidget(self.canvas_4)

                #Grafico 5
                self.main_screen.filelocation_5.setText(project_audio_5)
                self.main_screen.filelocation_5.setEnabled(False)
                self.canvas_5 = graficos(project_audio_5)
                self.main_screen.frame_graphic_5.addWidget(self.canvas_5)

                #Boton de Proyecto
                self.main_screen.btnFolder.clicked.connect(lambda: self.open_folder(project_file_dir))
                #self.main_screen.btnGenSpectrum.clicked.connect(lambda: cargar_espectrograma(project_audio_1))

                #self.spectrogram_screen = GraphicScreen()
                #self.spectro_canvas = cargar_espectrograma(project_audio_5)
                #self.spectrogram_screen.spectrogramLayout.addWidget(self.spectro_canvas)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                #self.main_screen.btnGenSpectrum.clicked.connect(self.spectrogram_screen.show)

                #Spectogram Bass
                self.spectrogram_screen_2 = GraphicScreen()
                self.spectro_canvas_2 = cargar_espectrograma(project_audio_1)
                self.spectrogram_screen_2.spectrogramLayout.addWidget(self.spectro_canvas_2)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumBass.clicked.connect(self.spectrogram_screen_2.show)

                #Spectogram Drums
                self.spectrogram_screen_3 = GraphicScreen()
                self.spectro_canvas_3 = cargar_espectrograma(project_audio_2)
                self.spectrogram_screen_3.spectrogramLayout.addWidget(self.spectro_canvas_3)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumDrums.clicked.connect(self.spectrogram_screen_3.show)

                #Spectogram Other
                self.spectrogram_screen_4 = GraphicScreen()
                self.spectro_canvas_4 = cargar_espectrograma(project_audio_3)
                self.spectrogram_screen_4.spectrogramLayout.addWidget(self.spectro_canvas_4)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumOther.clicked.connect(self.spectrogram_screen_4.show)

                #Spectogram Piano
                self.spectrogram_screen_5 = GraphicScreen()
                self.spectro_canvas_5 = cargar_espectrograma(project_audio_4)
                self.spectrogram_screen_5.spectrogramLayout.addWidget(self.spectro_canvas_5)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumPiano.clicked.connect(self.spectrogram_screen_5.show)

                #Spectogram Vocals
                self.spectrogram_screen_6 = GraphicScreen()
                self.spectro_canvas_6 = cargar_espectrograma(project_audio_5)
                self.spectrogram_screen_6.spectrogramLayout.addWidget(self.spectro_canvas_6)
                #self.main_screen.btnGenSpectrum.clicked.connect()

                self.main_screen.btnGenSpectrumVocals.clicked.connect(self.spectrogram_screen_6.show)

                self.main_screen.btnSpeechReg.clicked.connect(lambda: self.text_to_speech(project_audio_5))

                #self.main_screen.btnGenSpectrum.clicked.connect(self.show_graphic())
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