from datetime import time

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
