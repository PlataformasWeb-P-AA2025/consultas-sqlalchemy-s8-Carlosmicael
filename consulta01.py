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



#  Obtiene las entregas de estudiantes de cursos del departamento "Arte", mostrando el título de la tarea, nombre del estudiante, calificación obtenida, nombre del instructor y nombre del departamento,
#  realizando múltiples joins para acceder a los datos que están relacionados en varias tablas estos serian Entrega , Tarea , Curso , Departamento e Instructor, y Estudiante
resultado = session.query(
    Tarea.titulo,Estudiante.nombre,Entrega.calificacion,Instructor.nombre,Departamento.nombre
    ).join(Entrega.tarea).join(Tarea.curso).join(Curso.departamento).join(Curso.instructor).join(Entrega.estudiante).filter(Departamento.nombre == 'Arte').all()

#en el resultado vamos a obtener una  List[Row[Tuple[str, str, Any, str, str]]] una lista de filas de tuplas por cada
#fila vamos a obtener cada valor de la tupla y solo lo interpolamos o formateamos la cadena mostrando el resultado
for tarea, estudiante, calificacion, instructor, departamento in resultado:
    print(f"nombre Tarea: {tarea}, Nombre Estudiante: {estudiante}, calificacion: {calificacion},Instructor: {instructor}, Departamento: {departamento}")