import flet as ft
from ..functions.verify_login_info import verify_login_info

# Função para limpar os inputs de username e password, resetando seus valores e mensagens de erro
def clean_inputs(username_input, password_input):
    username_input.value = ''
    password_input.value = ''
    username_input.error_text = None
    password_input.error_text = None
    
    # Atualiza os campos de texto na interface
    username_input.update()
    password_input.update()

# Campo de texto para o nome de usuário com configurações de estilo e placeholders
username = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='archer_123',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    prefix=ft.Text(value='@'),
    label='Seu nome de usuário..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.PERSON,
    error_style=ft.TextStyle(color=ft.colors.BLACK)
)

# Campo de texto para a senha com configurações de estilo e placeholders
password = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='Ex:14Archer_##',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    label='Sua senha..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.PASSWORD,
    password=True,
    can_reveal_password=True,  # Permite que a senha seja revelada
    error_style=ft.TextStyle(color=ft.colors.BLACK)
)

# Função que retorna a página de login
def LoginPage(page):

    # Botão de login que chama a função de verificação de login ao ser clicado
    login_button = ft.ElevatedButton(
        content=ft.Text(
            "Entrar..",
            size=20,
            font_family='Pixeled',
            color=ft.colors.BLACK
        ),
        style=ft.ButtonStyle(
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=0),
            bgcolor=ft.colors.RED_800
        ),
        width=250,
        on_click=lambda _: verify_login_info(page, username, password)  # Chama a função de verificação de login
    )

    # Componentes da página de login organizados em uma coluna
    components = ft.Column(
        controls=[
            ft.Text(
                value="Bem vindo de volta ao Kingdoms...",
                font_family='Medieval',
                theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                style=ft.TextStyle(
                    color=ft.colors.BLACK
                )
            ),
            username,  # Campo de texto do username
            password,  # Campo de texto da senha
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        controls=[
                            login_button,  # Botão de login
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row( 
                        spacing=0,
                        controls=[ 
                            ft.Text(
                                value='Ainda não tem uma conta?',
                                theme_style=ft.TextThemeStyle.BODY_LARGE,
                                style=ft.TextStyle(
                                    color=ft.colors.BLACK,
                                    font_family='Medieval',
                                )
                            ),
                            ft.TextButton(
                                content=ft.Text(
                                    value="Clique Aqui!",
                                    font_family='Medieval',
                                    size=20
                                ),
                                # Redireciona para a página de criação de conta e limpa os inputs ao ser clicado
                                on_click= lambda _: (page.go('/create-account'), clean_inputs(username, password))
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=80,
        scroll=ft.ScrollMode.AUTO  # Permite rolagem na coluna, caso necessário
    )

    # Container interno que contém todos os componentes da página
    inner_container = ft.Container( 
        content=ft.Container(
            content=components,
            shadow=ft.BoxShadow(
                color=ft.colors.RED_900,
                blur_radius=700,
                spread_radius=10,
                blur_style=ft.ShadowBlurStyle.NORMAL
            ),
            height=700,
            width=500,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
        ),
        alignment=ft.alignment.center,
        expand=True,
        image_src='images/backgroundLogin.webp',  # Imagem de fundo da página
        image_fit=ft.ImageFit.COVER,  # Ajusta a imagem de fundo para cobrir todo o container  
    )
    
    # Container principal que expande para preencher a tela
    window = ft.Container(
        content= inner_container,
        expand=True,
    )

    return window  # Retorna a página de login completa
