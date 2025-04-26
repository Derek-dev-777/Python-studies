import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Supermercado"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = 650
    page.window.width = 700
    page.padding = ft.padding.only(top=10, right=10, left=10, bottom=10)

    tasks = []  # Lista que vai armazenar os itens
    prices = []  # Lista que vai armazenar os preços

    def add_task(e):
        if new_task.value != "":  # Verifica se o campo não está vazio
            tasks.append(new_task.value)  # Adiciona a tarefa à lista
            update_task_list()  # Atualiza a exibição da lista
            new_task.value = ""  # Limpa o campo de texto
            page.update()

    def update_task_list():
        task_list.controls.clear()  # Limpa a lista de itens na interface
        for task in tasks:  # Para cada item na lista de tarefas
            task_list.controls.append(ft.Checkbox(label=task))  # Adiciona o item à interface
        page.update()

    def add_price(e):
        if new_price.value != "":  # Verifica se o campo de preço não está vazio
            prices.append(new_price.value)  # Adiciona o preço à lista
            update_prices_list()  # Atualiza a exibição da lista
            new_price.value = ""  # Limpa o campo de texto
            page.update()

    def update_prices_list():
        price_list.controls.clear()  # Limpa a lista de preços na interface
        for preco in prices:  # Para cada item na lista de preços
            price_list.controls.append(ft.Text(f"R${preco}"))  # Exibe o preço
        page.update()

    def somar_prices(e):
        total_price = 0

        for preco in prices:
            try:
                total_price += float(preco)
            except ValueError:
                continue

        total.value = f"Preço total: R$ {total_price:.2f}" 
        page.update()



    # Campos de entrada
    new_task = ft.TextField(label="Insira um item", hint_text="Exemplo: Arroz, Feijão")
    new_price = ft.TextField(label="Adicione o valor", hint_text="Exemplo: 12.30")
    
    # Botões para adicionar
    add_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)
    add_price_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_price)
    somar = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=somar_prices)

    # Listas para exibir tarefas e preços
    task_list = ft.ListView(
        controls=[],  # Inicia a lista vazia
        spacing=10,
        auto_scroll=True
    )

    price_list = ft.ListView(
        controls=[],  # Inicia a lista vazia
        spacing=10,
        auto_scroll=True
    )

    total = ft.Text(
    "Preço total: R$ 0.00",  # Exemplo de valor
    bgcolor=ft.colors.GREEN_600,  # Cor de fundo
    color=ft.colors.WHITE,  # Cor do texto
    size=24,  # Tamanho da fonte
    weight=ft.FontWeight.BOLD,  # Negrito  
    
    )

    # Layout
    layout = ft.Column(
        controls=[
            # Linhas para entrada de task e preço
            ft.Row(
                controls=[new_task, add_button]
            ),
            ft.Row(
                controls=[new_price, add_price_button]
            ),
            # Linhas para as listas de tarefas e preços, uma ao lado da outra
            ft.Row(
                controls=[
                    ft.Column(controls=[task_list], expand=True),  # Coluna para tarefas
                    ft.Column(controls=[price_list], expand=True)  # Coluna para preços
                ],
                expand=True  # Isso garante que o layout ocupe todo o espaço disponível
            ),
            ft.Row(controls=[total, somar], expand=True)
        ]
    )

    page.add(layout)
    page.update()

ft.app(target=main)