import flet as ft

def LoginPage(page: ft.Page):

    page.window_min_height = 900
    page.window_min_width = 700
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.all(0)
    page.fonts = {
        'Medieval': 'fonts/Medieval.ttf',
        'Pixeled': 'fonts/Pixeled.ttf'
    }


    login_box = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    value="Bem vindo de volta ao Kingdoms...",
                    font_family='Medieval',
                    no_wrap=True,
                    theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                    style=ft.TextStyle(
                        color=ft.colors.BLACK
                    )
                ),
                ft.TextField(
                    text_style=ft.TextStyle(font_family='Pixeled', size=10),
                    hint_text='archer_123',
                    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
                    prefix=ft.Text(value='@'),
                    label='Seu nome de usuário..',
                    label_style=ft.TextStyle(font_family='Pixeled', size=10),
                    icon=ft.icons.PERSON,
                ),
                ft.TextField(
                    text_style=ft.TextStyle(font_family='Pixeled', size=10),
                    hint_text='Ex:14Archer_##',
                    hint_style=ft.TextStyle(font_family='Pixeled', size=10),
                    label='Sua senha..',
                    label_style=ft.TextStyle(font_family='Pixeled', size=10),
                    icon=ft.icons.PASSWORD,
                    password=True,
                    can_reveal_password=True,
                ),
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
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
                                    width=250
                                ),
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
                                    on_click=page.go('/create-account')
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=80
        ),
        shadow=ft.BoxShadow(
            color=ft.colors.RED_900,
            blur_radius=700,
            spread_radius=10,
            blur_style=ft.ShadowBlurStyle.NORMAL
        ),
        height=700,
        width=500,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(16)
    )

    window = ft.Container( 
        content=login_box,
        alignment=ft.alignment.center,
        expand=True,
        image_src='images/background.webp',  
        image_fit=ft.ImageFit.COVER,   
    )

    page.add(window)

if __name__=='__main__':
    ft.app(target=LoginPage, assets_dir='../assets')