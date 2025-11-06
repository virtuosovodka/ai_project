import pandas as pd #data manipulation
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold #dividing data, cross validation
from sklearn.ensemble import RandomForestClassifier #random forest classifier is the ML model
from sklearn.preprocessing import LabelEncoder #encode categorical variables
import numpy as np #numerical library

# Load data
df = pd.read_csv("fraudTrain.csv")

# Convert datetime columns to numeric features
df['trans_date_trans_time'] = pd.to_datetime(df['trans_date_trans_time'])
df['trans_hour'] = df['trans_date_trans_time'].dt.hour
df['trans_day'] = df['trans_date_trans_time'].dt.day
df['trans_month'] = df['trans_date_trans_time'].dt.month
df['trans_dayofweek'] = df['trans_date_trans_time'].dt.dayofweek

df['dob'] = pd.to_datetime(df['dob'])
df['age'] = (df['trans_date_trans_time'] - df['dob']).dt.days / 365.25

# Drop original datetime and personal identifier columns
df = df.drop(['trans_date_trans_time', 'dob', 'first', 'last', 'street', 'trans_num'], axis=1)

# Encode categorical variables using LabelEncoder
le_dict = {}
categorical_cols = ['merchant', 'category', 'gender', 'state', 'city', 'job']
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    le_dict[col] = le

# Prepare features and target
# Remove the index column and separate features from target
X = df.drop(["is_fraud", "Unnamed: 0"], axis=1)  # Fixed: space and colon
y = df["is_fraud"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1,
test_size=0.4)

# Random Forest does not require scaling
# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=1)
model.fit(X_train, y_train)

# Cross-validation
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=1)
cv_scores = cross_val_score(model, X_train, y_train, cv=cv, verbose=True)

print("\nCross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())

# Test set performance
test_accuracy = model.score(X_test, y_test)
print(f"Test Accuracy: {test_accuracy}")