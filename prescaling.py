import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Read original data from Pandas
training_data_df = pd.read_csv('data/boxing_data_training.csv')
test_data_df = pd.read_csv('data/boxing_data_test.csv')
new_fight_df = pd.read_csv('data/new_bout.csv')

# Create the Scaler
scaler = MinMaxScaler(feature_range=(0, 1))

# Run the data through the scale. Fit the training first.
scaled_training = scaler.fit_transform(training_data_df)
scaled_test = scaler.transform(test_data_df)
scaled_new = scaler.transform(new_fight_df)
print("Note: total_earnings values were scaled by multiplying by {:.10f} and adding {:.6f}".format(scaler.scale_[8], scaler.min_[8]))

# Create new DataFrames from the scale and store them in new files
scaled_training_df = pd.DataFrame(scaled_training, columns=training_data_df.columns.values)
scaled_test_df = pd.DataFrame(scaled_test, columns=test_data_df.columns.values)
scaled_new_df = pd.DataFrame(scaled_new, columns=new_fight_df.columns.values)

scaled_training_df.to_csv("data/boxing_data_training_scaled.csv", index=False)
scaled_test_df.to_csv("data/boxing_data_test_scaled.csv", index=False)
scaled_new_df.to_csv("data/new_bout_scaled.csv", index=False)