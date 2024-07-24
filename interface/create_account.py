import flet as ft

def CreateAccount(page: ft.Page):

    page.add(
        ft.Text(value="Hello World"),
        ft.Container(
            height=700,
            width=500,
            bgcolor='blue'
        )
    )


if __name__=='__main__':
    ft.app(target=CreateAccount)