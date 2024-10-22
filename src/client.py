import socket
import logging
from libs.crud_client import CrudClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_coneect(host, port):
    host = 'localhost'
    porta = 5000
    
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, porta))
    return cliente_socket

def cliente():
    cliente_socket = start_coneect('localhost', 50000)
    crud_client = CrudClient()

    while True:
        print("# Programa de gestão #")
        print("Operacoes disponiveis: ")
        print("CREATE | READ | UPDATE | DELETE | READ-ALL | EXIT")
        operacao = input(">> Digite a operação: ")
 
        comando = ""
        match operacao:
            case "CREATE":
                comando = crud_client.create()
            case "READ":
                comando = crud_client.read()
            case "UPDATE":
                comando = crud_client.update()
            case "DELETE":
                comando = crud_client.delete()
            case "READ-ALL":
                comando = crud_client.read_all()
            case "EXIT":
                break
            case "":
                print("Imput incorreto, tente novamente.")
            case _:
                print("Opção inválida.")
                continue

        print(f"comando: {comando}")
        if comando == "":
            break

        msg = comando.encode()
        tam = (len(msg)).to_bytes(2, 'big')
        cliente_socket.send(tam + msg)

        bytes_resp = cliente_socket.recv(2)
        if not bytes_resp:
            print("Conexão encerrada.")
            break

        tam_resp = int.from_bytes(bytes_resp, 'big')
        resposta = cliente_socket.recv(tam_resp).decode()
        print(f"Resposta do servidor: {resposta}")

        if "Encerrando conexão." in resposta:
            break

    cliente_socket.close()

if __name__ == "__main__":
    cliente()
