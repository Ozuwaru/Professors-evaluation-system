from email.message import EmailMessage
import smtplib

link=""
remitente="bot.ugma@gmail.com"
def send_email(nombre, destino):
    msg="Hola "+nombre+", ingresa a este link para responder la encuesta sobre tu profesor: "+link;
    email=EmailMessage()
    email["From"]=remitente
    email["To"]=destino
    email["Subject"]="Encuesta de profesores"
    email.set_content(msg)
    
    smtp= smtplib.SMTP_SSL('smtp.gmail.com')
    smtp.login(remitente, "zgzm vvlw cctf kyjo")
    smtp.sendmail(remitente,destino,email.as_string())
    smtp.quit()
    
