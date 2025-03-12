import flet as ft

def main(page: ft.Page):
    page.title = "BMI Calculator"
    input_weight = ft.TextField(hint_text="Enter your weight (kg)")
    input_height = ft.TextField(hint_text="Enter your height (cm)")
    result_text = ft.Text("")
    

    page.window.height = 350
    page.window.width = 450
    page.window.alignment = ft.alignment.center

    def calculate_bmi(e):
        try:
            weight = float(input_weight.value)
            height = float(input_height.value) / 100
            bmi = weight / (height ** 2)
            result_text.value = f"Your BMI is: {bmi:.1f}"
        except ValueError:
            result_text.value = "Please enter valid numbers!"
        page.update()
    
    calculate_button = ft.FilledButton("Calculate", on_click=calculate_bmi, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))

    # page.add(input_weight, input_height)
    page.add(
        ft.Container(
            content=input_height,
            alignment=ft.alignment.center,
            expand=True,
            padding=ft.Padding(top=10, bottom=5, left=10, right=10)
        ),

        ft.Container(
            content=input_weight,
            alignment=ft.alignment.center,
            expand=True,
            padding=ft.Padding(top=5, bottom=10, left=10, right=10)
        ),

        ft.Container(
            content=calculate_button,
            alignment=ft.alignment.center,
            expand=True,
            padding=ft.Padding(top=5, bottom=5, left=10, right=10)
        ),

        ft.Container(
            content=result_text,
            alignment=ft.alignment.center,
            expand=True,
            padding=ft.Padding(top=5, bottom=10, left=10, right=10)
        )
    )
    
    page.update()

ft.app(main)