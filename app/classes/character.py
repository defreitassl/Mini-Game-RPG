from ..database.characters_operations import insert_character

class Character:

    def __init__(self, category: str, age: int, gender: str,
        strength: int, agility: int, health: int,
        stamina: int, intelligence: int, height: int,
        body_shape: str, skin_color: str, hair_color: str,
        biography: str, picture_src: str) -> None:
        
        self.category = category
        self.age = age
        self.gender = gender
        self.strength = strength
        self.agility = agility
        self.health = health
        self.stamina = stamina
        self.intelligence = intelligence
        self.height = height
        self.body_shape = body_shape
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.biography = biography
        self.picture = picture_src


    def _insert_character_in_db(self):
        insert_character()

    
    def __str__(self):
        return f"""
            Personagem:

            Categoria: {self.category}
            Idade: {self.age}
            Gênero: {self.gender}
            Força: {self.strength}
            Agilidade: {self.agility}
            Saúde: {self.health}
            Energia: {self.stamina}
            Inteligência: {self.intelligence}
            Altura: {self.height} cm
            Tipo de Corpo: {self.body_shape}
            Cor da Pele: {self.skin_color}
            Cor do Cabelo: {self.hair_color}
            Biografia: {self.biography}
            Foto de Perfil: {self.picture}
        """
    


