import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import *

RUN_NAME = "run with 50 nodes"

# Read training data
training_data_df = pd.read_csv('data/boxing_data_training_scaled.csv')

X = training_data_df.drop('result', axis=1).values
Y = training_data_df[['result']].values

# Define the Neural Network
model = Sequential()
model.add(Dense(50, input_dim=20, activation='relu', name='layer_1'))
model.add(Dense(100, activation='relu', name='layer_2'))
model.add(Dense(50, activation='relu', name='layer_3'))
model.add(Dense(1, activation='linear', name='layer_output'))

# Model Compiler
model.compile(loss="mean_squared_error", optimizer='adam')

# TensorBoard Callback
logger = keras.callbacks.TensorBoard(
    log_dir='logs/{}'.format(RUN_NAME),
    write_graph=True,
    histogram_freq=0
)

# Train the Model
model.fit(
    X,
    Y,
    epochs=50,
    shuffle=True,
    verbose=2,
    callbacks=[logger]
)

# Read test data
test_data_df = pd.read_csv('data/boxing_data_test_scaled.csv')

X_test = test_data_df.drop('result', axis=1).values
Y_test = test_data_df[['result']].values

# Evaluate the model
test_error_rate = model.evaluate(X_test, Y_test, verbose=0)
print("The mean squared error (MSE) for the test data set is: {}".format(test_error_rate))

# Save the model
model.save('trained_models/BoxingModel.h5')
print("\n== Model saved on disk ==")

