import flet as ft
from time import sleep
from ...functions.collect_character_info import collect_character_info
from .identity_menu import identity_confirm_button, character_class, character_age, feminine_check
from .skills_menu import skills_confirm_button, forca, agilidade, energia, vida, inteligencia
from .attributes_menu import attributes_confirm_button, character_shape, character_height, get_skin_color, get_hair_color
from ..home_page import HomePage

# Função para coletar todas as informações do personagem e enviá-las para o banco de dados
def collect_all_info(page):
    
    # Verifica se a biografia possui mais de 50 caracteres e se uma foto de perfil foi selecionada
    if len(character_bio.value) > 50 and selected_picture_src is not None:
        # Verifica se todos os campos foram confirmados
        if all([identity_confirm_button.disabled, skills_confirm_button.disabled, attributes_confirm_button.disabled]):
            # Define o gênero do personagem com base na seleção do usuário
            gender = 'Feminino' if feminine_check.value else 'Masculino'

            # Coleta a cor da pele e do cabelo
            skin_color = get_skin_color()
            hair_color = get_hair_color()
            
            # Chama a função para coletar e salvar as informações no banco de dados
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

            # Redireciona para a página principal
            page.go('/home-page')

        else:
            print("Por favor, preencha todos os campos antes de criar o personagem.")
    else:
        # Exibe uma mensagem de erro se a biografia for muito curta ou se não houver foto de perfil selecionada
        print("A biografia deve conter no mínimo 50 caracteres e uma foto de perfil deve ser selecionada.")
        character_bio.error_text = "A biografia deve conter no mínimo 50 caracteres"
        character_bio.update()
        sleep(3)  # Pausa por 3 segundos para mostrar a mensagem de erro
        character_bio.error_text = ""
        character_bio.update()

# Função para contar os caracteres da biografia em tempo real
def count_characters(e):
    num_characters = len(e.control.value)
    e.control.counter_text = num_characters
    e.control.update()

# Variável global para armazenar o caminho da foto de perfil selecionada
selected_picture_src = None

# Função para selecionar a foto de perfil do personagem
def select_picture(e):
    global selected_picture_src
    selected_picture_src = e.control.data

# Gerador de avatares para seleção
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

# Campo de texto para a biografia do personagem
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
    error_style=ft.TextStyle(color=ft.colors.WHITE54),

    multiline=True,
    min_lines=3,
    max_lines=5,

    on_change=count_characters  # Atualiza o contador de caracteres em tempo real
)

# Gera os avatares para a seleção
picture_gen = create_profile_avatars()

# Função para gerar o conteúdo do menu de perfil, incluindo seleção de avatar e biografia
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
        on_click=lambda _: collect_all_info(page)  # Chama a função para coletar todas as informações ao clicar
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
                            controls=[next(picture_gen) for _ in range(6)],  # Gera os botões de seleção de avatar
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
                        character_bio  # Campo de texto para inserir a biografia
                    ]
                ),
                width=500
            ),
            ft.Container(
                content=create_button  # Botão para criar o personagem
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50,
    )
