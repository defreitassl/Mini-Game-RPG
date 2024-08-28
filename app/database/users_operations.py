from .connections import create_conn, close_conn
from ..current_user import get_logged_user_id


def insert_user(name: str, username: str, password: str) -> None:
    """
    Insere um novo usuário no banco de dados.

    Args:
        name (str): Nome do usuário.
        username (str): Nome de usuário único.
        password (str): Senha do usuário (em formato hash).
    """
    try:
        conn, cursor = create_conn()  # Cria conexão com o banco de dados
        query = """
            INSERT INTO users(name, username, password)
            VALUES (%s, %s, %s)
        """  # Consulta SQL para inserir o novo usuário
        cursor.execute(query, [name, username, password])  # Executa a consulta
        print('\n Usuário adicionado com sucesso \n')
        close_conn(conn, cursor)  # Fecha a conexão com o banco de dados
    except Exception as e:
        # Exibe mensagem de erro em caso de falha
        print(f'\n Erro ao adicionar usuário no Banco de Dados: {e}\n')


def verify_username_not_in_db(username: str) -> bool:
    """
    Verifica se o nome de usuário já existe no banco de dados.

    Args:
        username (str): Nome de usuário a ser verificado.

    Returns:
        bool: Retorna True se o nome de usuário não existir, False caso contrário.
    """
    try: 
        conn, cursor = create_conn()  # Cria conexão com o banco de dados
        query = """
            SELECT username FROM users
            WHERE username = %s
        """  # Consulta SQL para verificar o username
        cursor.execute(query, [username])  # Executa a consulta
        rows = cursor.fetchall()  # Recupera os resultados
        close_conn(conn, cursor, commit=False)  # Fecha a conexão com o banco de dados
        
        if not rows:
            # Username não encontrado, pode ser usado
            print('\n Nenhum Username igual encontrado. \n')
            return True
        else:
            # Username já existe no banco de dados
            print('\n UsernameRepetido: Um username igual já existe no banco de dados \n')
            return False
        
    except Exception as e:
        # Exibe mensagem de erro em caso de falha
        print(f'\n Erro ao consultar usuários no banco de dados: {e} \n')


def get_user_id_from_db(username: str) -> any:
    """
    Obtém o ID do usuário a partir do banco de dados com base no username.

    Args:
        username (str): Nome de usuário para o qual o ID deve ser recuperado.

    Returns:
        any: Retorna o ID do usuário se encontrado, caso contrário, retorna False.
    """
    try:
        conn, cursor = create_conn()  # Cria conexão com o banco de dados
        query = """
            SELECT user_id FROM users
            WHERE username = %s
        """  # Consulta SQL para recuperar o ID do usuário
        cursor.execute(query, [username])  # Executa a consulta
        rows = cursor.fetchall()  # Recupera os resultados
        close_conn(conn, cursor, commit=False)  # Fecha a conexão com o banco de dados

        if not rows:
            # Usuário não encontrado
            print('\n Usuário não encontrado na base de dados \n')
            return False
        
        else:
            # Retorna o ID do usuário encontrado
            user_id = rows[0][0]
            print(f'\n Conectado como {username}.')
            return user_id
    
    except Exception as e:
        # Exibe mensagem de erro em caso de falha
        print(f'\n Erro ao conectar ou consultar o banco de dados: {e} \n')
        return None
    

def check_login_info_in_db(username: str, password: str):
    """
    Verifica se as informações de login estão corretas no banco de dados.

    Args:
        username (str): Nome de usuário fornecido.
        password (str): Senha fornecida (em formato hash).

    Returns:
        any: Retorna o ID do usuário se o login for bem-sucedido, caso contrário, retorna False.
    """
    try:
        user_id = get_user_id_from_db(username)  # Obtém o ID do usuário
        
        if user_id:
            conn, cursor = create_conn()  # Cria conexão com o banco de dados
            query = """
                SELECT password FROM users
                WHERE user_id = %s
            """  # Consulta SQL para recuperar a senha do usuário
            cursor.execute(query, [user_id])  # Executa a consulta
            rows = cursor.fetchall()  # Recupera os resultados
            close_conn(conn, cursor, commit=False)  # Fecha a conexão com o banco de dados

            if not rows:
                # Usuário não encontrado
                print('\n Usuário não encontrado no banco de dados \n')
                return False
            
            # Verifica se a senha fornecida é válida
            password_valid = True if rows[0][0] == password else False
            
            if password_valid:
                # Senha válida, retorna o ID do usuário
                print('\n Usuário encontrado e conectado com sucesso \n')
                return user_id
            else:
                # Senha inválida
                print('\n Senha inválida.')
                return False
    
    except Exception as e:
        # Exibe mensagem de erro em caso de falha
        print(f'\n Erro ao verificar informações de login no banco de dados: {e} \n')
        return None
    

def get_user_hashed_password_from_db(username: str) -> str:
    """
    Obtém a senha hash do usuário a partir do banco de dados com base no username.

    Args:
        username (str): Nome de usuário para o qual a senha hash deve ser recuperada.

    Returns:
        str: Senha hash do usuário, ou None se o usuário não for encontrado.
    """
    try:
        conn, cursor = create_conn()  # Cria conexão com o banco de dados
        query = """
            SELECT password FROM users
            WHERE username = %s
        """  # Consulta SQL para recuperar a senha hash do usuário
        cursor.execute(query, [username])  # Executa a consulta
        rows = cursor.fetchall()  # Recupera os resultados
        close_conn(conn, cursor, commit=False)  # Fecha a conexão com o banco de dados

        if not rows:
            # Usuário não encontrado
            print('\n Usuário não encontrado na base de dados \n')
            return None
        
        else:
            # Retorna a senha hash do usuário
            hashed_password = rows[0][0]
            return hashed_password
    
    except Exception as e:
        # Exibe mensagem de erro em caso de falha
        print(f'\n Erro ao conectar ou consultar o banco de dados: {e} \n')
        return None
    

def get_user_picture_from_db() -> str:
    """
    Obtém a imagem de perfil do personagem a partir do banco de dados com base no ID do usuário.

    Returns:
        str: Caminho da imagem de perfil do personagem, ou None em caso de erro.
    """
    user_id = get_logged_user_id()  # Obtém o ID do usuário logado

    try:
        conn, cursor = create_conn()  # Cria conexão com o banco de dados
        query = """
            SELECT picture_src FROM characters
            WHERE user_id = %s
        """  # Consulta SQL para recuperar a imagem do personagem
        cursor.execute(query, [user_id])  # Executa a consulta
        rows = cursor.fetchall()  # Recupera os resultados
        close_conn(conn, cursor, commit=False)  # Fecha a conexão com o banco de dados
        
        picture_src = rows[0][0]  # Obtém o caminho da imagem
        return picture_src
    
    except Exception as e:
        # Exibe mensagem de erro em caso de falha
        print(f'\n Erro ao consultar foto de perfil de personagem: {e} \n')
        return None
