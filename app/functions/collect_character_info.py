from ..classes.character import Character

def collect_character_info(category, age, gender: str, strength, agility, health, 
                           stamina, intelligence, height, body_shape, skin_color, 
                           hair_color, biography, picture_src) -> None:
    
    new_character = Character(category, age, gender, strength, agility, health, stamina, intelligence,
                              height, body_shape, skin_color, hair_color, biography, picture_src)
    print(new_character)
    new_character._insert_character_in_db()
