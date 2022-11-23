#Importar las librerias
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import ffmpeg as ff
import subprocess
from glob import glob

import librosa as lr

#Importar las libreŕías
data_dir = './audio-samples/set_a'

#command = subprocess.call("ffmpeg -i *.mp3 audio.wav",shell=True)
#print(command)
##subprocess.call(['ffmpeg', '-i', 'audio.mp3','audio.wav'])

audio_files = glob(data_dir + "/*.wav")

# Read in the first audio file, create the time array (timeline)
audio, sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq

fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel="Time (s)",ylabel="Sound Amplitude")
plt.show()