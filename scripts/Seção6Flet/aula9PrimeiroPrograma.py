import flet as ft

def main(page:ft.Page):
    page.title = "Projeto"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = 650
    page.window.width = 400
    page.padding = ft.padding.only(top=10, right=10, left=10, bottom=10)

    def adicionar(e):
        
            page.add(ft.Checkbox(label= nova_tarefa.value))
            nova_tarefa.value = ""
            nova_tarefa.focus()
            nova_tarefa.update()


    nova_tarefa = ft.TextField(hint_text="O que precisa ser feito", width=300)
    button = ft.ElevatedButton("Adicionar", on_click=adicionar)

    coluna = ft.Column(
          controls=[
                ft.Row(
                      controls=[
                            nova_tarefa,
                            button,
                      ]
                )
          ]
    )
      


    page.add(
        coluna
    )
ft.app(target=main)