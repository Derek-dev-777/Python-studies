import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Ícones do Flet"

    # Criando um Container com altura fixa e rolagem
    lista_icones = ft.Column(scroll="always", expand=True, height=500)

    # Pegando todos os ícones disponíveis no Flet
    icones = [attr for attr in dir(ft.icons) if attr.isupper()]

    # Criando uma lista visual com os ícones e seus nomes
    for icone in icones:
        lista_icones.controls.append(
            ft.Row(
                [
                    ft.Icon(getattr(ft.icons, icone), size=30),
                    ft.Text(icone),
                ],
                alignment=ft.MainAxisAlignment.START
            )
        )

    # Adicionando a lista dentro de um Container para melhor organização
    container_lista = ft.Container(lista_icones, expand=True, padding=10)

    # Adicionando à página
    page.add(container_lista)
    page.update()

ft.app(target=main, view=ft.AppView.FLET_APP)  # Rodando no app Desktop