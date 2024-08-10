

class Character:

    def __init__(self, category: str, age: int, gender: str,
        strength: int, agility: int, health: int,
        stamina: int, intelligence: int, height: int,
        body_shape: str, skin_color: str, hair_color,
        biography: str, picture_id: int) -> None:
        
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
        self.picture = f'/images/avatar{picture_id}.webp'

    
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
    

character = Character(
    category="Warrior",        # Categoria do personagem
    age=30,                    # Idade do personagem
    gender="Male",             # Gênero do personagem
    strength=80,               # Força do personagem
    agility=60,                # Agilidade do personagem
    health=100,                # Saúde do personagem
    stamina=75,                # Energia do personagem
    intelligence=50,           # Inteligência do personagem
    height=180,                # Altura do personagem em cm
    body_shape="Muscular",     # Tipo de corpo do personagem
    skin_color="Light",        # Cor da pele do personagem
    hair_color="Black",        # Cor do cabelo do personagem
    biography="A brave warrior from the northern lands, known for his unmatched strength and courage in battle.",  # Biografia
    picture_id=1               # ID da imagem do personagem
)

