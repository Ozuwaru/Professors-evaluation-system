import csv
import Consultas
from getInfo import insertarUna
 
# importing
linkF = 'https://docs.google.com/forms/d/e/1FAIpQLScR08acr2BS2BU9N1PTW8ZdrbkbwNwQc2HywaqTz4GWYKAahw/viewform'

def cambiarPregunta(pregunta):
    if pregunta== 'El docente entrega las notas a tiempo?':
        return 1
    elif pregunta== 'El docente trae material suficiente?':
        return 2
    elif pregunta== 'El docente tiene buena metodologia al explicar?':
        return 3
    elif pregunta== 'El docente evalua de manera justa?':
        return 4
    elif pregunta== 'El docente llega a la hora de clases?':
        return 5
            


def cargarArchivo():


    with open('C:/Users/usuario/Documents/app profesores y tal/botFormularios/Encuesta Estadistica 2.csv', newline='') as csvfile:
        data =csv.reader(csvfile)
        next(data)
        for row in data:
            
            

            '''row['ID']= Consultas.consultaInscripcionPorCorreo(row['Username'])
            row['El docente entrega las notas a tiempo?']= Consultas.consultaInscripcionPorCorreo(row['Username'])
            '''
            row[0]= Consultas.consultaInscripcionPorCorreo(row[1])
            if(row[0]):
                row[0]= row[0][0]
                for r in range(5):
                    row[r+2]= Consultas.consultaP(row[r+2]);
                    'print(row[r+2])'
                insertarUna(row[0],1,row[2])
                insertarUna(row[0],2,row[3])
                insertarUna(row[0],3,row[4])
                insertarUna(row[0],4,row[5])
                
                insertarUna(row[0],5,row[6])
                print(row);
            



cargarArchivo()