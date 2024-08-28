from ..database.users_operations import insert_user

class User:
    """
    Classe que representa um usuário no sistema. 
    Contém métodos para manipulação de dados relacionados ao usuário.
    """

    def __init__(self, name: str, username: str, password: str) -> None:
        
        # Atributos do usuário
        self._name = name
        self._username = username
        self.__password = password  # A senha é armazenada como um atributo privado
        self._character = None  # Atributo para armazenar o personagem associado ao usuário, se houver

    def _insert_user_in_db(self):
        """
        Insere o usuário no banco de dados.
        Chama a função `insert_user` para realizar a inserção no banco de dados.
        """
        insert_user(name=self._name, username=self._username, password=self.__password)

    def _get_password(self) -> str:
        """
        Retorna a senha do usuário.

        Returns:
            str: A senha armazenada no objeto.
        """
        return self.__password

    def __str__(self) -> str:

        return f"""
        Name: {self._name}
        Username: {self._username}
        Password: {'#' * len(self.__password)}  # A senha é mascarada para proteger os dados
        """
