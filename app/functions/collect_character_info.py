from ..classes.character import Character
from ..current_user import get_logged_user_id


def collect_character_info(category: str, age: int, gender: str, strength: int, agility: int, health: int, 
                           stamina: int, intelligence: int, height: int, body_shape: str, skin_color: str, 
                           hair_color: str, biography: str, picture_src: str) -> None:
    
    current_user_id = get_logged_user_id()
    
    new_character = Character(current_user_id, category, round(age, 2), gender, strength, agility, health, stamina, intelligence,
                              height, body_shape, skin_color, hair_color, biography, picture_src)
    print(new_character)
    new_character._insert_character_in_db()
