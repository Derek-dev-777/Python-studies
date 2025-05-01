import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE24
    page.title = "Clima Tempo"
    page.window.width = 350
    page.window.height = 730

    
    # container principal, onde os outros containers serão adicionados
    cnt_principal = ft.Container(

        bgcolor=ft.colors.DEEP_ORANGE,
        border_radius=35,
        padding = 10,
        width= page.window.width * 0.90,
        height= page.window.height * 0.90,
        content=ft.Column(
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            height=page.window.height * 0.90,
            width=page.window.width * 0.90,


        )
    )
    #---------------------------------------------------------------------------------
    # Container superior:

    cnt_superior = ft.Container(
        #bgcolor= ft.colors.WHITE,
        height = 100,
        width = cnt_principal.width * 0.95,
        content= ft.Row(

        )
    )

    pesquisa_local = ft.TextField(
        bgcolor=ft.colors.GREY_100,
        border_color=ft.colors.WHITE,
        border_radius=10,
        width=cnt_superior.width * 0.80,
        hint_text="Informe a cidade e o pais ",
        hint_style=ft.TextStyle(
            size=12,
            color=ft.colors.BLUE_GREY,
            ),
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(
            size=14,
            color=ft.colors.BLACK,
            ),
        value=" São Paulo, SP",
        )
    
    botao_pesquisa = ft.IconButton(
        icon= ft.icons.SEARCH,
        icon_color=ft.colors.BLACK,
    )

    cnt_superior.content.controls.append(pesquisa_local)
    cnt_superior.content.controls.append(botao_pesquisa)

    #---------------------------------------------------------------------------------
    # Container central:

    cnt_central = ft.Container(
        bgcolor= ft.colors.GREY_100,
        height = 200,
        width= cnt_principal.width * 0.95,
        content= ft.Column(

        )
    )

    cnt_central_linha1 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="cidade",
                font_family="Segaon Medium",
                color=ft.colors.BLACK,
                size=38,
                weight=ft.FontWeight.BOLD,
            )
        ]
    )
    cnt_central_linha2 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Image(
                src="https://cdn-icons-png.flaticon.com/512/5538/5538361.png",
                width=50,
                height=50,
            )
        ]
    )
    cnt_central_linha3 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="17°",
                font_family="Segaon Medium",
                color=ft.colors.BLACK,
                size=28,
                
            )
        ]
    )
    cnt_central_linhar4 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="75%",
                font_family="Segaon Medium",
                color=ft.colors.BLACK,
                
                
            )
        ]
    )

    cnt_central.content.controls.append(cnt_central_linha1)
    cnt_central.content.controls.append(cnt_central_linha2)
    cnt_central.content.controls.append(cnt_central_linha3)
    cnt_central.content.controls.append(cnt_central_linhar4)
    #---------------------------------------------------------------------------------
    # Container inferior:
    
    cnt_inferior = ft.Container(
        bgcolor= ft.colors.GREY_100,
        height = 150,
        content= ft.Column(

        )
    )

    cnt_inferior_linha1 = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.Text(
                f"D{i}",
                color=ft.colors.BLACK,
                
            ) for i in range(1,6) # função de repetição, faz com que ele repita o texto 5 vezes substituindo o I.
            
        ],
    )

    cnt_inferior_linha2 = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.Image(
                src="https://cdn-icons-png.flaticon.com/512/5538/5538361.png",
                width=50,
                height=50,
            ) for i in range(1,6)
        ]
    )

    cnt_inferior_linha3 = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.Text(
                f"T{i}",
                color=ft.colors.BLACK,
                
            ) for i in range(1,6) # função de repetição, faz com que ele repita o texto 5 vezes substituindo o I.
            
        ],
    )

    cnt_inferior.content.controls.append(cnt_inferior_linha1)
    cnt_inferior.content.controls.append(cnt_inferior_linha2)
    cnt_inferior.content.controls.append(cnt_inferior_linha3)
    #---------------------------------------------------------------------------------

    # Adicionando os containers dentro do container principal
    cnt_principal.content.controls.append(cnt_superior)
    cnt_principal.content.controls.append(cnt_central)
    cnt_principal.content.controls.append(cnt_inferior)

    page.add(
        cnt_principal,
        )

ft.app(port=8550, target=main, view=ft.AppView.FLET_APP)