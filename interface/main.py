import flet as ft
from login import LoginPage
from create_account import CreateAccountPage

def main(page: ft.Page):

    page.window_min_height = 900
    page.window_min_width = 700
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.all(0)
    page.fonts = {
        'Medieval': 'fonts/Medieval.ttf',
        'Pixeled': 'fonts/Pixeled.ttf'
    }
    
    login_view = ft.View(route='/login', controls=[LoginPage(page)])
    create_account_view = ft.View(route='/create-account', controls=[CreateAccountPage(page)])


    def route_change(route):
        page.views.clear()
        page.views.append(login_view)

        if page.route == '/create-account':
            page.views.append(create_account_view)
        
        page.update()

    page.on_route_change = route_change
    page.go(page.route)
    



ft.app(target=main, assets_dir='../assets')