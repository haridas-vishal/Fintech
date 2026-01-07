import os
import joblib

# Determine the absolute path to the model folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "model", "fraud_model.pkl")

# Load model if it exists, otherwise use a fallback
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("✅ ML Model loaded successfully.")
else:
    model = None
    print("⚠️ WARNING: fraud_model.pkl not found. Running in 'Mock Mode'.")

def ml_score(data):
    """
    Returns a fraud risk score. 
    If model is missing, returns a default score for testing.
    """
    if model:
        try:
            # Assuming the model takes a list of features
            return model.predict_proba([data])[0][1]
        except Exception:
            return 0.5
    
    # Fallback: if amount > 5000, give it a higher risk score
    amount = data.get("amount", 0)
    return 0.85 if amount > 5000 else 0.15