import flet as ft
from .create_character_views.identity_menu import identity_menu_content
from .create_character_views.skills_menu import skills_menu_content
from .create_character_views.attributes_menu import attributes_menu_content
from .create_character_views.profile_menu import profile_menu_content

# Função que cria a página de criação de personagem
def CreateCharacterPage(page):

    # Função para trocar a visualização com base na aba selecionada na barra de navegação lateral
    def change_view(e):
        new_view = e.control.selected_index  # Obtém o índice da aba selecionada
        
        responsive_row.controls.pop()  # Remove o conteúdo atual do menu de personagem
        
        # Adiciona o conteúdo correspondente à aba selecionada
        if new_view == 0:
            responsive_row.controls.append(identity_menu_content)
        elif new_view == 1:
            responsive_row.controls.append(skills_menu_content)
        elif new_view == 2:
            responsive_row.controls.append(attributes_menu_content)
        elif new_view == 3:
            responsive_row.controls.append(profile_menu_content(page))

        page.update()  # Atualiza a página para refletir as mudanças

    # Barra de navegação lateral com as diferentes seções da criação de personagem
    side_bar = ft.NavigationRail(
        col=1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.PERSON_2,
                label_content=ft.Text(value='Identidade', font_family='Medieval', color='white'),
                padding=ft.padding.only(top=70)
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ALIGN_VERTICAL_BOTTOM_SHARP,
                label_content=ft.Text(value='Habilidades', font_family='Medieval', color='white'),
                padding=ft.padding.only(top=70)
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_ACCESSIBILITY_SHARP,
                label_content=ft.Text(value='Características', font_family='Medieval', color='white'),
                padding=ft.padding.only(top=70)
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PERM_IDENTITY,
                label_content=ft.Text(value='Perfil', font_family='Medieval', color='white'),
                padding=ft.padding.only(top=70)
            )
        ],
        bgcolor=ft.colors.BLACK54,  # Cor de fundo da barra de navegação
        indicator_color=ft.colors.RED_900,  # Cor do indicador de aba selecionada
        selected_index=0,  # Aba selecionada por padrão
        indicator_shape=ft.ContinuousRectangleBorder(),  # Forma do indicador
        expand=True,
        on_change=change_view,  # Função chamada ao mudar a aba
    )

    # Linha responsiva que organiza a barra de navegação e o conteúdo do menu
    responsive_row = ft.ResponsiveRow(
        controls=[
            side_bar,
            identity_menu_content,  # Conteúdo da aba selecionada inicialmente
        ],
        columns=10,
        height=700  # Altura da linha responsiva
    )

    # Container que envolve a linha responsiva e permite rolagem 
    menu = ft.Container(
        content=ft.Column(
            controls=[responsive_row],
            scroll=ft.ScrollMode.AUTO  # Habilita rolagem
        ),
        bgcolor=ft.colors.BLACK54,  # Cor de fundo do container
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

    # Container principal que envolve todo o menu de criação de personagem
    window = ft.Container(
        content=menu,
        alignment=ft.alignment.center,
        expand=True,
        image_src='images/backgroundCharacter.webp',  # Imagem de fundo do container
        image_fit=ft.ImageFit.COVER,  # Ajusta a imagem de fundo para cobrir todo o container
    )
    
    page.update()  # Atualiza a página para refletir as mudanças

    return window  # Retorna a página de criação de personagem completa
