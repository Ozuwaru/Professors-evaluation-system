import mysql.connector;
dbuser ="root"
dbpassword= '1234'

def createDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user=dbuser,
        password=dbpassword
    )


    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE proyectoProfes")
    mycursor.close()

    mydb.close()




def createTables():
    mydb = mysql.connector.connect(
        host="localhost",
        user=dbuser,
        password=dbpassword,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor()    
    mycursor.execute(
        '''
            CREATE TABLE Escuelas (
            ID  int auto_increment not null,
            Escuela varchar(20),
            PRIMARY KEY (ID)
            );




            CREATE TABLE Carreras (
            ID int auto_increment not null,
            Carrera varchar(30),
            Escuela int not null ,
            primary key (ID),
            foreign key (Escuela) references Escuelas(ID)
            );




            CREATE TABLE Materias (
            ID int auto_increment not null,
            Materia varchar(20) not null unique,
            primary key (ID)
            );

            CREATE TABLE MateriasxCarrera (
            Carrera INT NOT NULL,
            Materia INT NOT NULL,
            primary key (Carrera,Materia),
            foreign key (Carrera) references Carreras(ID),
            foreign key (Materia) references Materias(ID)
            );


            CREATE TABLE Profesores (
            ID int auto_increment not null,
            Cedula varchar(20) not null unique,
            Nombre varchar(50) not null,
            FechaIngreso date not null,
            FechaNacimiento date not null,
            Escuela int not null ,
            primary key (ID),
            foreign key (Escuela) references Escuelas(ID)
            );


            CREATE TABLE Alumnos (
            ID int auto_increment not null,
            Cedula varchar(20) not null unique,
            Nombre varchar(50) not null,
            Email varchar(255) not null unique,
            Carrera int not null ,
            primary key (ID),
            foreign key (Carrera) references Carreras(ID)
            );

            CREATE TABLE ProfesorxMateria (
            ID INT NOT NULL auto_increment PRIMARY KEY,
            Profesor  int not null ,
            Materia INT NOT NULL, 
            Seccion varchar (10),
            foreign key (Profesor) references Profesores(ID),
            foreign key (Materia) references Materias(ID)
            );

            CREATE TABLE Inscripciones (
            ID INT NOT NULL auto_increment PRIMARY KEY,
            Alumno  int not null ,
            Materia Int not null,
            foreign key (Alumno) references Alumnos(ID),
            foreign key (Materia) references ProfesorxMateria(ID)
            );

            Create table Preguntas(

            ID INT NOT NULL AUTO_INCREMENT primary KEY,
            Pregunta varchar (60)
            );

            Create table Respuestas(

            ID INT NOT NULL AUTO_INCREMENT primary KEY,
            Respuesta varchar (60)
            );


            Create table Encuestas(

            ID int not null auto_increment primary key,
            Cupo Int not null ,
            pregunta int not null,
            respuesta int not null, 
            foreign key (cupo) references Inscripciones(ID),
            foreign key (pregunta) references preguntas(ID),
            foreign key (respuesta) references respuestas(ID)

            );


        
            create table Usuarios (
                ID int not null auto_increment,
                username varchar (15) not null unique,
                uPassword varchar(30) not null,
                primary key (ID)
                
            );

        '''
    )


    print("tables created succesfully");

    mycursor.close()





def insertarDatos(tabla,columnas,cantidad, info ,cursor):
    
    comando = "INSERT INTO  %s (%s) VALUES (%s)" %(tabla,columnas,cantidad)
    cursor.executemany(comando,info)


'''
    seedtables es la funcion para llenar las tablas de info de prueba, debe ser llamada al instalar la app o 
    al abrirla por primera vez
'''


def seedTables():
    mydb = mysql.connector.connect(
        host="localhost",
        user=dbuser,
        password=dbpassword,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor();
    

    insertarDatos('usuarios', 'username,uPassword','%s,%s',
                [('aura','123456789',),],mycursor)



    insertarDatos("preguntas","pregunta","%s",
                  [
        ("¿El docente entrega las notas a tiempo?",),
        ("¿El docente trae material suficiente?",),
        ("¿El docente tiene buena metodologia al explicar?",),
        ("¿El docente evalua de manera justa?",),
        ("¿El docente llega a la hora de clases?",)
    ],mycursor)

    insertarDatos("respuestas","Respuesta", "%s",
                  [
        ("Muy ineficiente",),
         ("Ineficiente",),
         ("Regular",),
         ("Eficiente",),
         ("Muy eficiente",),
     ],mycursor)
    

    insertarDatos("Escuelas","Escuela","%s",
                  [
         ("Ingenieria",),
         ("Derecho",),
         ("Faces",)
     ],mycursor)
    mydb.commit()


    insertarDatos("Profesores", "Cedula,Nombre, FechaIngreso, FechaNacimiento,Escuela","%s,%s,%s,%s,%s",
                 [
         (11112222,"Luis Hernandez","2016-04-23","1970-04-23",1,),
     ],mycursor )
    
    mydb.commit()
    insertarDatos("Carreras","Carrera,Escuela","%s,%s",
                 [
         ('Ingenieria Informatica',1,),
         ('Ingenieria en Sistemas',1,),
     ],mycursor )
    
    mydb.commit()
    insertarDatos("Alumnos", "Cedula,Nombre,Email,Carrera","%s,%s,%s,%s",
                  [
        ('30365852','Oswald Torrealba','oswaldtg1@gmail.com', '1',),
        ('30453752','Frank Diaz','p1@gmail.com', '1',),
        ('29568456','Victor Rojaz ','p2@gmail.com', '1',),
    ],mycursor)
    mydb.commit()
    

    insertarDatos("Materias","Materia", "%s",
                  [("Estadistica 2",),("Estadistica 1",),],mycursor)
    
    mydb.commit()
    insertarDatos("MateriasxCarrera","Carrera,Materia","%s,%s",
                  [("1","1",),("1","2",),],mycursor)
    


    insertarDatos("ProfesorxMateria", "Profesor,Materia,Seccion","%s,%s,%s",
                  [
        ('1','1', '1',),
        ('1','2', '1',),
    ],mycursor)
    mydb.commit()


    insertarDatos("inscripciones", "Alumno,Materia","%s,%s",
                  [
        ('1', '1',),
        ('2', '1',),
        ('2', '1',),
    ],mycursor)
    
    mydb.commit()




def insertarEncuestasSinExcel():
    mydb = mysql.connector.connect(
        host="localhost",
        user=dbuser,
        password=dbpassword,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor();

    insertarDatos("Encuestas","Cupo,pregunta,respuesta", "%s,%s,%s",[
        (1,1,1,),
        (1,2,2,),
        (1,3,3,),
        (1,4,4,),
        (1,5,5,),

        (2,1,1,),
        (2,2,1,),
        (2,3,1,),
        (2,4,1,),
        (2,5,1,),

        (3,1,5,),
        (3,2,5,),
        (3,3,5,),
        (3,4,5,),
        (3,5,5,),
    ],mycursor)

    mydb.commit()



def obtenerPromedioPorProfesor(idProfe):
    mydb = mysql.connector.connect(
        host="localhost",
        user=dbuser,
        password=dbpassword,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor();
    
    comando = """
            select Materias.Materia as Materia, preguntas.Pregunta as pregunta , avg(encuestas.respuesta)
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

        



def login(username, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user=dbuser,
        password=dbpassword,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor();
    command = """select exists(select * from usuarios 
    where username ="%s" AND uPassword = "%s");"""%(username,password)
    mycursor.execute(command)
    result = mycursor.fetchall()

    return (result[0][0])


'''

EJECUTA ESTAS 2 FUNCIONES PRIMERO
creamos la base de datos




createDatabase()

creamos las tablas



createTables()
'''


'''
luego EJECUTA ESTAS 2
seedTables()

insertarEncuestasSinExcel()
'''
