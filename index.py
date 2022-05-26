import subprocess
import platform
import os
import time
import smtplib
#Importa a lib de envio de email
from email.message import EmailMessage
#Importa a senha
from senha import senhaa

# Configurar email e senha
EMAIL_ENDERECO = 'seuemail@gmail.com'
EMAIL_SENHA = senhaa

# Informações do email
msg = EmailMessage()
msg['Subject'] = 'ALERTA! SERVIDOR'
msg['From'] = 'remetente@gmail.com'
msg['To'] = 'destinatario@gmail.com'
msg.set_content('O servidor está fora do ar')

ips = ['yourip']

while True:
    with open(os.devnull, "wb") as sumir:
        for ip in ips:
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                            stdout=sumir, stderr=sumir).wait()
                if result:
                    print (ip, "Falha! IP fora do ar!")
                    # Enviar o email
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(EMAIL_ENDERECO, EMAIL_SENHA)
                        smtp.send_message(msg)
                else:
                    print (ip, "ativo")

# Tempo para o programa refazer a análise do ping
time.sleep(5)
print('--Recomeçar--')
