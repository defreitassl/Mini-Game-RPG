import flet as ft
from app.interface.login import LoginPage
from app.interface.create_account import CreateAccountPage
from app.interface.create_characther import CreateCharacterPage
from app.interface.home_page import HomePage


def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0
    page.title = 'Kingdoms'
    page.fonts = {
        'Medieval': 'fonts/Medieval.ttf',
        'Pixeled': 'fonts/Pixeled.ttf'
    }

    login_view = ft.View(route='/login', controls=[LoginPage(page)], padding=0)
    create_account_view = ft.View(route='/create-account', controls=[CreateAccountPage(page)], padding=0)
    create_character_view = ft.View(route='/create-character', controls=[CreateCharacterPage(page)], padding=0)
    home_page_view = ft.View(route='/home-page', controls=[HomePage(page)], padding=0)

    def route_change(route):
        page.views.clear()
        page.views.append(login_view)

        if page.route == '/create-account':
            page.views.append(create_account_view)
        
        if page.route == '/create-character':
            page.views.append(create_character_view)

        if page.route == '/home-page':
            page.views.append(home_page_view)
        
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir='./assets')