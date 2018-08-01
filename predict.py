import pandas as pd
from keras.models import load_model

model = load_model('trained_models/BoxingModel200.h5')

# Prediction
X_pred = pd.read_csv('data/new_bout_scaled.csv').values

prediction = model.predict(X_pred)[0]

res_A = prediction[0]
res_B = prediction[1]
res_T = prediction[2]

# Print result
print("Change for Fighter A: {}%".format(round(res_A * 100, 2)))
print("Change for Fighter B: {}%".format(round(res_B * 100, 2)))
print("Change for Tie: {}%".format(round(res_T * 100, 2)))