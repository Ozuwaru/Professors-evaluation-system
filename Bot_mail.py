from email.message import EmailMessage
#from google_form import linkF
import smtplib
from BDconsultas import *

#link=linkF

remitente="bot.ugma@gmail.com"

def correos():
    
    #La funcion que debes llamar para guardar la fecha de envio de cada formulario es:
    #guardarFechaEnvioEncuestas(IDMATERIA)

    
    materias=consultaMaterias()
    links=consultaLinks()
    for i in range(len(materias)):
        for j in range(len(links)):
            if(materias[i][0]==links[j][0]):
                link=links[j][1]
                break
        print("enviado correos a materia: %i"%(materias[i][0]))
        listado=AlumnosSinEncuestar(materias[i][0])
        for k in range(len(listado)):
            send_email(listado[k][0],listado[k][1],link)

def send_email(nombre, destino, link):
    msg="Hola, "+nombre+",Soy el bot de la UGMA, responde la siguiente encuesta porfavor: \n %s"%(link)
    #msg="Hola "+nombre+", ingresa a este link para responder la encuesta sobre tu profesor: "+link;
    email=EmailMessage()
    email["From"]=remitente
    email["To"]=destino
    email["Subject"]="Encuesta de profesores"
    email.set_content(msg)
    smtp= smtplib.SMTP_SSL('smtp.gmail.com')
    smtp.login(remitente, "zgzm vvlw cctf kyjo")
    smtp.sendmail(remitente,destino,email.as_string())
    smtp.quit()

# def main():
#     correos()
    
    
# if __name__=="__main__":
#     main()