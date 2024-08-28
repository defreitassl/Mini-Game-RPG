#Modifica o ID do usuário logado atualmente
def set_logged_user_id(user_id=None) -> None:
    global current_user_id
    current_user_id = user_id

#Busca e retorna o ID para que seja importado em outros arquivos
def get_logged_user_id() -> int:
    global current_user_id
    if current_user_id != None:
        return current_user_id
    else:
        print('\n ID de usuário não encontrado ou não definido \n')


current_user_id = None
