
class User:
    
    def __init__(self, name: str, username: str, password: str) -> None:
        
        self._name = name
        self._username = username
        self.__password = password
        self._character = None


    def __get_password(self) -> str:
        return self.__password

    
    def __str__(self) -> str:
        return f"""
        Name: {self._name}
        Username: {self._username}
        Password: {self.__password.replace(self.__password, '#'*len(self.__password))}
        """
