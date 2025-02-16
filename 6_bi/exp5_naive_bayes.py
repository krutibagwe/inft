import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

data = {
    'outlook': ['sunny', 'sunny', 'overcast', 'rain', 'rain', 'rain', 'overcast', 'sunny', 'sunny', 'rain', 'sunny', 'overcast', 'overcast', 'rain'],
    'temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'wind': ['weak', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'strong'],
    'target': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

df = pd.DataFrame(data)

label_encoder_outlook = LabelEncoder()
label_encoder_temperature = LabelEncoder()
label_encoder_humidity = LabelEncoder()
label_encoder_wind = LabelEncoder()

df['outlook'] = label_encoder_outlook.fit_transform(df['outlook'])
df['temperature'] = label_encoder_temperature.fit_transform(df['temperature'])
df['humidity'] = label_encoder_humidity.fit_transform(df['humidity'])
df['wind'] = label_encoder_wind.fit_transform(df['wind'])

label_encoder_target = LabelEncoder()
df['target'] = label_encoder_target.fit_transform(df['target'])

X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

sample_data = {  'outlook': 'sunny',  'temperature': 'cool',  'humidity': 'high',  'wind': 'strong' }

sample_df = pd.DataFrame([sample_data])

sample_df['outlook'] = label_encoder_outlook.transform(sample_df['outlook'])
sample_df['temperature'] = label_encoder_temperature.transform(sample_df['temperature'])
sample_df['humidity'] = label_encoder_humidity.transform(sample_df['humidity'])
sample_df['wind'] = label_encoder_wind.transform(sample_df['wind'])

predicted_class = model.predict(sample_df)
predicted_label = label_encoder_target.inverse_transform(predicted_class)
print(f"Predicted output for the new sample: {predicted_label[0]}")
