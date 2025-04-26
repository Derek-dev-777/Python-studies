import flet as ft
"""
    ResponsiveRow cabe 12 colunas, podemos dividir elas em quanto quisermos, mas esse é seu limite
"""
def main(page: ft.Page):
    res = ft.ResponsiveRow(
            ft.Column(col={"sm":6}, controls=[ft.Text("Coluna 1")]),
            ft.Column(col={"sm":6}, controls=[ft.Text("Coluna 2")]),
    )

    pw = ft.Text(bottom=50, right=50, style="displaysmall")
    page.overlay.append(pw)
    






    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text("Coluna1"),
                    padding=5,
                    bgcolor=ft.colors.YELLOW,
                    col={"sm":6, "md":4, "x1":2},
                ),
            ]
        )
    )


ft.app(target=main)