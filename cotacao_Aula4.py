import requests 

requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_a = requisicao.json()
cotacao_dolar = requisicao_a["USDBRL"]["bid"]
cotacao_euro = requisicao_a["EURBRL"]["bid"]
cotacao_bitcon = requisicao_a["BTCBRL"]["bid"]

print(cotacao_dolar)
print(cotacao_euro)
print(cotacao_bitcon)
