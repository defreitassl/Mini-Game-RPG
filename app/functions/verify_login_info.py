import bcrypt
import flet as ft
from ..database.users_operations import get_user_hashed_password_from_db, check_login_info_in_db
from ..current_user import set_logged_user_id

def verify_login_info(page, username, password) -> None:
    """
    Verifica e valida as informações de login fornecidas pelo usuário.

    Args:
        page: A página atual onde a função está sendo executada.
        username: Campo de entrada que contém o nome de usuário.
        password: Campo de entrada que contém a senha do usuário.
    
    Returns:
        None
    """

    # Seleciona o valor dos objetos de input
    username_value = username.value
    password_value = password.value

    # Busca o hash da senha no banco de dados com base no nome de usuário fornecido
    stored_hashed_password = get_user_hashed_password_from_db(username_value)

    #Checa se os valores são todos verdadeiros para prosseguir o código
    if stored_hashed_password and bcrypt.checkpw(password_value.encode('utf-8'), stored_hashed_password.encode('utf-8')):
        
        user_id = check_login_info_in_db(username_value, stored_hashed_password) #Busca o id do usuário caso a senha e o nome de usuário estiverem corretos
        
        #Redireciona para a home-page caso o id de usuário esteja correto
        if user_id:
            set_logged_user_id(user_id) #Define o ID de usuário logado atualmente para fazer buscas futuras com base no ID
            page.go('/home-page')
            #Limpa os inputs e mensagens de erro
            username.value = ''
            password.value = ''
            username.error_text = None
            password.error_text = None
        
        #Mensagem de erro caso a senha esteja incorreta
        else:
            username.error_text = 'Nome de usuário ou senha inválidos'
            password.error_text = 'Nome de usuário ou senha inválidos'
            username.update()
            password.update()
            print('\n Login Inválido \n')
    #Mensagem de erro caso o usuário esteja incorreto
    else:
        username.error_text = 'Nome de usuário ou senha inválidos'
        password.error_text = 'Nome de usuário ou senha inválidos'
        username.update()
        password.update()
        print('\n Login Inválido \n')
