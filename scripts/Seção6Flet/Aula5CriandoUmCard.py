import flet as ft

def main(page: ft.Page):
    page.title="Criando um card"
    page.bgcolor=ft.colors.BLACK

    texto = ft.Text("Ola")


    card = ft.Card(
        content= ft.Container(

            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("Filho da noite"),
                        subtitle=ft.Text("Musica de matue")
                    ),
                    ft.Row(
                        [
                            ft.TextButton("Comprar ingressos"),
                            ft.TextButton("Ouvir"),

                        ],
                        alignment= ft.MainAxisAlignment
                        
                    )
                ],
            
            ),
        width=400,
        padding=10
        ),
    )

    page.add(
        card,
    )





ft.app(target=main)