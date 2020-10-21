import smtplib
import datetime
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from view.html import Nexodata, Memed, Indisponibilidade

def memed():
    #Leitura do arquivo CSV
    with open('data/memed.csv') as csvfile: 
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            #A cada iteração do laço (leitura linha a linha), pegamos os dados da linha, e armazenamos em uma variável
            panvel = row[0]
            usuario = row[1]
            senha = row[2]

            #obtém o horário de envio
            hora = datetime.datetime.now()
            hora = hora.strftime("%H:%M")

            #inicializa o corpo do e-mail
            msg = MIMEMultipart()
            
            #define os destniatários que receberão o e-mail, pode separar por virgula ex: [destinatario1, destinatario2]
            destinatarios = [usuario]
            #define quem estará em copia no momento do envio. pode separar por virgula ex: [copia1, copia2]
            cc = ["suportcs@dimed.com.br"]

            msg['From'] = "Memed Acesso <suportcs@dimed.com.br>"
            msg['To'] = ", ".join(destinatario)
            msg['Cc'] = ", ".join(cc)
            destinatarios.extend(cc)

            msg['Subject'] = "[Memed] Acesso a Plataforma - {0}".format(panvel)

            #aqui é chamado a função para criar o e-mail utilizando os parametros lidos do arquivo csv
            msg.attach(MIMEText(Memed(panvel, usuario, senha), 'html', 'utf-8'))

            #aqui é enviado o e-mail para todos os destinatários
            server = smtplib.SMTP('smtp.dimed.local', 25)
            server.sendmail(msg['From'], destinatarios, msg.as_string())
            print("{0} - Enviado - {1}".format(panvel, hora))
            server.quit()


def nexodata():
    with open('data/nexodata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            panvel = row[0]
            usuario = row[1]
            senha = row[2]

            msg = MIMEMultipart()

            hora = datetime.datetime.now()
            hora = hora.strftime("%H:%M")

            destinatarios = [usuario]
            cc = ["suportcs@dimed.com.br"]

            msg['From'] = "Nexodata Acesso <suportcs@dimed.com.br>"
            msg['To'] = ", ".join(destinatarios)
            msg['Cc'] = ", ".join(cc)
            destinatarios.extend(cc)

            msg['Subject'] = "[Nexodata] Acesso a Plataforma - {0}".format(panvel)

            msg.attach(MIMEText(Nexodata(panvel, usuario, senha), 'html', 'utf-8'))

            server = smtplib.SMTP('smtp.dimed.local', 25)
            server.sendmail(msg['From'], destinatarios, msg.as_string())

            print("{0} - Enviado {1}".format(panvel, hora))
            server.quit()

nexodata()

def indisponibilidade():
    with open('data/Indisponibilidade.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            panvel = row[0]
            msg = MIMEMultipart()
            
            destinatarios = [panvel, 
            "roquee@panvel.com.br",
            "fesoares@panvel.com.br",
            "clsoares@panvel.com.br",
            "adrodrigues@panvel.com.br",
            "amviana@panvel.com.br",
            "azevedof@panvel.com.br",
            "wposada@panvel.com.br",
            "jfdias@panvel.com.br",
            "jmay@panvel.com.br",
            "lpadilha@panvel.com.br",
            "rluna@panvel.com.br",
            "jmoraes@panvel.com.br",
            "scorrea@panvel.com.br",
            "jjrodrigues@panvel.com",
            "crcarvalho@panvel.com.br",
            "jrigo@panvel.com.br",
            "lalves@grupodimed.com.br",
            "suvieira@panvel.com.br",
            "fonofre@panvel.com.br",
            "jtoliveira@panvel.com.br",
            "sampaior@panvel.com.br"
            ]

            cc = ["eodil@dimed.com.br", "ppastore@dimed.com.br", "bgadea@dimed.com.br"]

            msg["From"] = "Central de Serviços <suportcs@dimed.com.br>"
            msg["To"] = ", ".join(para)
            msg['Cc'] = ", ".join(cc)
            msg['Subject'] = "<ATENÇÃO!> Indisponibilidade nos Serviços de Venda no Final de Semana"

            msg.attach(MIMEText(Indisponibilidade(), 'html', 'utf-8'))
            para.extend(cc)

            server = smtplib.SMTP('smtp.dimed.local', 25)
            server.sendmail(msg['From'], destinatarios, msg.as_string())
            print("{0} - Enviado {1}".format(i, panvel))
            
            server.quit()