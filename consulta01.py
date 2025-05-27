from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from clases import *

# se importa información del archivo configuracion
from config import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

#1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte.
#  En función de la entrega, presentar, nombre del tarea, nombre del estudiante, calificación, 
# nombre de instructor y nombre del departamento



#Consultamos Entrega y con multiples joins Unimos las Tablas Entrega etc y vamos accediendo a cada columna especifica luego
#filtramos por departamentos y recolectamos todos los objetos.
resultado = session.query(Entrega).join(Entrega.tarea).join(Tarea.curso).join(Curso.departamento).join(Curso.instructor).join(Entrega.estudiante).filter(Departamento.nombre == 'Arte').all()

# Mostramos la lista de Entega accediendo a cada uno de sus atributos o columnas:
for entrega in resultado:
    print(
        entrega.tarea.titulo,
        entrega.estudiante.nombre,
        entrega.calificacion,
        entrega.tarea.curso.instructor.nombre,
        entrega.tarea.curso.departamento.nombre
    )
