from flask import render_template, request, redirect, url_for, session
from conexion import app, db
from models import Alumnos, Horario

@app.route('/')

def index():
    return render_template('index.html')

# CRUD (Crear, Leer, Actualizar, Eliminar)

@app.route('/cargar_alumno', methods=['POST', 'GET'])

def cargar_alumno():
    if request.method == 'POST':
        nombre_alumno = request.form['nombre_alumno']
        apellido_alumno = request.form['apellido_alumno']
        cedula = request.form['cedula']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        carrera = request.form['carrera']

        datos_alumnos = Alumnos(nombre_alumno, apellido_alumno, cedula, correo, contraseña, carrera)

        db.session.add(datos_alumnos)
        db.session.commit()

        session["alumno_id"] = datos_alumnos.id

        return render_template('semestres.html')

    return render_template('cargar_alumno.html')

@app.route('/actualizar_horario/<int:horario_id>', methods=['GET','POST'])

def actualizar_horario(horario_id):
    horario_a_actualizar = Horario.query.get(horario_id)

    if request.method == 'POST':
        materia = request.form['materia']
        seccion = request.form['seccion']
        dia = request.form['dia']
        turno = request.form['turno']


        horario_a_actualizar.materia = materia
        horario_a_actualizar.seccion = seccion
        horario_a_actualizar.dia = dia
        horario_a_actualizar.turno = turno

        db.session.commit()

        return redirect(url_for('ver_horario'))
    
    return render_template('actualizar_horario.html', horario_a_actualizar=horario_a_actualizar)

@app.route('/eliminar_horario', methods = ['GET','POST'])

def eliminar_horario():
    
    if request.method == 'POST':
        id = request.form['horario_id']
        horario_a_eliminar = Horario.query.filter_by(id=id).first()

        db.session.delete(horario_a_eliminar)
        db.session.commit()

        return redirect(url_for('ver_horario'))
    
@app.route('/inicio_sesion', methods=['POST','GET'])

def inicio_sesion():
    if request.method == 'POST':
        cedula = request.form['cedula']
        alumno_existe = Alumnos.query.filter(Alumnos.cedula == cedula).first()

        if alumno_existe:
            session["alumno_id"] = alumno_existe.id
            return render_template('semestres.html')
        else:
            mensaje_error = "Usuario no registrado"
            return render_template("inicio_sesion.html", mensaje_error=mensaje_error)

    return render_template('inicio_sesion.html')
    

@app.route('/semestres', methods=['POST','GET'])

def semestres():
    return render_template("semestres.html")

@app.route('/nosotros', methods=['POST','GET'])

def nosotros():
    return render_template("nosotros.html")

@app.route('/primer_semestre', methods=['POST','GET'])

def primer_semestre():
     if request.method == 'POST':
        alumno_id = session.get('alumno_id')
        materia = request.form['materia']
        seccion = request.form['seccion']
        dia = request.form['dia']
        turno = request.form['turno']

        datos_horario = Horario(materia, seccion, dia, turno, alumno_id)

        db.session.add(datos_horario)
        db.session.commit()

        return render_template('primer_semestre.html', alumno_id=alumno_id)
     return render_template('primer_semestre.html')

@app.route('/segundo_semestre', methods=['POST','GET'])

def segundo_semestre():
    if request.method == 'POST':
        alumno_id = session.get('alumno_id')
        materia = request.form['materia']
        seccion = request.form['seccion']
        dia = request.form['dia']
        turno = request.form['turno']

        datos_horario = Horario(materia, seccion, dia, turno, alumno_id)

        db.session.add(datos_horario)
        db.session.commit()

        return render_template('segundo_semestre.html', alumno_id=alumno_id)
    return render_template('segundo_semestre.html')

@app.route('/tercer_semestre', methods=['POST','GET'])

def tercer_semestre():
    if request.method == 'POST':
        alumno_id = session.get('alumno_id')
        materia = request.form['materia']
        seccion = request.form['seccion']
        dia = request.form['dia']
        turno = request.form['turno']

        datos_horario = Horario(materia, seccion, dia, turno, alumno_id)

        db.session.add(datos_horario)
        db.session.commit()

        return render_template('tercer_semestre.html', alumno_id=alumno_id)
    return render_template('tercer_semestre.html')

@app.route('/cuarto_semestre', methods=['POST','GET'])

def cuarto_semestre():
    if request.method == 'POST':
        alumno_id = session.get('alumno_id')
        materia = request.form['materia']
        seccion = request.form['seccion']
        dia = request.form['dia']
        turno = request.form['turno']

        datos_horario = Horario(materia, seccion, dia, turno, alumno_id)

        db.session.add(datos_horario)
        db.session.commit()

        return render_template('cuarto_semestre.html', alumno_id=alumno_id)
    return render_template('cuarto_semestre.html')

@app.route('/quinto_semestre', methods=['POST','GET'])

def quinto_semestre():
    if request.method == 'POST':
        alumno_id = session.get('alumno_id')
        materia = request.form['materia']
        seccion = request.form['seccion']
        dia = request.form['dia']
        turno = request.form['turno']

        datos_horario = Horario(materia, seccion, dia, turno, alumno_id)

        db.session.add(datos_horario)
        db.session.commit()

        return render_template('quinto_semestre.html', alumno_id=alumno_id)
    return render_template('quinto_semestre.html')

@app.route('/sexto_semestre', methods=['POST','GET'])

def sexto_semestre():
    if request.method == 'POST':
        alumno_id = session.get('alumno_id')
        materia = request.form['materia']
        seccion = request.form['seccion']
        dia = request.form['dia']
        turno = request.form['turno']

        datos_horario = Horario(materia, seccion, dia, turno, alumno_id)

        db.session.add(datos_horario)
        db.session.commit()

        return render_template('sexto_semestre.html', alumno_id=alumno_id)
    return render_template('sexto_semestre.html')

@app.route('/ver_horario', methods = ['POST','GET'])

def ver_horario():

    alumno_id = session.get("alumno_id")

    # Consultar la tabla "horarios" para obtener las materias del alumno

    materias = Horario.query.filter_by(alumno_id=alumno_id).all()

    return render_template("ver_horario.html", materias=materias)



if __name__ == ("__main__"):
    app.run(debug = True, port=8000)
