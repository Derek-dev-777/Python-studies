import flet as ft

def main(page: ft.Page):
    page.title = "Projeto2"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = 650
    page.window.width = 700
    page.padding = ft.padding.only(top=10, right=10, left=10, bottom=10)

    # Lista de tarefas e seus preços
    tasks = []
    total_price = 0
    removed_tasks = []

    def add_task(e):
        nonlocal total_price  # Para modificar a variável total_price dentro da função

        
        if new_task.value and price_field.value and quantas_unidades:
            try:
                price = float(price_field.value)  # Convertendo o preço para float
                vezes = float(quantas_unidades.value)

                tasks.append(
                    ft.Row(
                        controls=[
                            ft.Checkbox(label=new_task.value),
                            ft.Text(f"R$ {price:.2f}", size=18),
                            ft.Text(f"{vezes}X", size=18),  # Mostrando o preço formatado
                        ]
                    )
                )

                preco_final = price * vezes
                total_price += preco_final  # Adicionando o preço ao total

                # Atualizando os controles
                task_list.controls = tasks
                total_label.value = f"Total: R$ {total_price:.2f}"  # Atualizando o total na tela
                new_task.value = ""  # Limpando o campo de tarefa
                price_field.value = ""  # Limpando o campo de preço
                page.update()

            except ValueError:
                # Caso o preço não seja um número válido
                error_label.value = "Digite um preço válido!"
                page.update()

    def remove_item():
        ...
        

    new_task = ft.TextField(label="Insira um produto", hint_text="Exemplo: Arroz, Feijão")
    price_field = ft.TextField(label="Preço", hint_text="Preço (R$)")
    quantas_unidades = ft.TextField(label="Unidades", hint_text="Coloque a quantidade")

    button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    # Criação do ListView com scroll e altura flexível
    task_list = ft.ListView(
        controls=tasks,  # A lista de tarefas a ser exibida
        spacing=10,       # Espaçamento entre os itens
        auto_scroll=True,  # Para o scroll automático quando necessário
        expand=True  # Garantir que o ListView ocupe o espaço disponível
    )

    # Rótulo para mostrar o total
    total_label = ft.Text(f"Total: R$ {total_price:.2f}", size=20, color=ft.colors.GREEN)
    
    # Rótulo para mostrar mensagens de erro
    error_label = ft.Text("", size=16, color=ft.colors.RED)

    layout = ft.Column(
        controls=[
            ft.Row(
                controls=[new_task]
            ),
            ft.Row(
                controls=[price_field]
            ),
            ft.Row(
                controls=[quantas_unidades]
            ),
            ft.Row(
                controls=[button]
            ),
            task_list,  # Exibe a lista de tarefas
            total_label,  # Mostrar o total
            error_label   # Mostrar mensagens de erro
        ],
        expand=True  # Isso ajuda a ocupar o restante do espaço disponível na página
    )

    page.add(layout)
    page.update()

ft.app(target=main)