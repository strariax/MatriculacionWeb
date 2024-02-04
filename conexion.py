from flask import Flask
from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///alumnos_matriculados.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Para evitar advertencias y reducir el consumo de memoria
app.config['SECRET_KEY'] = 'aaabbbcccddee'

db.init_app(app)

with app.app_context():
    db.create_all()