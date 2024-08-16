from .connections import create_conn, close_conn


def insert_character(category: str, age: int, gender: str,
        strength: int, agility: int, health: int,
        stamina: int, intelligence: int, height: int,
        body_shape: str, skin_color: str, hair_color: str,
        biography: str, picture_src: str):
    
    try:
        conn, cursor = create_conn()
        query = """
            INSERT INTO characters ()
            VALUES ()
        """
        cursor.execute(query, [])
        print('Personagem adicionado com sucesso.')
        close_conn(conn, cursor)
    
    except Exception as e:
        print(f'Erro ao adicionar personagem ao banco de dados: {e}')
