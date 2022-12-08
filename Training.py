#from google.colab import drive
#drive.mount('/content/drive')

import os
Root = "/home/chriss/Music_Genre_Classification"
os.chdir(Root)

import pandas as pd
import numpy as np
import os
import IPython.display as ipd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import tensorflow
#%matplotlib inline

audio_dataset_path='/home/chriss/Music_Genre_Classification/Data/genres_original'
metadata=pd.read_csv('/home/chriss/Music_Genre_Classification/Data/features_30_sec.csv')
metadata.head()

def features_extractor(file):
  audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
  mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
  mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)

  return mfccs_scaled_features

#metadata.drop(labels=554, axis=0, inplace=True)
#metadata.drop(labels=555, axis=0, inplace=True)

from tqdm import tqdm

extracted_features=[]
for index_num,row in tqdm(metadata.iterrows()):
  try:
    final_class_labels=row["label"]
    file_name = os.path.join(os.path.abspath(audio_dataset_path), final_class_labels+'/',str(row["filename"]))
    data = features_extractor(file_name)
    extracted_features.append([data,final_class_labels])
  except Exception as e:
    print(f"Error: {e}")
    continue

metadata.drop(labels=554, axis=0, inplace=True)
metadata.drop(labels=555, axis=0, inplace=True)

extracted_features_df=pd.DataFrame(extracted_features,columns=['feature','class'])
extracted_features_df.head()

extracted_features_df['class'].value_counts()

X=np.array(extracted_features_df['feature'].tolist())
y=np.array(extracted_features_df['class'].tolist())

X.shape

y.shape

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

X_train

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

import tensorflow as tf
print(tf.__version__)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.optimizers import Adam
from sklearn import metrics

num_labels = y.shape[1]

model = Sequential()
model.add(Dense(1024,input_shape=(40,), activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(32, activation="relu"))
model.add(Dropout(0.3))

# Capa final
model.add(Dense(num_labels, activation="softmax"))

model.summary()

model.compile(
    loss='categorical_crossentropy',
    metrics=['accuracy'],
    optimizer='adam'
)

import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

# Entrenamiento del modelo
from tensorflow.keras.callbacks import ModelCheckpoint
from datetime import datetime

num_epochs = 100
num_batch_size = 32

checkpointer = ModelCheckpoint(filepath=f'saved_models/audio_classification_{current_time}.hdf5', verbose=1, save_best_only=True)
start = datetime.now()

history = model.fit(X_train, y_train, batch_size=num_batch_size, epochs=num_epochs, validation_data=(X_test, y_test), callbacks=[checkpointer], verbose=1)

duration = datetime.now() - start
print("El Entrenamiento duró: ", duration)

model.evaluate(X_test,y_test,verbose=0)

pd.DataFrame(history.history).plot(figsize=(12,6))
plt.show()

#model.predict(X_test)
np.argmax(model.predict(X_test), axis=-1)

filename='/home/chriss/Music_Genre_Classification/Data/genres_original/country/country.00091.wav'
audio, sample_rate = librosa.load(filename, res_type='kaiser_fast')
mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)

print(mfccs_scaled_features)
mfccs_scaled_features = mfccs_scaled_features.reshape(1,-1)
print(mfccs_scaled_features)
print(mfccs_scaled_features.shape)
#predicted_label = model.predict_classes(mfccs_scaled_features)
predicted_label = np.argmax(model.predict(mfccs_scaled_features), axis=-1)
print(predicted_label)
prediction_class = labelencoder.inverse_transform(predicted_label)
prediction_class

print("El género musical del archivo es: "+str(prediction_class[0]))