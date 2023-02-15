import requests

import enviar

requisicao = requests.get(
    "http://economia.awesomeapi.com.br/json/last/ETH-BRL"
    ).json()

valor_eth = requisicao["ETHBRL"]["bid"]

if valor_eth < '7826':
    enviar.eth_menor(valor_eth=valor_eth)
elif valor_eth > '8200':
    enviar.eth_maior(valor_eth=valor_eth)
    

