import flet as ft
from ..current_user import get_logged_user_id
from ..database.characters_operations import collect_character_info
from ..database.users_operations import get_user_picture_from_db

#Função que busca todas as infos do personagem para que ele possa vizualiza-las melhor
def show_user_info(main_content: ft.Container):
    """
    Exibe as informações do personagem do usuário logado na interface.

    Args:
        main_content (ft.Container): O container principal que contém o conteúdo atual da página.

    Returns:
        None
    """
    
    column_in_container = main_content.content    #Seleciona a coluna interna do container principal
    column_controls = column_in_container.controls    #Seleciona o conteúdo da coluna

    user_id = get_logged_user_id() #Busca o ID do usuário logado atualmente
    character_info = collect_character_info(user_id) #Busca todas as infos do personagem e as retorna em uma tupla
    picture_src = get_user_picture_from_db() #Seleciona o caminho da imagem de perfil do personagem

    #Executa o código caso as informações sejam extraídas com sucesso
    if character_info:
        #Desempacota a tupla com as infos do personagem
        category, age, gender, strength, agility, health, stamina, intelligence, height, body_shape, skin_color, hair_color, biography = character_info

        #Cria o novo conteúdo da coluna para exibir as infos do personagem
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
        #Redefine o conteúdo da coluna para column_content
        column_controls[1] = ft.Container(
            content=ft.Column(
                controls=column_content
            )
        )
        column_controls[2] = ft.Text('')   #Coloca um texto invisível na coluna para ocupar espaço


        column_in_container.controls = column_controls 
        
        main_content.update() #Atualiza a página para mostrar o novo conteúdo

    else:
        #Mensagem de erro caso as informações não sejam extraídas com sucesso
        print("\n Não foi possível obter as informações do personagem. \n")
