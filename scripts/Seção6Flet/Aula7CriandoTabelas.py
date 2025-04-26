import flet as ft

def main(page:ft.Page):

    page.title = "Table"

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Primeiro Nome")),
            ft.DataColumn(ft.Text("Ultimo Nome")),
            ft.DataColumn(ft.Text("Idade")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("joão")),
                    ft.DataCell(ft.Text("Muanda")),
                    ft.DataCell(ft.Text(15)),   
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Derek")),
                    ft.DataCell(ft.Text("Meneghel")),
                    ft.DataCell(ft.Text(15)),   
                ],
            )
        ]
    )

    page.add(
        tabela,
    )
ft.app(target=main)