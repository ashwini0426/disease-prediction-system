import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("datasets/disease_dataset.csv")

# Features and target
X = data.drop("disease", axis=1)
y = data["disease"]

# Better model
model = RandomForestClassifier(n_estimators=200, random_state=42)

# Train
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

# Save column order
joblib.dump(list(X.columns), "symptoms.pkl")

print("Model trained successfully")