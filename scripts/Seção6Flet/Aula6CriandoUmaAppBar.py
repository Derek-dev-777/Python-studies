import flet as ft

def main(page: ft.Page):
    page.title = "AppBar"

    app_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALLET),
        leading_width=40,
        title=ft.Text("App bar example"),
        center_title=True,
        bgcolor=ft.colors.SURFACE
    )

    page.add(
        app_bar,
    )

ft.app(target=main)