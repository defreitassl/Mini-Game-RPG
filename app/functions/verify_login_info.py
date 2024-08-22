import flet as ft
from ..database.users_operations import check_login_info_in_db, get_user_picture_from_db
from ..current_user import set_logged_user_id, set_logged_user_picture
from ..interface.home_page import HomePage


def verify_login_info(page, username, password) -> None:
    
    username_value = username.value
    password_value = password.value

    user_id = check_login_info_in_db(username_value, password_value)

    if user_id:
        # Define o ID do usuário logado
        set_logged_user_id(user_id)

        # Obtém o caminho da imagem
        picture_src = get_user_picture_from_db()
        set_logged_user_picture(picture_src)

        # Redireciona para a home-page e limpa as visualizações antigas
        page.views.clear()  # Limpa todas as visualizações anteriores
        page.views.append(ft.View(route='/home-page', controls=[HomePage(page, picture_src)]))
        page.update()

    else:
        username.error_text = 'Nome de usuário ou senha inválidos'
        password.error_text = 'Nome de usuário ou senha inválidos'
        username.update()
        password.update()
        print('\n Login Inválido \n')