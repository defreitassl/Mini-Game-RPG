import flet as ft
from ..functions.user_log_out import log_out
from ..functions.show_info import show_user_info

# Variáveis globais para armazenar o conteúdo original e rastrear se as informações do personagem estão sendo exibidas
original_content = None
info_displayed = False  

# Função que define a página principal do aplicativo
def HomePage(page):
    global original_content, info_displayed  

    # Função para fechar o banner de aviso
    def close_banner(e):
        page.banner.open = False 
        page.update()

    # Função para abrir o banner de aviso
    def open_banner(e):
        page.banner = bn1 
        bn1.open=True 
        page.update()

    # Definição do banner de aviso que será exibido temporariamente
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

    # Botão para desconectar/log out do sistema
    menu_button = ft.IconButton(
        icon=ft.icons.EXIT_TO_APP_ROUNDED,
        icon_color=ft.colors.WHITE54,
        height=100,
        icon_size=70,
        col=1,
        tooltip='Sair/Desconectar',
        on_click=lambda e: log_out(page)  # Chama a função de logout ao clicar
    )

    # Botão para visualizar as informações do perfil do usuário
    account_button = ft.IconButton(
        icon=ft.icons.PERSON,
        icon_color=ft.colors.WHITE54,
        height=100,
        icon_size=70,
        col=1,
        tooltip='Visualizar Perfil',
        on_click=lambda _: toggle_info(menu)  # Alterna entre mostrar/esconder informações do perfil
    )

    # Barra de navegação contendo o título do jogo e os botões de logout e perfil
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
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    # Imagem representando o modo de jogo
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

    # Coluna de botões para "JOGAR" e "RANKING"
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
                on_click= open_banner  # Exibe o banner de aviso ao clicar
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
                on_click= open_banner  # Exibe o banner de aviso ao clicar
            ),
        ]
    )
    
    # Menu principal contendo a barra de navegação, a imagem do modo de jogo e os botões
    menu = ft.Container(
        content=ft.Column(
            controls=[
                nav_bar,
                game_mode_img,
                buttons,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll=ft.ScrollMode.AUTO
        ),
        bgcolor=ft.colors.BLACK54,
        expand=True,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            color=ft.colors.BLACK,
            blur_radius=800,
            blur_style=ft.ShadowBlurStyle.NORMAL
        ),
        padding=30
    )
    
    # Contêiner que encapsula todo o conteúdo da página, incluindo o fundo de tela
    window = ft.Container(
        content=menu,
        alignment=ft.alignment.center,
        expand=True,
        image_src='images/backgroundHome.webp',  
        image_fit=ft.ImageFit.COVER,
    )

    page.update()  # Atualiza a página

    return window  # Retorna a janela principal

# Função que alterna entre exibir as informações do usuário ou o conteúdo original da página
def toggle_info(main_content: ft.Container):
    global original_content, info_displayed

    column_in_container = main_content.content

    if info_displayed:
        # Retorna o conteúdo original da página
        column_in_container.controls = original_content
        info_displayed = False

    else:
        # Salva o conteúdo atual e exibe as informações do usuário
        original_content = column_in_container.controls.copy()
        show_user_info(main_content)
        info_displayed = True

    main_content.update()  # Atualiza o conteúdo da página
