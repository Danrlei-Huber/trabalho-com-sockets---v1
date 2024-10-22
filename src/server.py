import socket
import logging
from libs.veiculos_data import get_veiculos

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Lista de veículos (usando um dicionário)
veiculos = {}
veiculos = get_veiculos()

def processar_comando(comando):
    partes = comando.strip('#').split('|')
    operacao = partes[0]

    if len(partes) < 1:
        return "Formato invalido. "

    if operacao == "CREATE":
        id_veiculo = int(partes[1])
        veiculos[id_veiculo] = {
            'marca': partes[2],
            'modelo': partes[3],
            'ano': int(partes[4]),
            'preco': float(partes[5])
        }
        return f"Veículo {id_veiculo} criado com sucesso."
    
    elif operacao == "READ":
        id_veiculo = int(partes[1])
        if id_veiculo in veiculos:
            v = veiculos[id_veiculo]
            return (
                f"Veículo encontrado:\n"
                f"Marca: {v['marca']}\n"
                f"Modelo: {v['modelo']}\n"
                f"Ano: {v['ano']}\n"
                f"Preço: R${v['preco']:.2f}"
            )
        else:
            return "Veículo não encontrado."
    
    elif operacao == "UPDATE":
        id_veiculo = int(partes[1])
        try:
            veiculo_atual = veiculos[id_veiculo]
            if partes[2] != "":
                veiculo_atual['marca'] = partes[2]
            if partes[3] != "":
                veiculo_atual['modelo'] = partes[3]
            if partes[4] != "0":
                veiculo_atual['ano'] = int(partes[4])
            if partes[5] != "0.0":
                veiculo_atual['preco'] = float(partes[5])

            return f"Veículo {id_veiculo} atualizado com sucesso."
        except KeyError:
            return "Veículo não encontrado."

    elif operacao == "DELETE":
        id_veiculo = int(partes[1])
        if id_veiculo in veiculos:
            del veiculos[id_veiculo]
            return f"Veículo {id_veiculo} removido com sucesso."
        else:
            return "Veículo não encontrado."
    
    elif operacao == "READ-ALL":
        print("read all")
        if not veiculos:
            return "Nenhum veículo encontrado."
        
        lista_veiculos = [] 
        
        for id_veiculo, v in veiculos.items(): 
            veiculo_info = (
                f"ID: {id_veiculo} | "
                f"Marca: {v['marca']} | "
                f"Modelo: {v['modelo']} | "
                f"Ano: {v['ano']} | "
                f"Preço: R${v['preco']:.2f}" 
            )
            lista_veiculos.append(veiculo_info)  
        
        resultado = "\n".join(lista_veiculos) 
        logging.info(f"\n{resultado}") 
        
        return resultado

    elif operacao == "EXIT":
        return "Encerrando conexão."
    
    return "Comando inválido."

def servidor():
    host = 'localhost'
    porta = 5000

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(1)
    
    logging.info(f"Servidor ouvindo em {host}:{porta}")
    
    conn, addr = servidor_socket.accept()
    logging.info(f"Conexão de {addr}")

    while True:
        dados_tam = conn.recv(2)
        if not dados_tam:
            logging.warning("Devido ao corte da conexão o servidor esta encerrando")
            break
        
        tam_msg = int.from_bytes(dados_tam, 'big')
        dados = conn.recv(tam_msg).decode()
        logging.info(f"Dados recebidos: {dados}")
        if not dados:
            logging.warning("Não ha dados")
            break

        resposta = processar_comando(dados)
        resposta_bytes = resposta.encode()
        tam_resposta = len(resposta_bytes).to_bytes(2, 'big')
        conn.send(tam_resposta + resposta_bytes)
        if "Encerrando conexão." in resposta:
            break

    conn.close()

if __name__ == "__main__":
    servidor()
