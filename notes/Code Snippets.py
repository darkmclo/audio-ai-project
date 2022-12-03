#Crear directorio con variable de tiempo actual:
import time
current_timestamp = time.time()
cmd = "mkdir -p "+ str(current_timestamp) + ""

#Clase de Gráficos (embebible dentro del programa):
class graficos(FigureCanvas):
    def __init__(self, dir_file: str):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        audio_files = glob(dir_file)

        audio, sfreq = lr.load(audio_files[0])
        time = np.arange(0, len(audio)) / sfreq

        self.ax.plot(time,audio)
        self.ax.set(xlabel="Tiempo",ylabel="Amplitud")

#Clase de Gráficos con Hardcoding (Data manual)
class graphic_1(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),sharey=True, facecolor='white')
        super().__init__(self.fig)

        nombres = ['15','25','30','35','40']
        colores = ['red','red','red','red','red']
        tamaño = [10,15,20,25,30]

        self.ax.bar(nombres,tamaño,color = colores)
        #self.fig.suptitle('Gráfica',size=9)