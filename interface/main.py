import flet as ft
from login import LoginPage
from create_account import CreateAccount


def main(page: ft.Page):

    page.views.append(
        ft.View(route="/", controls=[LoginPage(page)])
    )

    def route_change(route):
        page.views.clear()

        if page.route == '/create-account':
            page.views.append(
                ft.View(route="/create-account", controls=[CreateAccount(page)])
            )
        
        page.update()

    
    
    page.title = 'Kingdoms'
    page.on_route_change = route_change
    page.go(page.route)



if __name__=='__main__':
    ft.app(target=main)