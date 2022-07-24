# Monitora o valor do Bitcoin E dispara um email Caso haja uma Mudanca significativa 

import requests 
import json 
import time
from main import email



def obter_valor():


    try:

        url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=BRL"

        response = requests.get(url)
        dados = response.json()
        valor_reais = float(dados['BRL'])
        valor_formatado_reais = "{:,.3f}".format(valor_reais)
        valor = valor_formatado_reais
        return valor

    except: 
        print('Erro')


novo = True
valor_novo = obter_valor()
valor_atual = obter_valor()
email(f'Valor Atual Do Bitcoin{valor_atual}')

while True:

    valor_novo = obter_valor()

    if valor_novo < valor_atual:
        print(f'\033[33m---> O valor esta caindo 1 bitcoin custa R${valor_novo} Reais\033[m')
        valor_atual = valor_novo

    elif valor_novo > valor_atual:
        print(f'\033[36m---> O valor esta subindo 1 bitcoin custa R${valor_novo} Reais\033[m')
        valor_atual = valor_novo

    elif valor_novo == valor_atual:
        print(f'O valor do bitcoin permanece o mesmo, aguardando mudanca... ')

    else:
        print('houve um problema ao acessar o link...')

    time.sleep(10)