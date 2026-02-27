import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

def train_lstm(data):

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data["demand"].values.reshape(-1,1))

    X = []
    y = []

    for i in range(1, len(scaled)):
        X.append(scaled[i-1])
        y.append(scaled[i])

    X = np.array(X)
    y = np.array(y)

    X = X.reshape((X.shape[0], 1, 1))

    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(50, activation='tanh', input_shape=(1,1)),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=50, verbose=0)

    prediction = model.predict(X[-1].reshape(1,1,1))
    
    return int(scaler.inverse_transform(prediction)[0][0])