from ..classes.user import User
from ..database.users_operations import verify_username_not_in_db


def collect_account_info(page ,name, username, password, conf_password) -> None:
    
    name_value = name.value
    username_value = username.value
    password_value = password.value
    conf_password_value = conf_password.value

    name_valid = verify_name(name_value)
    username_valid = verify_username(username_value)
    password_valid = verify_password(password_value, conf_password_value)


    if not name_valid:
        name.error_text = 'Nome inválido'
        name.update()
    
    if not username_valid:
        username.error_text = 'Nome de usuário inválido, ou já existente'
        username.update()

    if not password_valid:

        if password_value != conf_password_value:
            conf_password.error_text = 'Senha incorreta tente novamente'
            conf_password.update()

        else:
            password.error_text = 'Senha fraca ou inválida'
            password.update()
    
    if all([name_valid, username_valid, password_valid]) == True:
        
        try:
            new_user = User(name=name_value, username=username_value, password=password_value)
            print(new_user)
            new_user.insert_user_in_db()
        
        except Exception as e:
            print(f'\n Erro inesperado ao criar o usuário: {e} \n')
        
        finally:
            page.go('/create-character')



def verify_name(name: str) -> bool:

    ver_name = name.split()

    if len(ver_name) == 2 and ver_name[0].isalpha() == True and ver_name[1].isalpha() == True:
        print('Nome ok \n')
        return True
    
    else:
        print('NomeInválido: Contém números ou caracteres especiais, ou contém menos ou mais do que 2 nomes (primeiroNome e ultimoNome) \n')
        return False


def verify_username(username: str) -> bool:

    user_not_in_db = verify_username_not_in_db(username)

    if user_not_in_db:

        ver_username = username.split()

        if len(ver_username) > 1 or len(username) < 4:
            print('NomeDeUsuárioInválido: Contém espaços ou menos de 4 caracteres \n')
            return False
        
        else:
            print('Username ok \n')
            return True
    
    else:
        print('Esse nome de usuário já existe.')
        return False

def verify_password(password: str, conf_password: str) -> bool:

    ver_password = password.split()

    if len(ver_password) > 1 or len(password) < 8:
        print('SenhaInválida: Contém espaços ou menos de 8 caracteres \n')
        return False
    
    elif password.isalpha() == True:
        print('SenhaFraca: Adicione no números ou caracteres especiais \n')
        return False

    else:
        print('Senha ok \n')
        
        if password == conf_password:
            print('Confirmação de senha ok \n')
            return True

        else:
            print('SenhaIncorreta: Senha e Confirmação de senha não são iguais \n')
            return False