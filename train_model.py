import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv("train (1).csv")

# Encode categorical columns if needed
label_cols = ['ChassisType', 'PowerPlatformRole']  # encode if they're strings

for col in label_cols:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

# Define features and target
X = df[[
    'TotalPhysicalRAMMB',
    'ProcessorCoreCount',
    'ChassisType',
    'IsSystemProtected',
    'IsGamer',
    'PowerPlatformRole'
]]

y = df['target']  # this is your target column

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'threat_model.pkl')
print("✅ Model trained and saved as 'threat_model.pkl'")
