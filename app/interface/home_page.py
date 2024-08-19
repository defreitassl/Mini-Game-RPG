import flet as ft


def HomePage(page):

    game_mode_img = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                image_src='images/game_mode.webp',
                image_fit=ft.ImageFit.COVER
            )
        ],
    )

    buttons = ft.Column(
        controls=[
            ft.ElevatedButton(
                content=ft.Text(
                    "JOGAR",
                    size=20,
                    font_family='Pixeled',
                    color=ft.colors.GREY_700
                ),
                style=ft.ButtonStyle(
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=0),
                    bgcolor=ft.colors.GREEN_500
                ),
                width=300,
            ),
            ft.ElevatedButton(
                content=ft.Text(
                    "RANKING",
                    size=20,
                    font_family='Pixeled',
                    color=ft.colors.GREY_700
                ),
                style=ft.ButtonStyle(
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=0),
                    bgcolor=ft.colors.AMBER_700
                ),
                width=300,
            ),
        ]
    )
    
    menu = ft.Container(
        content=ft.Column(
            controls=[
                #nav_bar,
                game_mode_img,
                buttons,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        ),
        bgcolor=ft.colors.BLACK54,
        height=700,
        width=1000,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(16),
        shadow=ft.BoxShadow(
            color=ft.colors.BLACK,
            blur_radius=600,
            blur_style=ft.ShadowBlurStyle.NORMAL
        )
    )
    
    window = ft.Container(
        content= menu,
        alignment=ft.alignment.center,
        expand=True,
        image_src='images/backgroundHome.webp',  
        image_fit=ft.ImageFit.COVER,
    )
    page.update()

    return window

#Adicionar funcao pra trocar de página ao apertar botao de criar personagem