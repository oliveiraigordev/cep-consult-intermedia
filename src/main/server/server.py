from flask import Flask
from src.main.routes.cep import cep_bp

app = Flask(__name__)
app.register_blueprint(cep_bp)
