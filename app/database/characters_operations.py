from .connections import create_conn, close_conn

def insert_character(user_id: int, category: str, age: int, 
        gender: str, strength: int, agility: int, health: int,
        stamina: int, intelligence: int, height: int,
        body_shape: str, skin_color: str, hair_color: str,
        biography: str, picture_src: str):
    """
    Insere um novo personagem no banco de dados.

    Args:
        user_id (int): ID do usuário associado ao personagem.
        category (str): Classe do personagem (ex: Arqueiro, Mago).
        age (int): Idade do personagem.
        gender (str): Gênero do personagem.
        strength (int): Valor da força do personagem.
        agility (int): Valor da agilidade do personagem.
        health (int): Valor da vida do personagem.
        stamina (int): Valor da estamina do personagem.
        intelligence (int): Valor da inteligência do personagem.
        height (int): Altura do personagem em centímetros.
        body_shape (str): Porte físico do personagem.
        skin_color (str): Cor da pele do personagem.
        hair_color (str): Cor do cabelo do personagem.
        biography (str): Biografia do personagem.
        picture_src (str): Caminho para a imagem de perfil do personagem.
    """
    try:
        # Cria uma conexão com o banco de dados e um cursor para executar comandos SQL
        conn, cursor = create_conn()
        
        # Query SQL para inserir um novo personagem na tabela "characters"
        query = """
            INSERT INTO characters (user_id, category, age, gender, strength,
                                    agility, health, stamina, intelligence, height, body_shape,
                                    skin_color, hair_color, biography, picture_src)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Executa a query SQL com os valores fornecidos
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
        # Fecha a conexão com o banco de dados
        close_conn(conn, cursor)
    
    except Exception as e:
        # Exibe uma mensagem de erro caso algo dê errado
        print(f'\n Erro ao adicionar personagem ao banco de dados: {e} \n')


def add_character_id_to_user(current_user_id: int, character_id: int) -> bool:
    """
    Adiciona o ID do personagem ao usuário no banco de dados.

    Args:
        current_user_id (int): ID do usuário atual.
        character_id (int): ID do personagem a ser associado ao usuário.

    Returns:
        bool: True se a atualização for bem-sucedida, False caso contrário.
    """
    try:
        # Cria uma conexão com o banco de dados e um cursor para executar comandos SQL
        conn, cursor = create_conn()
        
        # Query SQL para atualizar a tabela "users" com o ID do personagem
        query = """
            UPDATE users
            SET character_id = %s
            WHERE user_id = %s
        """
        
        # Executa a query SQL com os valores fornecidos
        cursor.execute(query, [character_id, current_user_id])
        print(f' \n Usuário de id {current_user_id} atualizado com sucesso \n')
        
        # Fecha a conexão com o banco de dados
        close_conn(conn, cursor)
        return True

    except Exception as e:
        # Exibe uma mensagem de erro caso algo dê errado
        print(f'\n Erro ao atualizar o usuário: {e}')
        return False


def get_character_id_from_db(user_id: int):
    """
    Obtém o ID do personagem associado a um usuário no banco de dados.

    Args:
        user_id (int): ID do usuário cujo personagem será recuperado.

    Returns:
        int: ID do personagem se encontrado, None caso contrário.
    """
    try:
        # Cria uma conexão com o banco de dados e um cursor para executar comandos SQL
        conn, cursor = create_conn()
        
        # Query SQL para selecionar o ID do personagem da tabela "characters"
        query = """
            SELECT character_id FROM characters
            WHERE user_id = %s
        """
        
        # Executa a query SQL com o ID do usuário fornecido
        cursor.execute(query, [user_id])
        rows = cursor.fetchall()
        
        # Fecha a conexão com o banco de dados sem confirmar transações
        close_conn(conn, cursor, commit=False)

        # Verifica se algum ID foi encontrado
        if not rows:
            print('\n ID de usuário não encontrado \n')
            return None
        
        else:
            # Retorna o ID do personagem encontrado
            character_id = rows[0][0]
            print(f'\n ID de personagem encontrado e coletado. \n')
            return character_id

    except Exception as e:
        # Exibe uma mensagem de erro caso algo dê errado
        print(f'\n Erro ao buscar ID de usuário no banco de dados: {e} \n')
        return None


def collect_character_info(user_id: int) -> any:
    """
    Coleta todas as informações do personagem do banco de dados.

    Args:
        user_id (int): ID do usuário cujo personagem será coletado.

    Returns:
        tuple: Contém todas as informações do personagem (categoria, idade, gênero, etc.), 
               ou False se algum problema for encontrado.
    """
    try:
        # Cria uma conexão com o banco de dados e um cursor para executar comandos SQL
        conn, cursor = create_conn()
        
        # Query SQL para selecionar todas as informações do personagem
        query = """
            SELECT category, age, gender, strength, agility, health, stamina, intelligence, height, body_shape, skin_color, hair_color, biography
            FROM characters WHERE user_id = %s
        """
        
        # Executa a query SQL com o ID do usuário fornecido
        cursor.execute(query, [user_id])
        result = cursor.fetchone()
        
        # Fecha a conexão com o banco de dados sem confirmar transações
        close_conn(conn, cursor, commit=False)

        # Verifica se o resultado foi encontrado
        if result is None:
            print('\n Nenhuma informação do personagem encontrada para esse user_id \n')
            return False

        # Desempacota o resultado corretamente
        category, age, gender, strength, agility, health, stamina, intelligence, height, body_shape, skin_color, hair_color, biography = result

        # Verifica se todas as informações são válidas
        if all([category, age, gender, height, body_shape, skin_color, hair_color, biography]):
            return category, age, gender, strength, agility, health, stamina, intelligence, height, body_shape, skin_color, hair_color, biography
        else:
            print('\n Alguma informação do personagem está inválida ou inexistente \n')
            return False

    except Exception as e:
        # Exibe uma mensagem de erro caso algo dê errado
        print(f'\n Erro ao coletar informações do personagem: {e}\n')
        return False
