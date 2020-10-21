import smtplib
import datetime
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def main():
    #Leitura do arquivo CSV
    with open('data/data_example.csv') as csvfile: 
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            #A cada iteração do laço (leitura linha a linha), pegamos os dados da linha, e armazenamos em uma variável
            email = row[0]
            usuario = row[1]
            senha = row[2]

            #obtém o horário de envio
            hora = datetime.datetime.now()
            hora = hora.strftime("%H:%M")

            #inicializa o corpo do e-mail
            msg = MIMEMultipart()
            
            #define os destniatários que receberão o e-mail, pode separar por virgula ex: [destinatario1, destinatario2]
            destinatarios = [email]
            #define quem estará em copia no momento do envio. pode separar por virgula ex: [copia1, copia2]
            cc = ["pessoa1@exemplo.com.br"]

            msg['From'] = "Nome Fulano <pessoa@exemplo.com.br>"
            msg['To'] = ", ".join(destinatarios)
            msg['Cc'] = ", ".join(cc)
            destinatarios.extend(cc)

            msg['Subject'] = "Assunto do e-mail"

            #aqui é se cria o corpo do e-mail
            msg.attach(MIMEText("""
                <h1>Olá!</h1>
                Seu usuário é <strong> {1} </strong> <br>
                sua senha é <strong> {2} </strong>
            """.format(usuario, senha), 
            'html', 'utf-8'))

            #aqui é enviado o e-mail para todos os destinatários
            server = smtplib.SMTP('smtp.example.local', 25)
            server.sendmail(msg['From'], destinatarios, msg.as_string())
            print("{0} - Enviado - {1}".format(email, hora))
            server.quit()
main()