from flask import Flask, request, jsonify
from app.routes import register_blueprints
import firebase_admin.auth as auth
from config import Config
import firebase_admin
from firebase_admin import credentials

def create_app():
    """Create and configure an instance of the Flask application"""
    cred = credentials.Certificate(Config.get_secret())
    firebase_admin.initialize_app(cred)
    
    app = Flask(__name__)
    
    # Registra todas as rotas automaticamente
    register_blueprints(app)

    @app.before_request
    def check_authentication():
        """Intercept all requests to check if the user is authenticated"""
        open_routes = ["/public", "/health"]  # Open routes
        
        if request.path in open_routes:
            return  # Skip authentication check

        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"message": "Token ausente ou inválido"}), 401

        token = auth_header.split(" ")[1]

        try:
            decoded_token = auth.verify_id_token(token)
            request.user = decoded_token  # Add user to request object
        except Exception as e:
            return jsonify({"message": "Token inválido ou expirado", "error": str(e)}), 401

    return app
