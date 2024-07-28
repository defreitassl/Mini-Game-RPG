import flet as ft


def CreateCharacterAppBar():
    return ft.AppBar(
        center_title=True, 
        title=ft.Text(
            value='Crie seu personagem',
            font_family='Medieval',
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
            weight=ft.FontWeight.W_900,
            color=ft.colors.BLACK
        ),
    )
#Continuar criando o appBar


def CreateCharacterPage(page):

    def checkbox_feminine_change(e):
        if feminine_check.value:
            masculine_check.value = False
            masculine_check.update()
    
    def checkbox_masculine_change(e):
        if masculine_check.value:
            feminine_check.value = False
            feminine_check.update()

    feminine_check = ft.Checkbox(
        on_change=checkbox_feminine_change,
        label='Feminino',
        label_position=ft.LabelPosition.RIGHT,
        label_style=ft.TextStyle(
            font_family='Medieval',
            weight=ft.FontWeight.W_900,
            size=20
        )
    )

    masculine_check = ft.Checkbox(
        on_change=checkbox_masculine_change,
        label='Masculino',
        label_position=ft.LabelPosition.RIGHT,
        label_style=ft.TextStyle(
            font_family='Medieval',
            weight=ft.FontWeight.W_900,
            size=20
        )
    )

    character_class = ft.Dropdown(
        label='Selecione uma opção',
        options=[
            ft.dropdown.Option(key=1, text='Arqueiro', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=2, text='Clérigo', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=3, text='Curandeiro', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=4, text='Ladrão', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=5, text='Guerreiro', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=6, text='Mago', text_style=ft.TextStyle(font_family='Pixeled'))
        ],
        label_style=ft.TextStyle(font_family='Medieval', weight=ft.FontWeight.W_900, size=25),
        bgcolor=ft.colors.GREY_700
    )


    character_age = ft.Slider(
        min=10,
        max=150,
        divisions=140,
        label='{value} anos',
        round=0
    )

    menu_content = ft.Column(
        col=9,
        controls=[
            ft.Text(
                value='Característcas não visuais',
                font_family='Medieval',
                theme_style=ft.TextThemeStyle.DISPLAY_SMALL,
                weight=ft.FontWeight.W_900,
                style=ft.TextStyle(
                    color=ft.colors.BLACK
                ),
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Escolha uma classe para seu personagem...',
                            font_family='Pixeled'
                        ),
                        character_class
                    ],
                ),
                width=500
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Defina a idade do personagem...',
                            font_family='Pixeled',
                        ),
                        character_age
                    ]
                ),
                width=500
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Defina o sexo do personagem...',
                            font_family='Pixeled'
                        ),
                        ft.Row(
                            controls=[
                                masculine_check,
                                feminine_check,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                ),
                width=500
            ),
            ft.Container(
                content=ft.ElevatedButton(
                    content=ft.Text(
                        "Aplicar",
                        size=20,
                        font_family='Pixeled',
                        color=ft.colors.BLACK
                    ),
                    style=ft.ButtonStyle(
                        padding=20,
                        shape=ft.RoundedRectangleBorder(radius=0),
                        bgcolor=ft.colors.GREY_500
                    ),
                    width=200
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50,
    )

    side_bar = ft.NavigationRail(
        col=1,
    )

    menu = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                side_bar,
                menu_content,
            ],
            columns=10,
            expand=True
        ),
        bgcolor=ft.colors.AMBER_800,
        height=700,
        width=1000,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(16),
    )

    window = ft.Container(
        content= menu,
        alignment=ft.alignment.center,
        expand=True,
        image_src='images/backgroundCharacter.webp',  
        image_fit=ft.ImageFit.COVER,
    )

    return window

if __name__=='__main__':
    ft.app(target=CreateCharacterPage)