# 👨🏻‍💻 Sistema de Matriculación Universitaria 👩🏻‍💻

## Descripción 📑

Este proyecto implementa un sistema de matriculación para universidades, permitiendo a los alumnos registrarse o iniciar sesión, elegir semestres, seleccionar materias, secciones, turnos y días de conveniencia. Además, ofrece funcionalidades para ver, actualizar o eliminar el horario registrado, incorporando operaciones CRUD fundamentales. Desarrollado con Python, SQLAlchemy, SQLite y Flask, y con un diseño estilizado utilizando Tailwind CSS.

## Enfoque y Metodología 📌

El sistema fue diseñado para que sea fácil y rápido de usar para los estudiantes que se están matriculando. Organizado de una manera que mantiene separados los datos, cómo se ve la página y cómo funciona, para poder hacer cambios fácilmente.

## Arquitectura del Sistema 🧩

El sistema se estructura de la siguiente manera:
- `models.py`: Define las clases y funciones para crear las tablas de la base de datos `Alumnos` y `Horario`.
- `conexion.py`: Establece la conexión con la base de datos SQLite `alumnos_matriculados`, que almacena ambas tablas.
- `app.py`: Contiene las rutas y la lógica del servidor Flask, gestionando las solicitudes y respuestas del usuario.
- Archivos HTML: Proporcionan la interfaz de usuario, estilizada con Tailwind CSS para mejorar la experiencia de navegación.

## Ejecución del Proyecto 🔌

Para ejecutar este proyecto, sigue estos pasos:
- Clonar el repositorio.
- Asegurarse de tener Python 3 instalado.
- Instalar las dependencias ejecutando `pip install -r requirements.txt` en la terminal.
- Ejecutar el archivo `app.py` con el comando `python app.py`.

## Escalabilidad 📈

La arquitectura modular permite agregar nuevas funcionalidades, como la gestión de profesores, aulas y calificaciones, sin grandes modificaciones al código existente.

## Trabajos Posteriores 📋

- Esta página puede ser complementada implementando un algoritmo que limite la inscripción a asignaturas cuyo horario se solape.
- Limitar el cupo a las secciones atendiendo la cantidad de alumnos que puede matricularse como máximo a cada asignatura.
- Se podría implementar agregar una página que permita el pago de la inscripción atendiendo a la cantidad de asignaturas matriculadas.
- Agregar un apartado para la gestión de profesores, aulas, calificaciones y programas de cada asignatura.

