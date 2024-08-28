from ..current_user import set_logged_user_id

#Função para que reseta o ID de usuário logado e volta a página inicial para fazer o LogOut
def log_out(page):
    """
    Reseta o ID de usuário logado e volta a página inicial para fazer o LogOut

    Args:
        page: ft.Page

    Returns:
        None
    """

    # Log para confirmar que a função foi chamada
    print("Botão de desconectar foi clicado. Iniciando o logout...")

    # Limpa as informações do usuário logado
    set_logged_user_id(None)

    #Redirecionan para a págin de login e avisa isso no terminal
    page.go('/login')
    print("Reiniciando a página e navegando para a tela de login...")
