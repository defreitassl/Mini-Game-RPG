from ..current_user import set_logged_user_id


def log_out(page):
    # Log para confirmar que a função foi chamada
    print("Botão de desconectar foi clicado. Iniciando o logout...")

    # Limpa as informações do usuário logado
    set_logged_user_id(None)

    page.go('/login')
    print("Reiniciando a página e navegando para a tela de login...")
