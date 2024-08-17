import flet as ft


def HomePage(page):
    
    menu = ft.Container()
    
    window = ft.Container(
        content= menu,
        alignment=ft.alignment.center,
        expand=True,
        image_src='images/backgroundHome.webp',  
        image_fit=ft.ImageFit.COVER,
    )
    page.update()

    return window