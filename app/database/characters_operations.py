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
        print('\n Personagem adicionado com sucesso. \n')
        close_conn(conn, cursor)
    
    except Exception as e:
        print(f'\n Erro ao adicionar personagem ao banco de dados: {e} \n')


def add_character_id_to_user(current_user_id: int, character_id: int) -> bool:
    try:
        conn, cursor = create_conn()
        query = """
            UPDATE users
            SET character_id = %s
            WHERE user_id = %s
        """
        cursor.execute(query, [character_id, current_user_id])
        print(f' \n Usuário de id {current_user_id} atualizado com sucesso \n')
        close_conn(conn, cursor, )
        return True

    except Exception as e:
        print(f'\n Erro ao atualizar o usuário: {e}')
        return False
    

def get_character_id_from_db(user_id: int):
    
    try:
        conn, cursor = create_conn()
        query = """
            SELECT character_id FROM characters
            WHERE user_id = %s
        """
        cursor.execute(query, [user_id])
        rows = cursor.fetchall()
        close_conn(conn, cursor, commit=False)

        if not rows:
            print('\n ID de usuário não encontrado \n')
            return None
        
        else:
            character_id = rows[0][0]
            print(f'\n ID de personagem encontrado e coletado. \n')
            return character_id

    except Exception as e:
        print(f'Erro ao buscar ID de usuário no banco de dados: {e}')
        return None

