import flet as ft
from ..functions.collect_account_info import collect_account_info


name = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='PrimeiroNome ÚltimoNome',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    label='Insira seu nome e sobrenome..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.PERSON,
    error_style=ft.TextStyle(color='black'),
    helper_text= 'apenas nome e último nome / apenas letras permitidas'
)

username = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='archer_123',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    prefix=ft.Text(value='@'),
    label='Insira seu nome de usuário..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.ALTERNATE_EMAIL_ROUNDED,
    error_style=ft.TextStyle(color='black'),
    helper_text= 'mínimo de 4 caracteres / proibido espaços'
)

password = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='Ex:14Archer_##',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    label='Insira sua senha..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.PASSWORD,
    password=True,
    can_reveal_password=True,
    error_style=ft.TextStyle(color='black'),
    helper_text= 'mínimo 8 caracteres'
)

password_confirmation = ft.TextField(
    text_style=ft.TextStyle(font_family='Pixeled', size=10),
    hint_text='Ex:14Archer_##',
    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
    label='Confirme sua senha..',
    label_style=ft.TextStyle(font_family='Pixeled', size=10),
    icon=ft.icons.PASSWORD,
    password=True,
    can_reveal_password=True,
    error_style=ft.TextStyle(color='black')
)


def CreateAccountPage(page):

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
        on_click= lambda _: collect_account_info(page, name=name, username=username, password=password, conf_password=password_confirmation),
        width=250
    )

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
            name,
            username,
            password,
            password_confirmation,
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        controls=[
                            create_account_button,
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
                                on_click=lambda _: page.go('/login')
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
        scroll=ft.ScrollMode.AUTO
    )

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
        image_src='images/backgroundLogin.webp',  
        image_fit=ft.ImageFit.COVER,   
    )

    return window