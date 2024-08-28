import flet as ft
from ..database.users_operations import check_login_info_in_db
from ..current_user import set_logged_user_id

#Verifica e valida as informações de login fornecidas pelo usuário
def verify_login_info(page, username, password) -> None:
    
    #Seleciona o valor dos objetos de input
    username_value = username.value
    password_value = password.value

    user_id = check_login_info_in_db(username_value, password_value) #Busca o ID do usuário no BD através do username, já que ele também é único

    if user_id:

        set_logged_user_id(user_id) #Define o ID do usuário logado atualmente para operações futuras

        page.go('/home-page') #Redireciona para a página principal

        #Limpa os valores dos inputs para evitar trabalho do usuário posteriormente
        username.value = ''
        password.value = ''

    else:
        #Gera mensagens de erro no input para alertar o usuário caso erre algo
        username.error_text = 'Nome de usuário ou senha inválidos'
        password.error_text = 'Nome de usuário ou senha inválidos'
        username.update()
        password.update()
        print('\n Login Inválido \n')