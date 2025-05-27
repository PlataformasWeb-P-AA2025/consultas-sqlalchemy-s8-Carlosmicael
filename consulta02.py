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



#2. Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 . En función de los departamentos,
# presentar el nombre del departamento y el número de cursos que tiene cada departamento.


#La consulta inicia desde Departamento luego realiza un join con Curso mediante la relación que tiene con deepartamento cursos
#  para obtener los cursos de ese departamento hace otro join con tarea a través de curso tareas
#  para acceder a las tareas asignadas en esos cursos y después se une con Entrega mediante Tarea 
# entregas para acceder a las entregas asociadas a esas tareas y finalmente filtra aquellas entregas con calificación menor o igual a 0.3
resultado = session.query(Departamento).join(Curso).join(Tarea).join(Entrega).filter(Entrega.calificacion <= 0.3).all()

# Mostramos la lista de DEpartamento accediendo a cada uno de sus atributos o columnas:
for depa in resultado:
    print(depa.nombre,len(depa.cursos))
