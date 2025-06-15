import jwt
from functools import wraps
from flask import request, jsonify
import datetime

SECRET_KEY = 'your-secret-key'

# Dummy credentials
users = {"admin": "admin123"}

def authenticate(username, password):
    return users.get(username) == password

def generate_token(username):
    token = jwt.encode({
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is missing!"}), 403
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data["user"]
        except:
            return jsonify({"error": "Invalid token!"}), 403
        return f(current_user, *args, **kwargs)
    return decorated
