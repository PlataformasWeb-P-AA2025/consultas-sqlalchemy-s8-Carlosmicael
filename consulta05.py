from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,func # se importa el operador and

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



#5.1 En una consulta, obtener todos los cursos.
#5.2 Realizar un ciclo repetitivo para obtener en cada iteración las entregas por cada curso 
# (con otra consulta), y presentar el promedio de calificaciones de las entregas


#obetenemos todos los cursos
resultado = session.query(Curso).all()

#rrecoremos todos los cursos y por cada cursos consultamos sus entregas promediamos y presentamos 
for cur in resultado:
    #aqui consultamos todos las entregas partiendo desde Entrega haciendo un join con Tarea 
    #filtramos accediendo al curso atraves de su id y lo comparamos con el id de cursos del objeto
    entregas = session.query(Entrega).join(Tarea).filter(Tarea.curso_id == cur.id).all()
    if entregas:
        #aqui promediamos utilizando funciones como sum y len 
        #la funcion sum recibe un array o secuencia para ello iteramos
        #con esta expersion e.calificacion for e in entregas indicandole
        #que en cada iteracion sume las calificaciones de las entregas y por
        #ultimo dividimos para el numero de entregas.
        promedio = sum(e.calificacion for e in entregas) / len(entregas)
        #imprimimos
        print(f"nombre del curso: {cur.titulo} -> Promedio: {promedio}")