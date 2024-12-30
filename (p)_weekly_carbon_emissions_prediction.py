# -*- coding: utf-8 -*-
"""(P) Weekly Carbon Emissions Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OAyUUMWIVKTt_q45aMvKfXyBChgYpVcu
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = pd.read_csv("New Data.csv")

# Extract the emissions data
emissions = data['Emisi'].values

data.head()

data.info()

data.describe()

# Plot the data
x=data['Minggu']
y=data['Emisi']
plt.plot(y, label='Emisi')
plt.xlabel('Weeks')
plt.ylabel('Carbon Emissions')
plt.legend()
plt.show()

# Normalize the data
scaler = MinMaxScaler()
emissions = scaler.fit_transform(emissions.reshape(-1, 1))

def create_sequences(data, seq_length):
    sequences = []
    target = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i+seq_length])
        target.append(data[i+seq_length])
    return np.array(sequences), np.array(target)

seq_length = 4
sequences, target = create_sequences(emissions, seq_length)
X_train, X_test, y_train, y_test = train_test_split(sequences, target, test_size=0.2, random_state=42)

print(X_train.shape[0])
print(X_test.shape[0])
print(y_train.shape[0])
print(y_test.shape[0])

# Define the LSTM model
model = keras.Sequential()
model.add(keras.layers.LSTM(256, activation='relu', return_sequences=True, input_shape=(seq_length, 1)))
model.add(keras.layers.LSTM(128, activation='relu', return_sequences=True))
model.add(keras.layers.LSTM(64, activation='relu', return_sequences=False))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(1))

model.summary()

model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-3), loss='mean_squared_error')
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test), shuffle=False)

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

# Predict emissions for the test data
y_pred = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')

plt.plot(y_test, label='Actual Emissions')
plt.plot(y_pred, label='Predicted Emissions')
plt.xlabel('Weeks')
plt.ylabel('Carbon Emissions')
plt.legend()
plt.show()

act = []
pred = []

i=10
Xt = model.predict(X_test[i].reshape(1,4,1))
print('predicted:{0}, actual:{1}'.format(scaler.inverse_transform(Xt),scaler.inverse_transform(y_test[i].reshape(-1,1))))
pred.append(scaler.inverse_transform(Xt))
act.append(scaler.inverse_transform(y_test[i].reshape(-1,1)))

def predict(model, week):
  scaler=MinMaxScaler()
  weeks = np.array(week)
  weeks = scaler.fit_transform(weeks.reshape(-1,1))
  totalweeks = weeks.reshape(1,4,1)

  pred = model.predict(totalweeks)

  prediksi = scaler.inverse_transform(pred).flatten()

  print("Prediksi emisi karbon anda pada minggu selanjutnya sebesar: ", prediksi)

  return prediksi

week = [[45879, 41236, 41562, 43947]]
predict(model, week)

tf.keras.models.save_model(model, 'prediksi_emisi_mingguan.h5')

loaded_model = tf.keras.models.load_model('./prediksi_emisi_mingguan.h5')

week = [84743, 93845, 87362, 85236]
predict(loaded_model, week)