import flet as ft

def main(page: ft.Page):
    page.title = "Controles"

    def botao_clicado(e):
        page.add(ft.Text(int(3+5)))

    button = ft.ElevatedButton(
        text="clique em mim",
        on_click=botao_clicado
        )

    page.add(
        button
    )
ft.app(target=main)