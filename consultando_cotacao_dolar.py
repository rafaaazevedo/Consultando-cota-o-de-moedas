import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = json.loads(requisicao.text)

    print('### COTACAO ### ', datetime.datetime.now())
    print('Dólar máximo: ', cotacao['USDBRL']['high'])
    print('Dólar mínimo: ', cotacao['USDBRL']['low'])
    print('Euro máximo: ', cotacao['EURBRL']['high'])
    print('Euro minimo: ', cotacao['EURBRL']['low'])
    print('Bitcoin máximo: ', cotacao['BTCBRL']['high'])
    print('Bitcoin mínimo: ', cotacao['BTCBRL']['low'])
    print()
    time.sleep(2)
