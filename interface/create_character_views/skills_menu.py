import flet as ft

points_left = 100

# Dicionário para armazenar as referências aos campos de texto das habilidades
stat_fields = {}

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
    stat_fields[stat_name] = field
    return field

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
                                ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click, icon_color='white', data='forca'),
                                create_stat_number(stat_name='forca'),
                                ft.IconButton(icon=ft.icons.ADD, on_click=plus_click, icon_color='white', data='forca'),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
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
                                ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click, icon_color='white', data='agilidade'),
                                create_stat_number(stat_name='agilidade'),
                                ft.IconButton(icon=ft.icons.ADD, on_click=plus_click, icon_color='white', data='agilidade'),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
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
                                ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click, icon_color='white', data='vida'),
                                create_stat_number(stat_name='vida'),
                                ft.IconButton(icon=ft.icons.ADD, on_click=plus_click, icon_color='white', data='vida'),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
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
                                ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click, icon_color='white', data='energia'),
                                create_stat_number(stat_name='energia'),
                                ft.IconButton(icon=ft.icons.ADD, on_click=plus_click, icon_color='white', data='energia'),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
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
                                ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click, icon_color='white', data='inteligencia'),
                                create_stat_number(stat_name='inteligencia'),
                                ft.IconButton(icon=ft.icons.ADD, on_click=plus_click, icon_color='white', data='inteligencia'),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center
                    )
                ],
            ),
            width=500
        ),
        ft.Container(
            content=confirm_button
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=20,
)