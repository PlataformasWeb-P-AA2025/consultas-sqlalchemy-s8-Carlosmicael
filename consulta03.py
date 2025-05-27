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





#Obtener todas las tareas asignadas a los siguientes estudiantes 
#Jennifer Bolton 
#Elaine Perez
#Heather Henderson
#Charles Harris
#En función de cada tarea, presentar el número de entregas que tiene

#creamos un listado de los estudiantes para filtrar
listE = ['Jennifer Bolton','Elaine Perez','Heather Henderson','Charles Harris']

#accedemos a Tarea luego con el join a Entrea y Finalizamos con Estudiante filtramos y devolvemos la lista de objetos
resultado = session.query(Tarea).join(Entrega).join(Estudiante).filter(Estudiante.nombre.in_(listE)).all()

# Mostramos la lista de DEpartamento accediendo a cada uno de sus atributos o columnas:
for tare in resultado:
    print(f"tarea : {tare.titulo} , numero de entregas: {len(tare.entregas)}" )