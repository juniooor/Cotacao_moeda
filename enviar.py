import csv
import datetime
import smtplib
import ssl
from email.message import EmailMessage


# password = 'yqwbxnpeompbzwvh'
def eth_maior(valor_eth):
    with open ('email.csv', 'r', encoding='utf-8') as arquivo_csv:
        emails = csv.reader(arquivo_csv)
        next(emails)
        
        for dados in emails:
            email_sender = 'testesdevjremail@gmail.com'
            email_password = "cnfkcyfeazjlvnov"
            email_receiver = dados[0]
            data = datetime.date.today()
            data = data.strftime('%d-%b-%Y')
            subject = 'Valor ETH subiu '
            corpo_email = f"""
                Olá {dados[1]}.
                    Hoje a moeda Ethereum Subiu!!
                        {data}
                    >R${valor_eth} 
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
        return 'enviado'
    
def eth_menor(valor_eth):
    with open ('email.csv', 'r', encoding='utf-8') as arquivo_csv:
        emails = csv.reader(arquivo_csv)
        next(emails)
        
        for dados in emails:
            email_sender = 'testesdevjremail@gmail.com'
            email_password = "cnfkcyfeazjlvnov"
            email_receiver = dados[0]
            data = datetime.date.today()
            data = data.strftime('%d-%b-%Y')
            subject = 'Valor ETH desceu'
            corpo_email = f"""
                Olá {dados[1]}.
                    Hoje a moeda Ethereum Desceu!!
                        {data}
                    >R${valor_eth} 
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
        return 'enviado'
                    
def eth_atual(valor_eth):
    with open ('email.csv', 'r', encoding='utf-8') as arquivo_csv:
        emails = csv.reader(arquivo_csv)
        next(emails)
        
        for dados in emails:
            email_sender = 'testesdevjremail@gmail.com'
            email_password = "cnfkcyfeazjlvnov"
            email_receiver = dados[0]
            data = datetime.date.today()
            data = data.strftime('%d-%b-%Y')
            subject = 'Valor Atual ETH'
            corpo_email = f"""
                Olá {dados[1]}.
                    Valor atual moeda Ethereum!!
                        {data}
                    >R${valor_eth} 
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
        return 'enviado'
                                       