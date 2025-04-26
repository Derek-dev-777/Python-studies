
"""
    ListView = é o controle de rolagem mais usado, ele exibe seus filhos um após o outro na direção da rolagem
acaba sendo muito eficaz para listas enormes

    GridView = Parecido com o list view, ele irá mostrar os elementos num formato como no pinterest, é dificil
explicar escrevendo.. mas pode vir a ser util em breve ( calculadora )
"""

import flet as ft

def main(page: ft.Page):
    page.title="Falando sobre containers"
    page.padding=0
    page.window.height=1000
    page.window.width=1000

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

    # Criando uma ListView
    lv = ft.ListView(auto_scroll=True, expand=1, padding=20, spacing=10)
    lv.controls.append(ft.Text("Ola derek menegas"))
    lv.controls.append(collum)

    # Criando uma GridView

    gv = ft.GridView(
        expand=1, runs_count=5, max_extent=150, spacing=5, run_spacing=5, child_aspect_ratio=1.0
    )
    gv.controls.append(row)
    page.update()

    page.add(
        lv,
        gv,
        
    )

ft.app(port=8550,target=main)