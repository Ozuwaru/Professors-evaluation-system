import BDclave;
import mysql.connector;

def createDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE proyectoProfes")
    mycursor.close()
    mydb.commit()
    mydb.close()
    
def createTables():
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
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
            Materia varchar(50) not null unique,
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
            Pregunta varchar (60),
            Fecha Date
            );

            Create table Respuestas(

            ID INT NOT NULL AUTO_INCREMENT primary KEY,
            Respuesta varchar (60)
            );


            Create table Encuestas(

            ID int not null auto_increment primary key,
            Materia Int not null ,
            pregunta int not null,
            respuesta int not null, 
            foreign key (Materia) references ProfesorxMateria(ID),
            foreign key (pregunta) references preguntas(ID),
            foreign key (respuesta) references respuestas(ID)

            );


        
            create table Usuarios (
                ID int not null auto_increment,
                username varchar (15) not null unique,
                uPassword varchar(30) not null,
                nombre varchar(30) not null,
                apellido varchar(30) not null,
                escuela varchar(20),
                telefono varchar(20),
                correo varchar(30),
                direccion varchar(30),
                primary key (ID)
                
            );



            alter table  profesorxmateria add encuesta  varchar (80);
            alter table  profesorxmateria add linkEncuesta  text;
            alter table inscripciones add encuestado bool;

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
def insertarFormID(idMateria,idForm, link):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor();
    comando = '''update profesorxmateria 
        set encuesta = %s,
        linkEncuesta = %s
        where ID = %s'''
    mycursor.execute(comando,(idForm,link,idMateria))

    mydb.commit()

def seedF():
    #Esta funcion guarda los links de estadistica 1 y 2, Bases de datos y ingenieria de sofware
    insertarFormID(1,'1SIGXyaM0_D03ury4SmLi8e6qqKAjynT1G5dtWceKJAA', 'https://docs.google.com/forms/d/e/1FAIpQLScKQfDluYIemITOOYuk0xSsMBG2ZzIVXsRbbSGMldSpi2ZjfA/viewform')
    insertarFormID(2,'1EgxyhcttQbEKgjXctp2g3hHQHY_1KHGSBndrzoHljnQ', 'https://docs.google.com/forms/d/e/1FAIpQLSerTQkkvRf4L9jMOdBu6Uh5WVi2xXg6v3ogo_XBbUKJoVwHDA/viewform')

    insertarFormID(3,'1VelEKYWSy0YaxkaffIC2pD1NHEHlqwgA_8F3AsWSAJc', 'https://docs.google.com/forms/d/e/1FAIpQLSeQz4_GQFghW1ju7EAT4hLaDiictYY85OWBTNBXf0cKbgrs7A/viewform')
    insertarFormID(4,'1zUSDF2kjWnj-DJg3T3xRyc75NP-bG4Fu0jNmHrsKau0', 'https://docs.google.com/forms/d/e/1FAIpQLSdEvnsIRPBu5ioWcX_nw8sOFvtsm1fpBHQGWwUsz7G7e3JyfA/viewform')


def seedTables():
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor()
    insertarDatos('usuarios', 'username,uPassword,nombre,apellido,escuela,telefono,correo,direccion','%s,%s,%s,%s,%s,%s,%s,%s',
                [('aura','123456789','Aura','Apellido','Ingenieria','0424-000000','aura@gmail.com','Su casa',),],mycursor)
    
    insertarDatos("preguntas","pregunta","%s",[
        ("¿El docente entrega las notas a tiempo?",),
        ("¿El docente trae material suficiente?",),
        ("¿El docente tiene buena metodologia al explicar?",),
        ("¿El docente evalua de manera justa?",),
        ("¿El docente llega a la hora de clases?",)],
        mycursor)

    insertarDatos("respuestas","Respuesta", "%s",[
        ("Muy ineficiente",),
        ("Ineficiente",),
        ("Regular",),
        ("Eficiente",),
        ("Muy eficiente",),],
        mycursor)
    

    insertarDatos("Escuelas","Escuela","%s",[
        ("Ingenieria",),
        ("Derecho",),
        ("Faces",)],
        mycursor)
    mydb.commit()


    insertarDatos("Profesores", "Cedula,Nombre, FechaIngreso, FechaNacimiento,Escuela","%s,%s,%s,%s,%s",[
        (11112222,"Luis Hernandez","2016-04-23","1970-04-23",1,),
        (12355132,"Yelenia","2016-04-23","1970-04-23",1,),
        (23522158,"Adalides ","2016-04-23","1970-04-23",1,),
        (23153251,'Yumilva Fermin', "2016-04-23","1970-04-23",1),
        (9231532,'Carlos lezama', "2016-04-23","1970-04-23",1),
        (193318859,'Manuel Romero', "2016-04-23","1970-04-23",1),],
        mycursor )
    
    mydb.commit()
    insertarDatos("Carreras","Carrera,Escuela","%s,%s",[
        ('Ingenieria Informatica',1,),
        ('Ingenieria en Sistemas',1,),],
        mycursor )
    
    mydb.commit()
    insertarDatos("Alumnos", "Cedula,Nombre,Email,Carrera","%s,%s,%s,%s",[
        ('30365852','Oswald Torrealba','c@gmail.com', '1',),
        ('30453752','Frank Diaz','p1@gmail.com', '1',),
        ('29568456','Victor Rojaz ','p2@gmail.com', '1',),
        ('56464564','Maria Rojaz ','p3@gmail.com', '2',),
        ('21315548','Juan Rojaz ','p4@gmail.com', '1',),
        ('13584532','Carlos Rojaz ','p5@gmail.com', '1',),],
        mycursor)
    
    mydb.commit()
    insertarDatos("Materias","Materia", "%s",[
        ("Estadistica 1",),
        ("Estadistica 2",),
        ("Bases de datos",),
        ("INGENIERIA DE SOFTWARE",),],
        mycursor)

    mydb.commit()
    insertarDatos("MateriasxCarrera","Carrera,Materia","%s,%s",[
        ("1","1",),
        ("1","2",),
        ("1","3",),
        ("1","4",),

        ("2","1",),
        ("2","2",),
        ("2","3",),
        ("2","4",),],
        mycursor)
    
    insertarDatos("ProfesorxMateria", "Profesor,Materia,Seccion","%s,%s,%s",[
        ('1','1', '3D1',),
        ('1','2', '3D1',),
        ('2','3', '3D1',),
        ('3','4', '3D1',),],
        mycursor)
    
    mydb.commit()
    insertarDatos("inscripciones", "Alumno,Materia","%s,%s",[
        ('1', '1',),
        ('1', '2',),
        ('2', '1',),
        ('3', '1',),

        ('1', '3',),
        ('2', '3',),
        ('3', '3',),

        ('1', '4',),
        ('2', '4',),
        ('3', '4',),],
        mycursor)
    
    mydb.commit()

def insertarEncuestasSinExcel():
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor()

    insertarDatos("Encuestas","Materia,pregunta,respuesta", "%s,%s,%s",[
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

        (4,1,5,),
        (4,2,5,),
        (4,3,5,),
        (4,4,5,),
        (4,5,5,),

        
        (2,1,1,),
        (2,2,1,),
        (2,3,1,),
        (2,4,1,),
        (2,5,1,),

        (1,1,5,),
        (1,2,5,),
        (1,3,5,),
        (1,4,5,),
        (1,5,5,),

        (3,1,5,),
        (3,2,5,),
        (3,3,5,),
        (3,4,5,),
        (3,5,5,),],
        mycursor)

    mydb.commit()
    
def insertarUna(Cupo,pregunta,respuesta):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor()
    
    insertarDatos("Encuestas","Materia,pregunta,respuesta", "%s,%s,%s",[
        (Cupo,pregunta,respuesta,),],mycursor)
    
    mydb.commit()

def checkLogin(username, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor()
    
    command = """select exists(select * from usuarios 
    where username ="%s" AND uPassword = "%s");"""%(username,password)
    mycursor.execute(command)
    result = mycursor.fetchall()

    return (result[0][0])

def registrarInscribir(cedula,nombre,email,carrera,idMateria):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor()

    mydb.commit()
    insertarDatos("Alumnos", "Cedula,Nombre,Email,Carrera","%s,%s,%s,%s", [
        (cedula,nombre,email, carrera,),],
        mycursor)
    
    mydb.commit()
    idEstudiante =mycursor.lastrowid

    insertarDatos("inscripciones", "Alumno,Materia","%s,%s",[
        (idEstudiante, idMateria,),],
        mycursor)
    
    mydb.commit()

'''
EJECUTA ESTAS 2 FUNCIONES PRIMERO
createDatabase()
createTables()

luego EJECUTA ESTAS 2
seedTables()
insertarEncuestasSinExcel()

CODIGO PA INSERTAR ENCUESTAS DE BD, SI QUIERES QUE SEA DE ing de software sumale 1 al cupo

mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.dbuser,
        password=env.dbpassword,
        database = "proyectoprofes"
    )

mycursor = mydb.cursor();
insertarDatos("Encuestas","Cupo,pregunta,respuesta", "%s,%s,%s",[
       (4,1,1,),
       (4,2,2,),
       (4,3,3,),
       (4,4,4,),
       (4,5,5,),

       (5,1,1,),
       (5,2,1,),
       (5,3,1,),
       (5,4,1,),
       (5,5,1,),

       (6,1,5,),
       (6,2,5,),
       (6,3,5,),
       (6,4,5,),
       (6,5,5,),],
       mycursor)
mydb.commit();
'''

#createDatabase()
#createTables()

#seedTables()
#insertarEncuestasSinExcel()
#seedF()

