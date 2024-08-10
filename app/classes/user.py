from ..database.users_operations import insert_user


class User:
    
    def __init__(self, name: str, username: str, password: str) -> None:
        
        self._name = name
        self._username = username
        self.__password = password
        self._character = None

    
    def insert_user_in_db(self):
        insert_user(name=self._name, username=self._username, password=self.__password)


    def _get_password(self) -> str:
        return self.__password

    
    def __str__(self) -> str:
        return f"""
        Name: {self._name}
        Username: {self._username}
        Password: {self.__password.replace(self.__password, '#'*len(self.__password))}
        """
