import flet as ft
from app.interface.login import LoginPage
from app.interface.create_account import CreateAccountPage
from app.interface.create_characther import CreateCharacterPage
from app.interface.home_page import HomePage

def route_change(page):


    #Adicionar funcao para limpar inputs de create-account



    login_view = ft.View(route='/login', controls=[LoginPage(page)], padding=0)
    create_account_view = ft.View(route='/create-account', controls=[CreateAccountPage(page)], padding=0)
    create_character_view = ft.View(route='/create-character', controls=[CreateCharacterPage(page)], padding=0)
    home_page_view = ft.View(route='/home-page', controls=[HomePage(page)], padding=0)

    page.views.clear()
    page.views.append(login_view)

    if page.route == '/login':
        page.views.clear()
        print("Navegando para a tela de login...")
        page.views.append(login_view)

    elif page.route == '/create-account':
        page.views.clear()
        print("Navegando para a tela de criação de conta...")
        page.views.append(create_account_view)

    elif page.route == '/create-character':
        page.views.clear()
        print("Navegando para a tela de criação de personagem...")
        page.views.append(create_character_view)

    elif page.route == '/home-page':
        page.views.clear()
        print("Navegando para a home page...")
        page.views.append(home_page_view)

    else:
        print(f"Rota desconhecida: {page.route}")

    # Atualize a página após mudar as views
    page.update()
    print("Página atualizada.")

def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0
    page.title = 'Kingdoms'
    page.fonts = {
        'Medieval': 'fonts/Medieval.ttf',
        'Pixeled': 'fonts/Pixeled.ttf'
    }

    page.on_route_change = lambda _: route_change(page)
    print("Função de mudança de rota configurada.")
    route_change(page)

ft.app(target=main, assets_dir='./assets')

