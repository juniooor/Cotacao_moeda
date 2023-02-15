import csv
import datetime
import smtplib
import ssl
from email.message import EmailMessage

import requests

requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/ETH-BRL")

requisicao_dict = requisicao.json()

valor_eth = requisicao_dict["ETHBRL"]["bid"]
horario = requisicao_dict["ETHBRL"]["create_date"]

if valor_eth < '7826':
    print('menor', valor_eth )
elif valor_eth > '8200':
    print('maior', valor_eth)
    
ethereumRegister = valor_eth

# password = 'yqwbxnpeompbzwvh'

with open ('email.csv', 'r', encoding='utf-8') as arquivo_csv:
    emails = csv.reader(arquivo_csv)
    next(emails)
    
    for dados in emails:
        email_sender = 'testesdevjremail@gmail.com'
        email_password = "cnfkcyfeazjlvnov"
        email_receiver = dados[0]
        data = datetime.date.today()
        data = data.strftime('%d-%b-%Y')
        subject = 'Valor da Moeda '
        corpo_email = f"""
            Olá {dados[1]}.
                Hoje a moeda Ethereum
                    {data}
                >R${ethereumRegister} 
            """

        msg = EmailMessage()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg.set_content(corpo_email)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context ) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
            print('enviado')