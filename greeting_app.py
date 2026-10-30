import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"

    entered_name = {"value": ""}

    name_field = ft.TextField(
        label="Your name",
        hint_text="Type your name here",
        width=300,
    )

    async def on_continue(e):
        if not name_field.value.strip():
            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Missing name"),
                    content=ft.Text("Please enter your name before continuing."),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: page.pop_dialog()),
                    ],
                )
            )
            return
        entered_name["value"] = name_field.value.strip()
        await page.push_route("/greeting")

    async def on_back(e):
        await page.push_route("/")

    def home_view():
        return ft.View(
            route="/",
            controls=[
                ft.AppBar(title=ft.Text("Home")),
                ft.Column(
                    controls=[
                        ft.Text("Welcome!", size=28, weight=ft.FontWeight.BOLD),
                        name_field,
                        ft.Button("Continue", on_click=on_continue),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    expand=True,
                ),
            ],
        )

    def greeting_view():
        return ft.View(
            route="/greeting",
            controls=[
                ft.AppBar(title=ft.Text("Greeting")),
                ft.Column(
                    controls=[
                        ft.Text(
                            f"Hello, {entered_name['value']}!",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Button("Back", on_click=on_back),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    expand=True,
                ),
            ],
        )

    def route_change(e):
        page.views.clear()
        if page.route == "/greeting" and entered_name["value"]:
            page.views.append(greeting_view())
        else:
            page.views.append(home_view())
        page.update()

    page.on_route_change = route_change
    route_change(None)


ft.run(main)