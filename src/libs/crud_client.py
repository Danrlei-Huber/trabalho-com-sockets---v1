class CrudClient:
    
    def create(self) -> str:
        """
        Cria um comando de inserção de um veículo no formato:
        CREATE|<id>|<marca>|<modelo>|<ano>|<preco>#
        """
        id = int(input("# ID: "))
        marca = input("# Marca: ")
        modelo = input("# Modelo: ")
        ano = int(input("# Ano: "))
        preco = float(input("# Preço: "))
        comando = f"CREATE|{id}|{marca}|{modelo}|{ano}|{preco}#"
        return comando

    def read(self) -> str:
        """
        Cria um comando de leitura de um veículo no formato:
        READ|<id>#
        """
        id = int(input("# ID: "))
        comando = f"READ|{id}#"
        return comando

    def update(self) -> str:
        """
        Cria um comando de atualização de um veículo no formato:
        UPDATE|<id>|<marca>|<modelo>|<ano>|<preco>#
        """
        id = int(input("# ID: ") or 0)
        marca = input("# Marca: ") or ""
        modelo = input("# Modelo: ") or ""
        ano = int(input("# Ano: ") or 0)
        preco = float(input("# Preço: ") or 0.0)
        comando = f"UPDATE|{id}|{marca}|{modelo}|{ano}|{preco}#"
        return comando

    def delete(self) -> str:
        """
        Cria um comando de exclusão de um veículo no formato:
        DELETE|<id>#
        """
        id = int(input("# ID: "))
        comando = f"DELETE|{id}#"
        return comando

    def read_all(self) -> str:
        """
        Cria um comando para ler todos os veículos no formato:
        READ-ALL
        """
        comando = "READ-ALL"
        return comando
