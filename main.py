#Estudo Sobre Envio De emails Com Python 

from email import message
from email.mime import application
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import password, email


host = "smtp.gmail.com"
port = "587"
login = email
senha = password


def email(mensagem):

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login, senha)

    corpo = mensagem

    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = 'thiagosantosdb13@gmail.com'
    email_msg['Subject'] = 'My Email'
    email_msg.attach(MIMEText(corpo, 'html'))


    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    server.quit()