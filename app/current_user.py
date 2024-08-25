

def set_logged_user_id(user_id=None) -> None:
    global current_user_id
    current_user_id = user_id


def get_logged_user_id() -> int:
    global current_user_id
    if current_user_id != None:
        return current_user_id
    else:
        print('\n ID de usuário não encontrado ou não definido \n')


def set_logged_user_picture(picture_src=None):
    global current_user_picture
    current_user_picture = picture_src


def get_logged_user_picture():
    global current_user_picture
    if current_user_picture != None:
        return current_user_picture
    print('\n Usuário ainda não foi logado ou não encontrado \n')

current_user_id = None

current_user_picture = None