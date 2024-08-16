from .connections import create_conn, close_conn


def insert_character(user_id: int, category: str, age: int, 
        gender: str, strength: int, agility: int, health: int,
        stamina: int, intelligence: int, height: int,
        body_shape: str, skin_color: str, hair_color: str,
        biography: str, picture_src: str):
    
    try:
        conn, cursor = create_conn()
        query = """
            INSERT INTO characters (user_id, category, age, gender, strength,
                                    agility, health, stamina, intelligence, height, body_shape,
                                    skin_color, hair_color, biography, picture_src)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
                query,
                [
                    user_id, 
                    category, 
                    age,
                    gender,
                    strength,
                    agility,
                    health,
                    stamina,
                    intelligence,
                    height,
                    body_shape,
                    skin_color,
                    hair_color,
                    biography,
                    picture_src
                ]
            )
        print('Personagem adicionado com sucesso.')
        close_conn(conn, cursor)
    
    except Exception as e:
        print(f'Erro ao adicionar personagem ao banco de dados: {e}')


def add_character_id_to_user():
    ...

    #Continuar a função para adicionar o id do personagem a ao seu usuário correspondente no db.