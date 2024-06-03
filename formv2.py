from apiclient import discovery
from httplib2 import Http
from oauth2client.service_account import (ServiceAccountCredentials)
from googleapiclient.errors import HttpError
from BDconsultas import MateriasSinFormularios,consultaPreguntas,consultaRespuestas,MateriasConFormularios,consultaP,actualizarDB,CedulasInscritas,cantP
from BD import insertarFormID,insertarUna
import json
SCOPES = ["https://www.googleapis.com/auth/forms.body",'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"


CLIENT_SECRET_FILE = r'C:\Users\usuario\Documents\app profesores y tal\credentials..json'

creds = ServiceAccountCredentials.from_json_keyfile_name(
            CLIENT_SECRET_FILE,
            SCOPES
        )

http = creds.authorize(Http());

form_service = discovery.build(
    "forms",
    "v1",
    http=http,
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)


drive_service = discovery.build('drive', 'v3', credentials=creds)

preguntas =False
respuestas = False

def crearObj(pregunta,respuestas, index):
    obj ={
        "createItem": {
                    "item": {
                        "title": (
                            "%s"%(pregunta)
                        ),
                        "questionItem": {
                            "question": {
                                "required": True,
                                "choiceQuestion": {
                                    "type": "RADIO",
                                    "options": [
                                        {"value": respuestas[0][0]},
                                        {"value": respuestas[1][0]},
                                        {"value": respuestas[2][0]},
                                        {"value": respuestas[3][0]},
                                        {"value": respuestas[4][0]},
                                    ],
                                    "shuffle": False,
                                },
                            }
                        },
                    },
                    "location": {"index": index},
                }
    }
    #print(obj)
    return obj


def crearForm(nombreMateria):

    objPreg =[]
    obj ={
        "createItem": {
                    "item": {
                        "title": (
                            "Ingrese su cedula por favor: "
                        ),
                        "questionItem": {
                            "question": {
                                "required": True,
                                "textQuestion": {
                                    "paragraph": False
                                },
                            }
                        },
                    },
                    "location": {"index": 0},
                }
    }
    objPreg.append(obj)

    global preguntas
    global respuestas
    index =1
    for p in preguntas:
        objPreg.append( crearObj(p,respuestas,index))
        index+=1

    NEW_FORM = {
        "info": {
            "title": "Encuesta %s"%(nombreMateria),
        }
    }

    # Request body to add a multiple-choice question
    NEW_QUESTION = {
        "requests": [

            #Aqui debo ingresar la lista de objetos que contenga las preguntas del formulario aa
            objPreg
           ]
    }
    
    # Creates the initial form
    result = form_service.forms().create(body=NEW_FORM).execute()

    # Adds the question to the form
    question_setting = (
        form_service.forms()
        .batchUpdate(formId=result["formId"], body=NEW_QUESTION)
        .execute()
    )

    # Prints the result to show the question has been added
    
    get_result = form_service.forms().get(formId=result["formId"]).execute()
    
    formId=result["formId"]

    
    
    #print(json.dumps(get_result))
    data = [formId, get_result['responderUri'] ]
    print(data)
    return  data


def crearFormularios():
    #primero necesito las materias y los formularios
    
    materias =MateriasSinFormularios()
    global preguntas
    preguntas = consultaPreguntas()
    global respuestas
    respuestas=  consultaRespuestas()
    #print(m)
    for m in materias :
        data = crearForm(m[1])       
        
        insertarFormID(m[0],data[0],data[1])

    print('formularios creados')
        






def obtenerInfo(id,idMateria):
    r  = form_service.forms().responses().list(formId=id).execute()
    cedulas=CedulasInscritas(idMateria)
    #print(json.dumps(r, sort_keys=True, indent=4, separators=(",", ": ")))
    #print('\n')
    cantidadP = cantP()
    
    if 'responses' in r:
        for res in r['responses']:
            cedula=0
            verC=False
            data= []
            #print('nueva respuesta')
            for a in res['answers']:
                if (res['answers'][a]['textAnswers']['answers'][0]['value']).isnumeric():
                    cedula= res['answers'][a]['textAnswers']['answers'][0]['value']

                    if cedula in cedulas:
                        verC=True

                    else:
                        break


                else:
                    
                    data.append(res['answers'][a]['textAnswers']['answers'][0]['value'])
                
            if verC:
                for i in range(cantidadP):
                    data[i]=consultaP(data[i])
                    insertarUna(idMateria,i+1,data[i])

    print("Info cargada para %s"%(idMateria))
                    





def cargarInfo():
    #actualizarDB()
    materias  =MateriasConFormularios()
    #print(materias)
    for m in materias:
        obtenerInfo(m[1],m[0])
    print('info Cargada correctamente')


def borrarF(id):
   
    

    response = drive_service.files().delete(fileId=id).execute()
    print('formulario borrado')


def mostrarFormularios(borrar=False):
    try:
        page_token = None


        while True:
            response = drive_service.files().list(
                # You can use MIME types to filter query results
                q="mimeType='application/vnd.google-apps.form'",
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=page_token
            ).execute()

            #print(response)
            for file in response.get('files', []):
                

            # Process change
                if borrar:
                    borrarF(file['id'])
                else:
                    print (file['id'])
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break       

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


