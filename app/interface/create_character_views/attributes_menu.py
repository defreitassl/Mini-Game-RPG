import flet as ft

index = 0

# Dicionários para rastrear se uma cor de pele ou cabelo foi selecionada
skin_color_selection = {}
hair_color_selection = {}

# Dicionários para associar cada botão ao nome da cor correspondente
skin_color_names = {}
hair_color_names = {}

# Variáveis para armazenar a cor escolhida
selected_skin_color = None
selected_hair_color = None


def get_skin_color():
    return selected_skin_color


def get_hair_color():
    return selected_hair_color


# Função chamada quando um botão de cor é clicado
def select_color(e):
    global selected_skin_color, selected_hair_color


    # Verifica qual tipo de cor está sendo selecionado
    if e.control in skin_color_buttons:
        skin_color_selection[e.control] = True
        selected_skin_color = skin_color_names[e.control]
    elif e.control in hair_color_buttons:
        hair_color_selection[e.control] = True
        selected_hair_color = hair_color_names[e.control]

    e.page.update()


def apply_attributes(e):
    # Verifica se todos os campos foram preenchidos
    if (character_height.value is not None and
        character_shape.value is not None and
        selected_skin_color is not None and
        selected_hair_color is not None):

        # Desativa todos os inputs para impedir edição futura
        character_height.disabled = True
        character_height.update()
        
        character_shape.disabled = True
        character_shape.update()

        for button in skin_color_buttons:
            button.disabled = True
            button.update()

        for button in hair_color_buttons:
            button.disabled = True
            button.update()

        attributes_confirm_button.disabled = True
        attributes_confirm_button.content.color = ft.colors.GREY_900
        attributes_confirm_button.bgcolor = ft.colors.GREY_600
        attributes_confirm_button.update()

    else:
        print("\n Preencha todos os atributos antes de confirmar. \n")


def generator_colors():
    global index
    colors = {
        1: ('Marrom', ft.colors.BROWN),
        2: ('Pardo', ft.colors.BROWN_600),
        3: ('Bronzeado', ft.colors.BROWN_300),
        4: ('Rosado', ft.colors.PINK_100),
        5: ('Amarelo', ft.colors.AMBER_300),
    }
    while True:
        yield colors.get(index % 5 + 1, ('Indefinido', ft.colors.GREY))
        index += 1

color_gen = generator_colors()


def create_color_button(color_type):
    name, color = next(color_gen)
    button = ft.ElevatedButton(
        width=20,
        bgcolor=color,
        height=20,
        style=ft.ButtonStyle(
            shape=ft.ContinuousRectangleBorder()
        ),
        on_click=select_color  # Atribui a função de seleção de cor ao clicar
    )
    
    # Associa o botão ao nome da cor
    if color_type == 'skin':
        skin_color_names[button] = name
    elif color_type == 'hair':
        hair_color_names[button] = name

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
        ft.dropdown.Option(key='Muito Magro', text='Muito Magro', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Magro', text='Magro', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Normal', text='Normal', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Forte', text='Forte', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Musculoso', text='Musculoso', text_style=ft.TextStyle(font_family='Pixeled')),
        ft.dropdown.Option(key='Obeso', text='Obeso', text_style=ft.TextStyle(font_family='Pixeled'))
    ],
    label_style=ft.TextStyle(font_family='Medieval', weight=ft.FontWeight.W_900, size=25, color=ft.colors.BLACK),
    bgcolor=ft.colors.GREY_700,
    focused_color=ft.colors.BLACK,
    border_color=ft.colors.BLACK
)

attributes_confirm_button = ft.ElevatedButton(
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
    on_click=apply_attributes  # Associa a função ao clique
)

# Criação dos botões de cor da pele e do cabelo
skin_color_buttons = [create_color_button('skin') for _ in range(5)]
hair_color_buttons = [create_color_button('hair') for _ in range(5)]

# Inicializa os dicionários de seleção como False
for button in skin_color_buttons:
    skin_color_selection[button] = False

for button in hair_color_buttons:
    hair_color_selection[button] = False

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
                        controls=skin_color_buttons,
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
                        controls=hair_color_buttons,
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            ),
            width=500
        ),
        ft.Container(
            content=attributes_confirm_button
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=50,
)
