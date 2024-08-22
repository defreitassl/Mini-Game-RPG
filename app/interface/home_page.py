import flet as ft

def HomePage(page, picture_src=None):

    def close_banner(e):
        page.banner.open = False 
        page.update()

    def open_banner(e):
        page.banner = bn1 
        bn1.open=True 
        page.update()

    bn1 = ft.Banner(
        content=ft.Text(value="Esta função está temporariamente indisponível"), 

        actions=[
            ft.TextButton(text="Cancelar", style=ft.ButtonStyle(color=ft.colors.RED), on_click=close_banner),
        ],
        content_padding=ft.padding.all(25),
        leading=ft.Icon(name=ft.icons.WARNING_AMBER), 
        force_actions_below=True, 
        bgcolor=ft.colors.AMBER_100
    )

    menu_button = ft.IconButton(
        icon=ft.icons.MENU_OUTLINED,
        icon_color=ft.colors.WHITE54,
        height=100,
        icon_size=70,
        col=1
    )

    # O valor de picture_src será recebido como parâmetro
    picture = ft.CircleAvatar(
        background_image_src=picture_src,  # Atualiza a imagem do avatar com o caminho da imagem passada
        radius=35,
        expand=True
    )

    account_button = ft.ElevatedButton(
        content=picture,
        style=ft.ButtonStyle(
            padding=0,
            shape=ft.CircleBorder(),
        ),
        col=1
    )

    nav_bar = ft.ResponsiveRow(
        controls=[
            ft.Container(
                col=5,
                content=ft.Text(
                    "Kingdoms",
                    font_family='Medieval',
                    color=ft.colors.WHITE54,
                    size=100,
                    weight=ft.FontWeight.W_900,
                )
            ),
            ft.Container(col=3),
            menu_button,
            account_button
        ],
        columns=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    game_mode_img = ft.Row(
        height=400,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                image_src='images/game_mode.webp',
                image_fit=ft.ImageFit.CONTAIN,
                width=400,
                height=300
            )
        ]
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
                on_click= open_banner
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
                on_click= open_banner
            ),
        ]
    )
    
    menu = ft.Container(
        content=ft.Column(
            controls=[
                nav_bar,
                game_mode_img,
                buttons,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        bgcolor=ft.colors.BLACK54,
        expand=True,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            color=ft.colors.BLACK,
            blur_radius=800,
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
