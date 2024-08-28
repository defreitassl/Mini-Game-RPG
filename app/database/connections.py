import mysql.connector


def create_conn():
    """Cria uma conexão com o banco de dados MySQL e retorna a conexão e o cursor."""
    try:
        # Define as configurações da conexão com o banco de dados
        connection = mysql.connector.connect(
            host='127.0.0.1',  # Endereço do host do banco de dados (localhost)
            database='RPG',    # Nome do banco de dados a ser acessado
            user='root',       # Nome de usuário do banco de dados
            password='admin'   # Senha do banco de dados
        )
        
        # Verifica se a conexão foi estabelecida com sucesso
        if connection.is_connected():
            cursor = connection.cursor()  # Cria um cursor para executar comandos SQL
            print("\n Conexão com o banco de dados RPG bem-sucedida! \n")
            return connection, cursor  # Retorna a conexão e o cursor
    
    except Exception as e:
        # Exibe uma mensagem de erro caso algo dê errado
        print(f"Erro: {e}")
        return None
    

def close_conn(connection, cursor, commit=True):
    """Fecha a conexão com o banco de dados e o cursor."""
    try:
        # Fecha o cursor, se ele existir
        if cursor is not None:
            cursor.close()
        
        # Fecha a conexão, se ela existir
        if connection is not None:
            if commit:  # Se a flag commit estiver marcada como True, faz commit das mudanças
                connection.commit()
            connection.close()  # Fecha a conexão com o banco de dados
    
    except Exception as e:
        # Exibe uma mensagem de erro caso algo dê errado ao fechar a conexão ou o cursor
        print(f"Erro de fechamento na conexão ou no cursor: {e}") 
