import flet as ft
from .create_character_views.identity_menu import identity_menu_content
from .create_character_views.skills_menu import skills_menu_content
from .create_character_views.attributes_menu import attributes_menu_content
from .create_character_views.profile_menu import profile_menu_content


def CreateCharacterPage(page):


    def change_view(e):
        new_view = e.control.selected_index
        
        responsive_row.controls.pop()
        
        if new_view == 0:
            responsive_row.controls.append(identity_menu_content)
        elif new_view == 1:
            responsive_row.controls.append(skills_menu_content)
        elif new_view == 2:
            responsive_row.controls.append(attributes_menu_content)
        elif new_view == 3:
            responsive_row.controls.append(profile_menu_content(page))

        page.update()

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
        bgcolor=ft.colors.BLACK54,
        indicator_color=ft.colors.RED_900,
        selected_index=0,
        indicator_shape=ft.ContinuousRectangleBorder(),
        expand=True,
        on_change= change_view,
    )

    responsive_row = ft.ResponsiveRow(
        controls=[
            side_bar,
            identity_menu_content,
        ],
        columns=10,
        height=700
    )

    menu = ft.Container(
        content=ft.Column(
            controls=[responsive_row],
            scroll=ft.ScrollMode.AUTO
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
        image_src='images/backgroundCharacter.webp',  
        image_fit=ft.ImageFit.COVER,
    )
    page.update()

    return window
