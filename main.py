import flet as ft
#Importa as funções que retornam as páginas à serem utilizadas 
from app.interface.login import LoginPage
from app.interface.create_account import CreateAccountPage
from app.interface.create_characther import CreateCharacterPage
from app.interface.home_page import HomePage

#Função que administra a troca entre páginas com rotas URL
def route_change(page):

    #Cria as Views que incluem as páginas
    login_view = ft.View(route='/login', controls=[LoginPage(page)], padding=0)
    create_account_view = ft.View(route='/create-account', controls=[CreateAccountPage(page)], padding=0)
    create_character_view = ft.View(route='/create-character', controls=[CreateCharacterPage(page)], padding=0)
    home_page_view = ft.View(route='/home-page', controls=[HomePage(page)], padding=0)

    #Limpa a lista de views para adicionar outra
    page.views.clear()
    #Adiciona a página de Login para ser mostrada primeiro
    page.views.append(login_view)

    #Condições para cada rota a ser direcionada
    if page.route == '/login':
        page.views.clear()
        print("Navegando para a tela de login...")
        page.views.append(login_view)

    elif page.route == '/create-account':
        page.views.clear()
        print("Navegando para a tela de criação de conta...")
        page.views.append(create_account_view)

    elif page.route == '/create-character':
        page.views.clear()
        print("Navegando para a tela de criação de personagem...")
        page.views.append(create_character_view)

    elif page.route == '/home-page':
        page.views.clear()
        print("Navegando para a home page...")
        page.views.append(home_page_view)

    else:
        print(f"Rota desconhecida: {page.route}")

    # Atualize a página após mudar as views
    page.update()
    print("Página atualizada.")

#Função principal onde tudo se inicia
def main(page: ft.Page):

    #Configurações da página padrão
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0
    page.title = 'Kingdoms'
    #Define as fontes padrões da página
    page.fonts = {
        'Medieval': 'fonts/Medieval.ttf',
        'Pixeled': 'fonts/Pixeled.ttf'
    }

    #Chama a função route_change a cada vez que a rota for mudada pelo usuário
    page.on_route_change = lambda _: route_change(page)
    print("Função de mudança de rota configurada.")
    route_change(page)

#Define a função principal e o diretório de assets
ft.app(target=main, assets_dir='./assets')

