from .connections import create_conn, close_conn


def insert_user(name: str, username: str, password: str) -> None:
    try:
        conn, cursor = create_conn()
        query = """
            INSERT INTO users(name, username, password)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, [name, username, password])
        print('\n Usuário adicionado com sucesso \n')
        close_conn(conn, cursor)
    except Exception as e:
        print(f'\n Erro ao adicionar usuário no Banco de Dados: {e}\n')


def verify_username_not_in_db(username: str) -> bool:
    try: 
        conn, cursor = create_conn()
        query = """
            SELECT username FROM users
            WHERE username = %s
        """
        cursor.execute(query, [username])
        rows = cursor.fetchall()
        close_conn(conn, cursor, commit=False)
        
        if not rows:
            print('\n Nenhum Username igual encontrado. \n')
            return True
        else:
            print('\n UsernameRepetido: Um username igual já existe no banco de dados \n')
            return False
        
    except Exception as e:
        print(f'\n Erro ao consultar usuários no banco de dados: {e} \n')


def get_user_id_from_db(username: str) -> any:
    try:
        conn, cursor = create_conn()
        query = """
            SELECT user_id FROM users
            WHERE username = %s
        """
        cursor.execute(query, [username])
        rows = cursor.fetchall()
        close_conn(conn, cursor, commit=False)

        if not rows:
            print('\n Usuário não encontrado na base de dados \n')
            return False
        
        else:
            user_id = rows[0][0]
            print(f'\n Conectado como {username}.')
            return user_id
    
    except Exception as e:
        print(f'\n Erro ao conectar ou consultar o banco de dados: {e} \n')
        return None