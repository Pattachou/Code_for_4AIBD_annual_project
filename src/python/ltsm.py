from keras.models import *
from keras.activations import *
from keras.layers import *
from keras.optimizers import *
from keras.losses import *
from keras.datasets import *
from keras.metrics import *
import numpy as np
import keras
import io
import csv
from keras.callbacks import *
import panda as pd


#### Variable globale
chemin = './dataset Process com.csv'
mode_ecriture = 'r'
name_logs = "linear_model"

##### Ouverture du dataset
file = open(chemin, mode_ecriture)
train_set=pd.read_csv(file, delimiter=',')
data = csv.reader(file)
### creation du dataset input et output
data_input = []
data_output = []

for row in data:
    data_input.append(row[0])
    print(row[0],int(row[1]))
    data_output.append(row[1])

#print(str(data_input[0:10])+"\n" +str(data_output[0:10]))
data_output = ''.join(str(e) for e in data_output)
data_output = keras.utils.to_categorical(data_output)


#construction du modele
#print('Build model...')
#model = Sequential()
#model.add(Embedding(output_dim=511))
#model.add(LSTM(6))
#model.add(Dropout(0.5))
#model.add(Dense(1, activation='sigmoid'))

#model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

#model.fit(data_input, data_output, batch_size=16, epochs=10,callbacks=[TensorBoard("./logs/" +name_logs )])