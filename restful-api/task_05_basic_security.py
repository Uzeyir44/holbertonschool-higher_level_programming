#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    get_jwt,
    create_access_token
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify(username, password):
    if username in users:
        return (check_password_hash(users[username]["password"], password))
    return (False)

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return ({"message": "Basic Auth: Access Granted"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    username = data.get("username")
    password = data.get("passsword")
    
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return (jsonify({"msg": "Bad credentials"}), 401)
    
    token = create_access_token(
        identity=username, 
        additional_claims={"role": user["role"]}
    )
    
    return jsonify({"access_token": token})

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return (jsonify({"message": "JWT Auth: Access Granted"}))

@app.route("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()
    
    if (claims.get("role") != "admin"):
        return (jsonify({"error": "Admin access required"}), 403)
    
    return jsonify({"message": "Admin Access: Granted"})

if (__name__ == "__main__"):
    app.run(debug=True)