import flet as ft

index = 0

def generator_colors():
    global index
    colors = {
        1: ft.colors.BROWN,
        2: ft.colors.BROWN_600,
        3: ft.colors.BROWN_300,
        4: ft.colors.PINK_100,
        5: ft.colors.AMBER_300,
    }
    while True:
        yield colors.get(index % 5 + 1, ft.colors.GREY)
        index += 1

color_gen = generator_colors()

def create_color_button():
    color = next(color_gen)
    button = ft.ElevatedButton(
        width=20,
        bgcolor=color,
        height=20,
        style=ft.ButtonStyle(
            shape=ft.ContinuousRectangleBorder()
        )
    )
    return button

character_height = ft.Slider(
    min=10,
    max=200,
    divisions=190,
    label='{value}cm',
    round=0,
    thumb_color=ft.colors.GREY_700,
    active_color=ft.colors.RED_900,
    inactive_color=ft.colors.WHITE, 
)

character_shape = ft.Dropdown(
    label='Selecione uma opção',
    options=[
        ft.dropdown.Option(key=1, text='Muito Magro', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key=2, text='Magro', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key=3, text='Normal', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key=4, text='Forte', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key=5, text='Musculoso', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key=6, text='Obeso', text_style=ft.TextStyle(font_family='Pixeled'))
    ],
    label_style=ft.TextStyle(font_family='Medieval', weight=ft.FontWeight.W_900, size=25, color=ft.colors.BLACK),
    bgcolor=ft.colors.GREY_700,
    focused_color=ft.colors.BLACK,
    border_color=ft.colors.BLACK
)

confirm_button = ft.ElevatedButton(
    content=ft.Text(
        "Aplicar",
        size=20,
        font_family='Pixeled',
        color=ft.colors.GREY_700
    ),
    style=ft.ButtonStyle(
        padding=20,
        shape=ft.RoundedRectangleBorder(radius=0),
        bgcolor=ft.colors.GREY_500
    ),
    width=200
)

attributes_menu_content = ft.Column(
    col=9,
    controls=[
        ft.Text(
            value='Características Físicas',
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
                        value='Defina a altura do seu personagem',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    character_height
                ],
            ),
            width=500
        ),
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Tipo de porte físico',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    character_shape
                ]
            ),
            width=500
        ),
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Cor da pele',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    ft.Row(
                        controls=[
                            create_color_button() for _ in range(5)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            ),
            width=500
        ),
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Cor do cabelo',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    ft.Row(
                        controls=[
                            create_color_button() for _ in range(5)
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
