from ..database.characters_operations import insert_character, add_character_id_to_user, get_character_id_from_db

class Character:
    """
    Classe que representa um personagem no jogo. 
    Contém todos os atributos do personagem e métodos para manipulação de dados relacionados ao personagem.
    """

    def __init__(self, user_id: int, category: str, age: int, 
        gender: str, strength: int, agility: int, health: int,
        stamina: int, intelligence: int, height: int,
        body_shape: str, skin_color: str, hair_color: str,
        biography: str, picture_src: str) -> None:
        
        # Atributos do personagem
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
        """
        Insere o personagem no banco de dados, vinculando-o ao usuário que o criou.
        Atualiza o ID do personagem no registro do usuário após a inserção.
        """
        # Insere o personagem no banco de dados
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
        # Obtém o ID do personagem recém-criado
        character_id = get_character_id_from_db(self.user_id)
        # Atualiza o registro do usuário com o ID do personagem
        update_user = add_character_id_to_user(self.user_id, character_id)
        
        if update_user:
            print("Usuário atualizado com sucesso.")
        else:
            print("Falha ao atualizar o usuário.")

    def __str__(self):
        """
        Retorna uma string formatada contendo todas as informações do personagem.
        Útil para depuração ou exibição das características do personagem.
        """
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
