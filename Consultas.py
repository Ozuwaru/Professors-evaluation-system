
import env;
import mysql.connector;
'CAMBIEN ESTAS VARIABLES:'

mydb = mysql.connector.connect(
        host="localhost",
        user=env.dbuser,
        password=env.dbpassword,
        database = "proyectoprofes"
    )




def obtenerPromedioPorProfesor(idProfe):
    mycursor = mydb.cursor();
    
    comando = """
            select Materias.Materia as Materia, Materias.id as id, preguntas.Pregunta as pregunta , avg(encuestas.respuesta) AS Promedio
            from (((
            (profesores  inner join profesorxmateria on profesores.ID = profesorxmateria.Profesor
            inner join materias on profesorxmateria.ID = Materias.ID
            )
            inner join inscripciones on profesorxmateria.ID= inscripciones.Materia)
            inner join encuestas on inscripciones.ID = encuestas.cupo
            inner join preguntas on encuestas.pregunta=preguntas.ID
            ))  where(profesores.id = %s)   group by Materia, pregunta;

        """%(idProfe)
    
    mycursor.execute(comando)
    encuestasPorProfe =mycursor.fetchall()

    for x in encuestasPorProfe:

        '''Aqui deberiamos hacer cualquier calculo o lo que sea con la info de las materias del profesor'''
        print(x)
    return encuestasPorProfe;

'''
Nombre prof
Materia Seccion
'''
def consultaNombre(nombre):
    mycursor = mydb.cursor();
    
    comando = """
            select Nombre,e.Escuela, Cedula from Profesores
            inner join Escuelas e on profesores.Escuela= e.id where (Nombre like '%s');

        """%('%'+nombre+'%')
    mycursor.execute(comando)
    Profesor =mycursor.fetchall()

    return Profesor;



def consultaCorreosPorMateria(idMateria):
    mycursor = mydb.cursor();
    
    comando = """
           
            select alumnos.nombre as Nombre, alumnos.Email, p.ID as Materia ,p.Profesor
            from profesorxmateria p inner join inscripciones on p.ID= inscripciones.Materia
            inner join alumnos on inscripciones.Alumno= alumnos.ID
            where (p.ID = %s);
        """%(idMateria)
    mycursor.execute(comando)
    Alumnos =mycursor.fetchall()

    return Alumnos;


print(consultaCorreosPorMateria(1))