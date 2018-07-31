import pandas as pd
from keras.models import load_model

model = load_model('trained_models/BoxingModel.h5')

# Prediction
X_pred = pd.read_csv('data/new_bout_scaled.csv').values

prediction = model.predict(X_pred)
prediction = prediction[0][0]

print("Predicted result: {}".format(prediction))