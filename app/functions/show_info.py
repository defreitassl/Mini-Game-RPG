import flet as ft
from ..current_user import get_logged_user_id
from ..database.characters_operations import collect_character_info
from ..database.users_operations import get_user_picture_from_db

def show_user_info(main_content: ft.Container):
    
    column_in_container = main_content.content
    column_controls = column_in_container.controls

    user_id = get_logged_user_id()
    character_info = collect_character_info(user_id)
    picture_src = get_user_picture_from_db()

    if character_info:
        category, age, gender, strength, agility, health, stamina, intelligence, height, body_shape, skin_color, hair_color, biography = character_info

        column_content = [
            ft.CircleAvatar(
                background_image_src=picture_src,
                radius=50,
            ),
            ft.Text(f'Classe: {category}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Idade: {age}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Gênero: {gender}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Força: {strength}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Agilidade: {agility}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Vida: {health}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Estamina: {stamina}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Inteligência: {intelligence}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Altura: {height}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Porte Físico: {body_shape}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Cor da Pele: {skin_color}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Cor do Cabelo: {hair_color}', font_family='Pixeled', color=ft.colors.GREY_700),
            ft.Text(f'Biografia: {biography}', font_family='Pixeled', color=ft.colors.GREY_700),
        ]

        column_controls[1] = ft.Container(
            content=ft.Column(
                controls=column_content
            )
        )
        column_controls[2] = ft.Text('')

        column_in_container.controls = column_controls
        
        main_content.update()

    else:
        print("\n Não foi possível obter as informações do personagem. \n")
