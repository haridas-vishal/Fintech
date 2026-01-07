import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 1. Create a tiny fake dataset
# Features: [user_id, amount, location_code]
data = {
    'user_id': [1, 2, 3, 4],
    'amount': [100, 10000, 150, 9000],
    'location_code': [1, 2, 1, 2],
    'is_fraud': [0, 1, 0, 1]
}
df = pd.DataFrame(data)

# 2. Train a dummy model
X = df[['user_id', 'amount', 'location_code']]
y = df['is_fraud']
model = RandomForestClassifier()
model.fit(X, y)

# 3. Save it to the 'model' folder
if not os.path.exists('model'):
    os.makedirs('model')

joblib.dump(model, 'model/fraud_model.pkl')
print("✅ Successfully created model/fraud_model.pkl")