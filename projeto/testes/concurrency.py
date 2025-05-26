import requests
from concurrent.futures import ThreadPoolExecutor
import time

URL       = "http://127.0.0.1:5000/pedido"
RELATORIO = "http://127.0.0.1:5000/relatorio"

def send_post(_):
    return requests.post(URL).status_code

if __name__ == "__main__":
    # dispara 20 requisições em paralelo
    with ThreadPoolExecutor(max_workers=10) as executor:
        codes = list(executor.map(send_post, range(20)))
    print("Códigos de resposta:", codes)

    # espera a fila esvaziar
    time.sleep(10)

    # busca o relatório final
    resp = requests.get(RELATORIO)
    print("Pedidos no relatório:", len(resp.json()))
    print(resp.json())
