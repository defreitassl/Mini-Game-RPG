import flet as ft

# Variável global para controlar os pontos restantes
points_left = 100

# Dicionário para armazenar as referências aos campos de texto das habilidades
stat_fields = {}

# Dicionário para armazenar as referências aos botões de adicionar e remover
button_fields = {}


def minus_click(e):
    global points_left
    stat_name = e.control.data
    if points_left < 100 and int(stat_fields[stat_name].value) > 0:
        stat_fields[stat_name].value = str(int(stat_fields[stat_name].value) - 1)
        points_left += 1
        points.value = f'PONTOS {points_left}'
        e.page.update()


def plus_click(e):
    global points_left
    stat_name = e.control.data
    if points_left > 0:
        stat_fields[stat_name].value = str(int(stat_fields[stat_name].value) + 1)
        points_left -= 1
        points.value = f'PONTOS {points_left}'
        e.page.update()


def create_stat_number(stat_name):
    # Cria um campo de texto desabilitado para exibir a pontuação de uma habilidade
    field = ft.TextField(
        value='0',
        text_style=ft.TextStyle(font_family='Pixeled'),
        text_align=ft.TextAlign.CENTER,
        width=100,
        disabled=True,
        color='white',
        border_color='white',
        data=stat_name
    )
    stat_fields[stat_name] = field  # Armazena a referência do campo de texto
    return field


def create_stat_buttons(stat_name):
    # Cria os botões de adicionar e remover e armazena suas referências
    minus_button = ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click, icon_color='white', data=stat_name)
    plus_button = ft.IconButton(icon=ft.icons.ADD, on_click=plus_click, icon_color='white', data=stat_name)
    
    button_fields[f'minus_{stat_name}'] = minus_button
    button_fields[f'plus_{stat_name}'] = plus_button
    
    return minus_button, plus_button


def apply_attributes(e):
    global points_left
    
    # Verifica se todos os 100 pontos foram distribuídos
    if points_left == 0:
        # Desativa os botões de adicionar e remover para todas as habilidades
        for stat_name in stat_fields:
            minus_button = button_fields[f'minus_{stat_name}']
            plus_button = button_fields[f'plus_{stat_name}']
            
            minus_button.disabled = True
            plus_button.disabled = True
            
            # Atualiza os botões na interface
            minus_button.update()
            plus_button.update()
        
        # Desativa o botão de confirmação
        skills_confirm_button.disabled = True
        skills_confirm_button.content.color = ft.colors.GREY_900
        skills_confirm_button.bgcolor = ft.colors.GREY_600
        skills_confirm_button.update()
        
        print("Todos os pontos foram distribuídos e a edição foi bloqueada.")
    
    else:
        print(f"Ainda restam {points_left} pontos para distribuir.")

# Botão de confirmação
skills_confirm_button = ft.ElevatedButton(
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

# Estrutura da página de habilidades e distribuição de pontos
skills_menu_content = ft.Column(
    col=9,
    controls=[
        ft.Text(
            value='Habilidades e Skills',
            font_family='Medieval',
            theme_style=ft.TextThemeStyle.DISPLAY_SMALL,
            weight=ft.FontWeight.W_900,
            color=ft.colors.GREY_700
        ),
        points := ft.Text(
            value=f'PONTOS {points_left}',
            font_family='Medieval',
            theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            weight=ft.FontWeight.W_900,
            color=ft.colors.GREY_700
        ),
        
        # Seção para a habilidade Força
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Força',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                *create_stat_buttons(stat_name='forca'),  # Botões de menos e mais
                                forca := create_stat_number(stat_name='forca'),   # Campo de texto desabilitado
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
        
        # Seção para a habilidade Agilidade
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Agilidade',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                *create_stat_buttons(stat_name='agilidade'),  # Botões de menos e mais
                                agilidade := create_stat_number(stat_name='agilidade'),   # Campo de texto desabilitado
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
        
        # Seção para a habilidade Vida
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Vida',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                *create_stat_buttons(stat_name='vida'),  # Botões de menos e mais
                                vida := create_stat_number(stat_name='vida'),   # Campo de texto desabilitado
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
        
        # Seção para a habilidade Energia
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Energia',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                *create_stat_buttons(stat_name='energia'),  # Botões de menos e mais
                                energia := create_stat_number(stat_name='energia'),   # Campo de texto desabilitado
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
        
        # Seção para a habilidade Inteligência
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value='Inteligência',
                        font_family='Pixeled',
                        color=ft.colors.GREY_700
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                *create_stat_buttons(stat_name='inteligencia'),  # Botões de menos e mais
                                inteligencia := create_stat_number(stat_name='inteligencia'),   # Campo de texto desabilitado
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
        
        # Botão de confirmação
        ft.Container(
            content=skills_confirm_button
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=20,
)
