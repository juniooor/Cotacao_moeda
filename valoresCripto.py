from datetime import time

import requests

requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/ETH-BRL")

requisicao_dict = requisicao.json()
print(f'valor atual = {requisicao_dict["ETHBRL"]["bid"]}')
print(f'horario da consulta = {requisicao_dict["ETHBRL"]["create_date"]}')