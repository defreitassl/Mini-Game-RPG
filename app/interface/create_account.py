import flet as ft
from ..functions.collect_account_info import collect_account_info

# Função para limpar os inputs de nome, nome de usuário, senha e confirmação de senha
def clean_inputs(name_input, username_input, password_input, conf_password_input):
    # Reseta os valores dos campos de entrada
    name_input.value = ""
    username_input.value = ""
    password_input.value = ""
    conf_password_input.value = ""

    # Remove mensagens de erro
    name_input.error_text = None
    username_input.error_text = None
    password_input.error_text = None
    conf_password_input.error_text = None

    # Atualiza os campos de texto na interface
    name_input.update()
    username_input.update()
    password_input.update()
    conf_password_input.update()

# Campo de texto para o nome completo do usuário com configurações de estilo e placeholders
name = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='PrimeiroNome ÚltimoNome',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    label='Insira seu nome e sobrenome..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.PERSON,
    error_style=ft.TextStyle(color='black'),
    helper_text='apenas nome e último nome / apenas letras permitidas'
)

# Campo de texto para o nome de usuário com configurações de estilo e placeholders
username = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='archer_123',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    prefix=ft.Text(value='@'),
    label='Insira seu nome de usuário..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.ALTERNATE_EMAIL_ROUNDED,
    error_style=ft.TextStyle(color='black'),
    helper_text='mínimo de 4 caracteres / proibido espaços'
)

# Campo de texto para a senha com configurações de estilo e placeholders
password = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='Ex:14Archer_##',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    label='Insira sua senha..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.PASSWORD,
    password=True,  # Oculta a senha por padrão
    can_reveal_password=True,  # Permite revelar a senha
    error_style=ft.TextStyle(color='black'),
    helper_text='mínimo 8 caracteres'
)

# Campo de texto para a confirmação da senha com as mesmas configurações do campo de senha
password_confirmation = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='Ex:14Archer_##',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    label='Confirme sua senha..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.PASSWORD,
    password=True,  # Oculta a senha por padrão
    can_reveal_password=True,  # Permite revelar a senha
    error_style=ft.TextStyle(color='black')
)

# Função que retorna a página de criação de conta
def CreateAccountPage(page):

    # Botão para criar a conta que chama a função de coleta de informações ao ser clicado
    create_account_button = ft.ElevatedButton(
        content=ft.Text(
            "Criar Conta..",
            size=16,
            font_family='Pixeled',
            color=ft.colors.BLACK,
        ),
        style=ft.ButtonStyle(
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=0),
            bgcolor=ft.colors.RED_800
        ),
        on_click=lambda _: collect_account_info(page, name=name, username=username, password=password, conf_password=password_confirmation),
        width=250
    )

    # Componentes da página de criação de conta organizados em uma coluna
    components = ft.Column(
        controls=[
            ft.Text(
                value="Bem vindo ao Kingdoms...",
                font_family='Medieval',
                theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                style=ft.TextStyle(
                    color=ft.colors.BLACK
                )
            ),
            name,  # Campo de texto para o nome
            username,  # Campo de texto para o nome de usuário
            password,  # Campo de texto para a senha
            password_confirmation,  # Campo de texto para a confirmação de senha
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        controls=[
                            create_account_button,  # Botão para criar a conta
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row( 
                        spacing=0,
                        controls=[ 
                            ft.Text(
                                value='Já possui uma conta?',
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
                                # Redireciona para a página de login e limpa os inputs ao ser clicado
                                on_click=lambda _: (page.go('/login'), clean_inputs(name, username, password, password_confirmation))
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50,
        scroll=ft.ScrollMode.AUTO  # Permite rolagem na coluna, caso necessário
    )

    # Container principal que envolve os componentes da página
    window = ft.Container(
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

    return window  # Retorna a página de criação de conta completa
