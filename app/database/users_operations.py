from .connections import create_conn, close_conn


def insert_user(name, username, password) -> None:
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


def verify_username_not_in_db(username) -> bool:
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
