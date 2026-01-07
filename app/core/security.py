from datetime import datetime, timedelta
from jose import jwt

SECRET = "SECRET_KEY"
ALGO = "HS256"

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=30)
    return jwt.encode(payload, SECRET, algorithm=ALGO)
