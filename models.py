from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_alumno = db.Column(db.String(40), nullable = False)
    apellido_alumno = db.Column(db.String(40), nullable = False)
    cedula = db.Column(db.Integer, nullable = False)
    correo = db.Column(db.String(40), nullable = False)
    contraseña = db.Column(db.String(80), nullable = False)
    carrera = db.Column(db.String(40), nullable = False)

    def __init__(self, nombre_alumno, apellido_alumno, cedula, correo, contraseña, carrera):
        self.nombre_alumno = nombre_alumno
        self.apellido_alumno = apellido_alumno
        self.cedula = cedula
        self.correo = correo
        self.contraseña = contraseña
        self.carrera = carrera

class Horario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    materia = db.Column(db.String(40), nullable = False)
    seccion = db.Column(db.String(40), nullable = False)
    dia = db.Column(db.String(20), nullable = False)
    turno = db.Column(db.String(40), nullable = False)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)

    def __init__(self, materia, seccion, dia, turno, alumno_id):
        self.materia = materia
        self.seccion = seccion
        self.dia = dia
        self.turno = turno
        self.alumno_id = alumno_id