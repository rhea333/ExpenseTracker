from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
import os

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    
    # Configurations
    app.config["MONGO_URI"] = "mongodb://mongo:27017/expense_tracker"
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "supersecretkey")

    # Initialize Extensions
    mongo.init_app(app)
    JWTManager(app)

    # Register Blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
