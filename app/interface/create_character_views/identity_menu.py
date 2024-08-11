import flet as ft


def apply_attributes(e):
    if character_class.value and character_age.value and (masculine_check.value or feminine_check.value):
        character_class.disabled = True
        character_age.disabled = True
        masculine_check.disabled = True
        feminine_check.disabled = True
        e.control.disabled = True  # Desabilita o botão que foi clicado
        
        character_class.update()
        character_age.update()
        masculine_check.update()
        feminine_check.update()
        e.control.content.color = ft.colors.GREY_900
        e.control.bgcolor = ft.colors.GREY_600
        e.control.update()

    else:
        print('\n Preencha todas as informações antes de confirmar \n')


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
        size=20,
        color=ft.colors.GREY_700
    ),
    active_color=ft.colors.RED_900,
    check_color=ft.colors.BLACK,
    disabled=False
)

masculine_check = ft.Checkbox(
    on_change=checkbox_masculine_change,
    label='Masculino',
    label_position=ft.LabelPosition.RIGHT,
    label_style=ft.TextStyle(
        font_family='Medieval',
        weight=ft.FontWeight.W_900,
        size=20,
        color=ft.colors.GREY_700
    ),
    active_color=ft.colors.RED_900,
    check_color=ft.colors.BLACK,
    disabled=False
)

character_class = ft.Dropdown(
    label='Selecione uma opção',
    options=[
        ft.dropdown.Option(key='Arqueiro', text='Arqueiro', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Clérigo', text='Clérigo', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Curandeiro', text='Curandeiro', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Ladrão', text='Ladrão', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Guerreiro', text='Guerreiro', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Mago', text='Mago', text_style=ft.TextStyle(font_family='Pixeled'))
    ],
    label_style=ft.TextStyle(font_family='Medieval', weight=ft.FontWeight.W_900, size=25, color=ft.colors.BLACK),
    bgcolor=ft.colors.GREY_700,
    focused_color=ft.colors.BLACK,
    border_color=ft.colors.BLACK,
    disabled=False
)


character_age = ft.Slider(
    min=10,
    max=150,
    divisions=140,
    label='{value} anos',
    round=0,
    thumb_color=ft.colors.GREY_700,
    active_color=ft.colors.RED_900,
    inactive_color=ft.colors.WHITE,
    disabled=False
)

confirm_button = ft.ElevatedButton(
    content=ft.Text(
        "Aplicar",
        size=20,
        font_family='Pixeled',
        color=ft.colors.WHITE
    ),
    style=ft.ButtonStyle(
        padding=20,
        shape=ft.RoundedRectangleBorder(radius=0),
        bgcolor=ft.colors.RED_900
    ),
    width=200,
    on_click= lambda e: apply_attributes(e)
)

identity_menu_content = ft.Column(
    col=9,
    controls=[
        ft.Text(
            value='Característcas não visuais',
            font_family='Medieval',
            theme_style=ft.TextThemeStyle.DISPLAY_SMALL,
            weight=ft.FontWeight.W_900,
            style=ft.TextStyle(
                color=ft.colors.GREY_700
            ),
        ),
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Escolha uma classe para seu personagem...',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
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
                        color=ft.colors.GREY_700
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
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
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
            content=confirm_button
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=50,
)