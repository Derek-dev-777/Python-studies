import os
from pathlib import Path
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


load_dotenv()
#caminho arquivo

CAMINHO_ARQUIVO = Path(__file__).parent / "Aula26gmai.html"

# Dados destinatario e remetente
remetente = os.getenv("FROM_EMAIL", "")
destinatario = os.getenv("EMAIL_DESTINATARIO2", "")

#Configurações SMPT
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = remetente
smtp_password = os.getenv("EMAIL_PASSWORD", "")



#Transformar a mensagem em MIMEmultipart
mime_multipart = MIMEMultipart()
mime_multipart["from"] = remetente
mime_multipart['to'] = destinatario
mime_multipart["subject"] = "to testando gatinha"

texto_arquivo = """\
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Teste de Email</title>
</head>
<body>
    <h1>aaaa</h1>
    <p>Teste, se tu ta lendo isso tu é mo maneiro</p>
    
</body>
</html>
"""

corpo_email = MIMEText(texto_arquivo, "html", "utf-8")
mime_multipart.attach(corpo_email)



for i in range(5):
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(mime_multipart)
        print("Email Enviado")