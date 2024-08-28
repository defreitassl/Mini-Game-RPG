import bcrypt
import flet as ft
from ..database.users_operations import get_user_hashed_password_from_db, check_login_info_in_db
from ..current_user import set_logged_user_id

def verify_login_info(page, username, password) -> None:
    
    # Seleciona o valor dos objetos de input
    username_value = username.value
    password_value = password.value

    stored_hashed_password = get_user_hashed_password_from_db(username_value)

    if stored_hashed_password and bcrypt.checkpw(password_value.encode('utf-8'), stored_hashed_password.encode('utf-8')):
        
        user_id = check_login_info_in_db(username_value, stored_hashed_password)
        
        if user_id:
            set_logged_user_id(user_id)
            page.go('/home-page')
            username.value = ''
            password.value = ''
            username.error_text = None
            password.error_text = None
        
        else:
            username.error_text = 'Nome de usuário ou senha inválidos'
            password.error_text = 'Nome de usuário ou senha inválidos'
            username.update()
            password.update()
            print('\n Login Inválido \n')
    else:
        username.error_text = 'Nome de usuário ou senha inválidos'
        password.error_text = 'Nome de usuário ou senha inválidos'
        username.update()
        password.update()
        print('\n Login Inválido \n')
