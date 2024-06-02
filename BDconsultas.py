
import BDclave as BDclave;
import mysql.connector;


mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )



#Caso 0 me dara promedio de cada materia que de el profe, caso 1 promedio de cada pregunta de una materia
def obtenerPromedioPorProfesor(idProfe,caso):
    mycursor = mydb.cursor();
    
    comando = """
           select Materias.Materia as Materia, Materias.id as id, preguntas.Pregunta as pregunta , avg(encuestas.respuesta) AS Promedio
        from ((
		(profesores  inner join profesorxmateria on profesores.ID = profesorxmateria.Profesor
		inner join materias on profesorxmateria.ID = Materias.ID
		)
		inner join encuestas on Materias.ID = encuestas.Materia
		inner join preguntas on encuestas.pregunta=preguntas.ID
		))  where(profesores.id = %s)   group by Materia, pregunta;

        """%(idProfe)
    
    mycursor.execute(comando)
    encuestasPorProfe =mycursor.fetchall()
    print(encuestasPorProfe)
    ''' for x in encuestasPorProfe:
        Aqui deberiamos hacer cualquier calculo o lo que sea con la info de las materias del profesor
        print(x)
    '''
    '''   
    if caso==0:
        return encuestasPorProfe
    else:
        promedio=[]
        suma=0
        cont=0
        nombre=encuestasPorProfe[0][0]
        for i in range(len(encuestasPorProfe)):
            if(nombre!=encuestasPorProfe[i][0]):
                if cont != 0:
                    promedio.append([nombre,(suma/cont)])
                suma=0
                cont=0
                nombre=encuestasPorProfe[i][0]
            suma+=float(encuestasPorProfe[i][3])
            cont+=1
        if cont != 0:
            promedio.append([nombre, (suma / cont)])
        return promedio'''
    
def tMaterias(idProfe):
    mycursor = mydb.cursor()
    
    comando = """
        SELECT materia
        FROM profesorxmateria
        WHERE Profesor = %s;
    """ %(idProfe)
    mycursor.execute(comando)
    profesor =mycursor.fetchall()

    return profesor


def consultaId(idProfe):
    mycursor = mydb.cursor()
    
    comando = """
            select profesores.ID,Nombre,e.Escuela, Cedula from Profesores
            inner join Escuelas e on profesores.Escuela= e.id where (profesores.ID = '%s');

        """%(idProfe)
    mycursor.execute(comando)
    Profesor =mycursor.fetchall()

    return Profesor



def consultaNombre(nombre):
    mycursor = mydb.cursor()
    
    comando = """
            select profesores.ID,Nombre,e.Escuela, Cedula from Profesores
            inner join Escuelas e on profesores.Escuela= e.id where (Nombre like '%s')
            order by Nombre desc;

        """%('%'+nombre+'%')
    mycursor.execute(comando)
    Profesor =mycursor.fetchall()

    return Profesor

def consultaCorreosPorMateria(idMateria):
    mycursor = mydb.cursor()
    
    comando = """
            select alumnos.nombre as Nombre, alumnos.Email, p.ID as Materia ,p.Profesor
            from profesorxmateria p inner join inscripciones on p.ID= inscripciones.Materia
            inner join alumnos on inscripciones.Alumno= alumnos.ID
            where (p.ID = %s);
        """%(idMateria)
    mycursor.execute(comando)
    Alumnos =mycursor.fetchall()

    return Alumnos

def consultaInscripcionPorCorreo(correo):
    mycursor = mydb.cursor()
    
    comando = """
            Select i.ID from Alumnos
            inner join inscripciones i on alumnos.ID = i.Alumno
            where (alumnos.email like '%s');
        """%(correo)
    mycursor.execute(comando)
    idInscrip =mycursor.fetchone()
    return idInscrip

def consultaP(preg):
    mycursor = mydb.cursor()
    
    comando = """
            SELECT ID FROM proyectoprofes.respuestas
            where Respuesta like '%s'
        """%(preg)
    mycursor.execute(comando)
    v =mycursor.fetchone()

    return v[0]

def consultaPreguntas():
    mycursor = mydb.cursor();
    comando = """
        SELECT Pregunta FROM proyectoprofes.preguntas
        """
    
    mycursor.execute(comando)
    v =mycursor.fetchall()

    return v

def consultaRespuestas():
    mycursor = mydb.cursor();
    comando = """
        SELECT Respuesta FROM proyectoprofes.respuestas
        """
    
    mycursor.execute(comando)
    v =mycursor.fetchall()

    return v;

def MateriasSinFormularios():
    mycursor = mydb.cursor();
    comando = """
        SELECT p.ID, m.Materia FROM profesorxmateria p
        inner join materias m on p.Materia= m.ID
        where encuesta is null;
        """
    
    mycursor.execute(comando)
    v =mycursor.fetchall()

    return v;

def MateriasConFormularios():
    mycursor = mydb.cursor();
    comando = """
        SELECT p.ID,p.encuesta FROM profesorxmateria p
        inner join materias m on p.Materia= m.ID
        where encuesta is not null;

        """
    
    mycursor.execute(comando)
    v =mycursor.fetchall()

    return v;



def actualizarDB():
    mycursor = mydb.cursor();





    comando = '''
        SET SQL_SAFE_UPDATES = 0;
        '''
    mycursor.execute(comando)
    mydb.commit()
    comando = '''
        delete from encuestas;

        '''
    mycursor.execute(comando)
    mydb.commit()

def userData(user,password):
    mycursor = mydb.cursor();
    comando = """
        select * from usuarios where username ="%s" AND uPassword = "%s";"""%(user,password)
    mycursor.execute(comando)
    data =mycursor.fetchall()
    return data

def consultaLinks():
    mycursor = mydb.cursor();
    comando = """
        select Materia,linkEncuesta from profesorxmateria;"""
    mycursor.execute(comando)
    links =mycursor.fetchall()
    return links

def consultaMaterias():
    mycursor = mydb.cursor();
    comando = """
            select ID from materias;
        """
    mycursor.execute(comando)
    materias =mycursor.fetchall()
    return materias;

def AlumnosSinEncuestar(idMateria):
    mycursor = mydb.cursor();


    comando = """
           
            select a.Nombre, a.Email from profesorxmateria m inner join inscripciones i
            on m.Materia = i.Materia inner join alumnos a on i.Alumno =a.ID
            where (i.encuestado is null and m.ID="%s");
        """%(idMateria)
    mycursor.execute(comando)

    v =mycursor.fetchall()


    comando = '''
        update inscripciones set encuestado = true 
        where materia = %s;'''%(idMateria)
    mycursor.execute(comando)

    mydb.commit()

    return v


def consultaIdMateria(idM):
    mycursor = mydb.cursor();
    comando = """
            select Materia from materias where ID='%s';
        """%(idM)
    mycursor.execute(comando)
    materias =mycursor.fetchall()
    return materias

def actualizarContra(user,nueva,repeat):
    if(nueva==repeat):
        mycursor = mydb.cursor();
        comando = """
                update usuarios set contraseña='%s' where username='%s';
            """%(nueva,user)
        mycursor.execute(comando)
        return True
    else:
        return False
    

