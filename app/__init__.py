from flask import Flask
from app.routes import register

app = Flask(__name__)

# Registrere routes
register(app)
