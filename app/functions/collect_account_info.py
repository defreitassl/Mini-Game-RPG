import bcrypt
from ..classes.user import User
from ..database.users_operations import verify_username_not_in_db, get_user_id_from_db
from ..current_user import set_logged_user_id

# Função principal para coletar e validar as informações da conta durante a criação de um novo usuário
def collect_account_info(page, name, username, password, conf_password) -> None:
    """
    Coleta as informações da conta, valida os dados e, se válidos, cria um novo usuário no banco de dados.

    Args:
        page: Referência à página atual para manipulação da interface.
        name: Campo de entrada para o nome do usuário.
        username: Campo de entrada para o nome de usuário.
        password: Campo de entrada para a senha.
        conf_password: Campo de entrada para a confirmação da senha.
    """
    
    # Obtém os valores dos campos de entrada
    name_value = name.value
    username_value = username.value
    password_value = password.value
    conf_password_value = conf_password.value

    # Validações individuais para nome, nome de usuário e senha
    name_valid = verify_name(name_value)
    username_valid = verify_username(username_value)
    password_valid = verify_password(password_value, conf_password_value)

    # Exibe erros caso o nome seja inválido
    if not name_valid:
        name.error_text = 'Nome inválido'
        name.update()
    
    # Exibe erros caso o nome de usuário seja inválido ou já exista
    if not username_valid:
        username.error_text = 'Nome de usuário inválido, ou já existente'
        username.update()

    # Exibe erros caso a senha seja inválida ou a confirmação não coincida com a senha
    if not password_valid:
        if password_value != conf_password_value:
            conf_password.error_text = 'Senha incorreta, tente novamente'
            conf_password.update()
        else:
            password.error_text = 'Senha fraca ou inválida'
            password.update()
    
    # Se todas as validações passarem, cria o novo usuário
    if all([name_valid, username_valid, password_valid]) == True:
        
        try:
            # Gerando o hash da senha e convertendo para string
            hashed_password = bcrypt.hashpw(password_value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Cria um novo objeto de usuário e insere no banco de dados
            new_user = User(name=name_value, username=username_value, password=hashed_password)
            print(new_user)
            new_user._insert_user_in_db()
            
            # Obtém o ID do novo usuário a partir do nome de usuário
            user_id = get_user_id_from_db(username_value)
            
            if user_id:
                # Define o ID do usuário logado e redireciona para a página de criação de personagem
                set_logged_user_id(user_id=user_id)
                page.go('/create-character')
                
                # Limpa os valores dos campos de entrada após o sucesso
                name.value = ''
                name.error_text = None
                username.value = ''
                username.error_text = None
                password.value = ''
                password.error_text = None
                conf_password.value = ''
                conf_password.error_text = None
            
            else:
                pass
        
        except Exception as e:
            print(f'\n Erro inesperado ao criar o usuário: {e} \n')

# Função para verificar a validade do nome
def verify_name(name: str) -> bool:
    """
    Verifica se o nome fornecido é válido, ou seja, se contém dois nomes (primeiro e último) e apenas letras.

    Args:
        name (str): O nome completo a ser verificado.

    Returns:
        bool: Retorna True se o nome for válido, caso contrário, False.
    """

    # Divide o nome em partes e verifica se contém dois nomes válidos (primeiro e último)
    ver_name = name.split()

    if len(ver_name) == 2 and ver_name[0].isalpha() == True and ver_name[1].isalpha() == True:
        
        print('Nome ok \n')
        return True
    
    else:
        print('NomeInválido: Contém números ou caracteres especiais, ou contém menos ou mais do que 2 nomes (primeiroNome e ultimoNome) \n')
        return False

# Função para verificar a validade do nome de usuário
def verify_username(username: str) -> bool:
    """
    Verifica se o nome de usuário fornecido é válido e se já não está presente no banco de dados.

    Args:
        username (str): O nome de usuário a ser verificado.

    Returns:
        bool: Retorna True se o nome de usuário for válido e único, caso contrário, False.
    """

    # Verifica se o nome de usuário já não está presente no banco de dados
    user_not_in_db = verify_username_not_in_db(username)

    if user_not_in_db:

        # Verifica se o nome de usuário contém espaços ou é muito curto
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

# Função para verificar a validade da senha e sua confirmação
def verify_password(password: str, conf_password: str) -> bool:
    """
    Verifica se a senha é válida, ou seja, se atende aos critérios de segurança 
    e se a confirmação da senha corresponde à senha.

    Args:
        password (str): A senha fornecida pelo usuário.
        conf_password (str): A confirmação da senha fornecida pelo usuário.

    Returns:
        bool: Retorna True se a senha for válida e a confirmação corresponder, caso contrário, False.
    """

    # Verifica se a senha contém espaços ou é muito curta
    ver_password = password.split()

    if len(ver_password) > 1 or len(password) < 8:
        
        print('SenhaInválida: Contém espaços ou menos de 8 caracteres \n')
        return False
    
    # Verifica se a senha é composta apenas por letras (indicando uma senha fraca)
    elif password.isalpha() == True:
        
        print('SenhaFraca: Adicione números ou caracteres especiais \n')
        return False

    else:
        print('Senha ok \n')
        
        # Verifica se a senha e a confirmação coincidem
        if password == conf_password:
            print('Confirmação de senha ok \n')
            return True

        else:
            print('SenhaIncorreta: Senha e Confirmação de senha não são iguais \n')
            return False
