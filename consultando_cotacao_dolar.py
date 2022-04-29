import requests
import json
import time
import datetime

while True:
    print('(1) Dólar')
    print('(2) Euro')
    print('(3) Bitcoin')
    opcao = input('Digite a opção:\n')
    if opcao == '1':
        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        cotacao = json.loads(requisicao.text)
        print('### COTACAO ### ', datetime.datetime.now())
        print('Dólar máximo: ', cotacao['USDBRL']['high'])
        print('Dólar mínimo: ', cotacao['USDBRL']['low'])
    elif opcao == '2':
        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        cotacao = json.loads(requisicao.text)
        print('### COTACAO ### ', datetime.datetime.now())
        print('Euro máximo: ', cotacao['EURBRL']['high'])
        print('Euro minimo: ', cotacao['EURBRL']['low'])
    elif opcao == '3':
        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        cotacao = json.loads(requisicao.text)
        print('### COTACAO ### ', datetime.datetime.now())
        print('Bitcoin máximo: ', cotacao['BTCBRL']['high'])
        print('Bitcoin mínimo: ', cotacao['BTCBRL']['low'])
    else:
        print('Opção inválida')
    print()
    time.sleep(2)
