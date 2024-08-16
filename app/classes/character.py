from ..database.characters_operations import insert_character, add_character_id_to_user

class Character:

    def __init__(self, user_id: int, category: str, age: int, 
        gender: str, strength: int, agility: int, health: int,
        stamina: int, intelligence: int, height: int,
        body_shape: str, skin_color: str, hair_color: str,
        biography: str, picture_src: str) -> None:
        
        self.user_id = user_id
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
        insert_character(
            user_id=self.user_id,
            category=self.category,
            age=self.age,
            gender=self.gender,
            strength=self.strength,
            agility=self.agility,
            health=self.health,
            stamina=self.stamina,
            intelligence=self.intelligence,
            height=self.height,
            body_shape=self.body_shape,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            biography=self.biography,
            picture_src=self.picture
        )
        add_character_id_to_user()

    
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
    


