import flet as ft
import os


def main(page: ft.Page):

    # Funções

    def calcular(e):
        if peso.value == "" or altura.value == "" or genero.value == "":
            banner.open = True
            page.update()
        else:
            try:
                # Convertendo os valores para float
                valor_peso = float(peso.value)
                valor_altura = float(altura.value)

                # Calculando o IMC
                imc_resultado = valor_peso / (valor_altura * valor_altura)
                imc_resultado = float(f"{imc_resultado:.2f}")

                # Exibindo o resultado
                IMC.value = f"Seu IMC é {imc_resultado:.2f}"
                page.update()

            except ValueError:  
                banner_value_error.open = True
                page.update()

        if genero.value == "Feminino":
            resultado = imc_feminino(imc_resultado)
            detalhes.value = f"{resultado}"
            icone_padrao.icon = ft.icons.WOMAN_2 
            page.update()  

        elif genero.value == "Masculino":
            resultado = imc_masculino(imc_resultado)
            detalhes.value = f"{resultado}"
            icone_padrao = ft.Icon(ft.icons.MAN_2, size=100)
            icone_padrao.update()  
            page.update()  

        
        peso.value = ""
        altura.value = ""
        genero.value = ""
        page.update()

    def imc_feminino(imc):
        if imc <= 19.1:
            return f"Abaixo do peso"
        elif imc >= 19.1 and imc <= 25.8:
            return f"Normal"
        elif imc >= 25.9 and imc <= 27.3:
            return f"Pouco Acima do peso"
        elif imc >= 27.4 and imc <= 32.3:
            return f"Acima do peso"
        elif imc >= 32.4:
            return f"Obesidade"

    def imc_masculino(imc):
        if imc <= 19:
            return f"Abaixo do peso"
        elif imc >= 19.1 and imc <= 24.9:
            return f"Normal"
        elif imc >= 25 and imc <= 29.9:
            return f"Pouco Acima do peso"
        elif imc >= 30 and imc <= 39.9:
            return f"Acima do peso"
        elif imc >= 40:
            return f"Obesidade mórbida"

    def close_banner(e):
        banner.open = False
        banner_value_error.open = False
        page.update()

    # Banner
    banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text("Oops, preencha todos os campos"),
        actions=[ft.TextButton("Ok", on_click=close_banner)],
    )

    banner_value_error = ft.Banner(
        bgcolor=ft.colors.RED_900,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER_100, size=40),
        content=ft.Text("Digite apenas números"),
        actions=[ft.TextButton("Ok", on_click=close_banner)],
    )

    page.overlay.append(banner)
    page.overlay.append(banner_value_error)  # Super importante isso para funcionar

    # Configurando a janela (window)
    page.window.height = 500
    page.window.width = 400

    # Configurando a app bar
    app_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Calculadora de IMC"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    # Configurando a info
    IMC = ft.Text("Descubra seu IMC", size=30)
    detalhes = ft.Text("Digite seus dados:", size=30)

    icone_padrao = ft.Icon(ft.icons.PEOPLE_OUTLINE, size=100)

    imc_and_detalhes = ft.Column(
        controls=[
            IMC,
            detalhes
        ]
    )

    INFO = ft.Row(
        controls=[
            imc_and_detalhes,
            icone_padrao
        ]
    )

    # Configurando inputs
    altura = ft.TextField(label="Altura", hint_text="Digite sua altura")
    peso = ft.TextField(label="Peso", hint_text="Digite seu peso")
    genero = ft.Dropdown(
        label="Gênero",
        hint_text="Escolha seu gênero",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
        ]
    )

    button_calcular = ft.ElevatedButton(text="Calcular IMC", on_click=calcular)

    # Layout da página
    layout = ft.ResponsiveRow(
        [
            ft.Container(
                content=INFO,
                padding=5,
                col={"sm": 4, "md": 4, "xl": 4},
                bgcolor=ft.colors.WHITE,
            ),
            ft.Container(
                altura,
                padding=5,
                col={"sm": 12, "md": 3, "xl": 3},
                bgcolor=ft.colors.WHITE,
            ),
            ft.Container(
                peso,
                padding=5,
                col={"sm": 12, "md": 3, "xl": 3},
                bgcolor=ft.colors.WHITE,
            ),
            ft.Container(
                genero,
                padding=5,
                col={"sm": 12, "md": 3, "xl": 3},
                bgcolor=ft.colors.WHITE,
            ),
            ft.Container(
                button_calcular,
                padding=5,
                col={"sm": 12, "md": 3, "xl": 3},
                bgcolor=ft.colors.WHITE,
            ),
            ft.Container(
                padding=5,
                col={"sm": 12, "md": 3, "xl": 3},
                alignment=ft.alignment.center,
            ),
        ],
    )

    page.add(app_bar, layout)
    page.update()



ft.app(target=main)