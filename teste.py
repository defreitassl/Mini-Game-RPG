import flet as ft

def main(page: ft.Page):

    character_class = ft.Dropdown(
        label='Selecione uma opção',
        options=[
            ft.dropdown.Option(key=1, text='Arqueiro', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=2, text='Clérigo', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=3, text='Curandeiro', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=4, text='Ladrão', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key=5, text='Guerreiro', text_style=ft.TextStyle(font_family='Pixeled')),
            ft.dropdown.Option(key='Mago', text='Mago', text_style=ft.TextStyle(font_family='Pixeled'))
        ],
        label_style=ft.TextStyle(font_family='Medieval', weight=ft.FontWeight.W_900, size=25, color=ft.colors.BLACK),
        bgcolor=ft.colors.GREY_700,
        focused_color=ft.colors.BLACK,
        border_color=ft.colors.BLACK,
        on_change= lambda e: print(e.control.value)
    )

    page.add(character_class)

ft.app(target=main)