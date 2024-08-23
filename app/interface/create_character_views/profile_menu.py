import flet as ft
from ...functions.collect_character_info import collect_character_info
from .identity_menu import identity_confirm_button, character_class, character_age, feminine_check
from .skills_menu import skills_confirm_button, forca, agilidade, energia, vida, inteligencia
from .attributes_menu import attributes_confirm_button, character_shape, character_height, get_skin_color, get_hair_color
from ..home_page import HomePage

def collect_all_info(page):
    
    if len(character_bio.value) > 50 and selected_picture_src is not None:
        if all([identity_confirm_button.disabled, skills_confirm_button.disabled, attributes_confirm_button.disabled]):
            gender = 'Feminino' if feminine_check.value else 'Masculino'

            skin_color = get_skin_color()
            hair_color = get_hair_color()
            
            # Chama a função de coleta com todos os atributos
            collect_character_info(
                category=character_class.value, 
                age=character_age.value, 
                gender=gender,
                strength=forca.value, 
                agility=agilidade.value, 
                health=vida.value,
                stamina=energia.value, 
                intelligence=inteligencia.value, 
                body_shape=character_shape.value,
                height=character_height.value, 
                skin_color=skin_color, 
                hair_color=hair_color,
                biography=character_bio.value, 
                picture_src=selected_picture_src
            )

            page.views.clear()
            page.views.append(ft.View(route='/home-page', controls=[HomePage(page, picture_src=selected_picture_src)]))
            page.update()

        else:
            print("Por favor, preencha todos os campos antes de criar o personagem.")
    else:
        print("A biografia deve conter no mínimo 50 caracteres e uma foto de perfil deve ser selecionada.")

def count_characters(e):
    num_characters = len(e.control.value)
    e.control.counter_text = num_characters
    e.control.update()


selected_picture_src = None
def select_picture(e):
    global selected_picture_src
    selected_picture_src = e.control.data


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
            data=f'images/avatar{index}.webp',
            on_click=lambda e: select_picture(e)
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

    on_change=count_characters
)

picture_gen = create_profile_avatars()

def profile_menu_content(page):

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
        on_click=lambda _: collect_all_info(page)  # Passa o page aqui
    )

    return ft.Column(
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
                            controls=[next(picture_gen) for _ in range(6)],
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
