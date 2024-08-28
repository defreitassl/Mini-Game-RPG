from ..classes.character import Character
from ..current_user import get_logged_user_id

# Coleta todas as informações da criação de personagem e as envia para o banco de dados
def collect_character_info(category: str, age: int, gender: str, strength: int, agility: int, health: int, 
                           stamina: int, intelligence: int, height: int, body_shape: str, skin_color: str, 
                           hair_color: str, biography: str, picture_src: str) -> None:
    """
    Coleta todas as informações fornecidas para a criação de um personagem e as insere no banco de dados.

    Args:
        category (str): A classe ou categoria do personagem (e.g., Guerreiro, Mago).
        age (int): A idade do personagem.
        gender (str): O gênero do personagem (e.g., Masculino, Feminino).
        strength (int): O nível de força do personagem.
        agility (int): O nível de agilidade do personagem.
        health (int): O nível de saúde do personagem.
        stamina (int): O nível de estamina do personagem.
        intelligence (int): O nível de inteligência do personagem.
        height (int): A altura do personagem (em centímetros).
        body_shape (str): O tipo de corpo do personagem.
        skin_color (str): A cor da pele do personagem.
        hair_color (str): A cor do cabelo do personagem.
        biography (str): A biografia do personagem.
        picture_src (str): O caminho para a imagem de perfil do personagem.

    Returns:
        None
    """
    
    current_user_id = get_logged_user_id()  # Busca o ID do usuário logado atualmente
    
    # Cria um objeto personagem para encapsular suas informações e enviá-las ao banco de dados
    new_character = Character(
        current_user_id, category, round(age, 2), gender, 
        strength, agility, health, stamina, intelligence,
        height, body_shape, skin_color, hair_color, biography, picture_src
    )
    
    print(new_character)  # Imprime uma mensagem de apresentação do personagem
    new_character._insert_character_in_db()  # Insere o personagem no banco de dados
