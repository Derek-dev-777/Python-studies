import flet as ft

"""
    Criando containers com flet, containers servem para organizar a estrutura do seu codigo, você pode alterar
a propriedade dos mesmos como weight, padding, height, cores, e adicionar um conteudo dentro deles assim como
no exemplo abaixo.
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

    page.update()

    page.add(
        c1,
        c2,
        c3
    )



ft.app(port=8550,target=main)