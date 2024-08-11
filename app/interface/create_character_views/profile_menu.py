import flet as ft
from ...functions.collect_character_info import collect_character_info


def collect_all_info():
    ...
    #Continuar com as importações gerais para passar os dados para a funçao collect_character_info e criar o objeto personagem


def count_characters(e):
    num_characters = len(e.control.value)
    e.control.counter_text = num_characters
    e.control.update()


index = 0
def create_profile_avatars():
    global index

    while True:
        index += 1
        picture = ft.CircleAvatar(
        background_image_src=f'images/avatar{index}.webp',
            radius=35
        )
        button = ft.ElevatedButton(
            content=picture,
            style=ft.ButtonStyle(
                padding=0,
                shape=ft.RoundedRectangleBorder(radius=35),
            ),
        )
        yield button


character_bio = ft.TextField(
    bgcolor=ft.colors.GREY_400,

    hint_text='Faça a história do seu personagem. Conte um pouco sobre ele para auxiliar na gameplay.',
    hint_style=ft.TextStyle(font_family='Medieval'),

    max_length=300,
    helper_text='Max 300 caracteres',
    helper_style=ft.TextStyle(font_family='Pixeled'),

    counter_text='',
    counter_style=ft.TextStyle(font_family='Pixeled'),
    text_style=ft.TextStyle(font_family='Pixeled'),

    multiline=True,
    min_lines=3,
    max_lines=5,

    on_change= count_characters
)

picture_gen = create_profile_avatars()

create_button = ft.ElevatedButton(
    content=ft.Text(
        "CRIAR PERSONAGEM",
        size=20,
        font_family='Pixeled',
        color=ft.colors.GREY_700
    ),
    style=ft.ButtonStyle(
        padding=20,
        shape=ft.RoundedRectangleBorder(radius=0),
        bgcolor=ft.colors.AMBER_700
    ),
    width=400,
    on_click=collect_all_info()
)

profile_menu_content = ft.Column(
    col=9,
    controls=[
        ft.Text(
            value='Quem é você?..',
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
                        value='Escolha uma foto de perfil',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    ft.Row(
                        controls = [
                            next(picture_gen) for _ in range(6)
                        ],
                    )
                ],
            ),
            width=500
        ),
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Biografia...',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    character_bio
                ]
            ),
            width=500
        ),
        ft.Container(
            content=create_button
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=50,
)