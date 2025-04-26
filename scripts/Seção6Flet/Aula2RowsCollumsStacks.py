import flet as ft

"""
O padrão do flet é organizar nossos controles em colunas, utilizando o metodo ft.row, e adicionando os elementos
que queremos por em linha no control=, nós organizamos esses itens em linhas ao inves de colunas e vice versa.

"""
def main(page: ft.Page):
    page.title="Falando sobre containers"
    page.padding=0
    page.window.height=400
    page.window.width=400

    c1 = ft.Container(
        content=ft.ElevatedButton("Buton 1"),
        bgcolor=ft.colors.YELLOW,
        padding=50,
    )
    c2 = ft.Container(
        content=ft.ElevatedButton("Buton 2"),
        bgcolor=ft.colors.YELLOW,
        padding=50,
    )
    c3 = ft.Container(
        content=ft.ElevatedButton("Buton 3"),
        bgcolor=ft.colors.YELLOW,
        padding=50,
    )

    # lista de controles
    items = [c1,c2,c3]

    # Criando row
    row = ft.Row(spacing=10, controls=items)

    # Criando coluna
    collum = ft.Column(spacing=10, controls=items)


    page.update()

    page.add(
        row,
        collum,
    )



ft.app(port=8550,target=main)