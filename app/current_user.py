current_user_id = None


def set_logged_user_id(user_id: int) -> None:
    global current_user_id
    current_user_id = user_id
    print(f'\n Usuário de ID igual a {current_user_id} logado \n')


def get_logged_user_id() -> int:
    global current_user_id
    if current_user_id != None:
        return current_user_id
    else:
        print('\n ID de usuário não encontrado ou não definido \n')