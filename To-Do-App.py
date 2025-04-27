import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 800
    page.window_height = 600

    task_column = ft.Column()
    task_input = ft.TextField(label='Insert the task', expand=True)

    def add_task(e):
        if task_input.value.strip():  # Validar que no esté vacío
            # Primero creamos el Checkbox
            checkbox = ft.Checkbox(label=task_input.value, value=False)
            
            # Luego creamos el botón de borrar
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                tooltip='Remove task'
            )
            
            # Ahora creamos la fila completa
            task_row = ft.Row(
                controls=[checkbox, delete_button],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
            
            # Configuramos el evento del botón después de crear la fila
            delete_button.on_click = lambda e: remove_task(e, task_row)
            
            task_column.controls.append(task_row)
            task_input.value = ''
            page.update()

    def remove_task(e, row_remove):
        task_column.controls.remove(row_remove)
        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text('My To Do List', size=30),
                ft.Row(
                    controls=[
                        task_input,
                        ft.IconButton(ft.icons.ADD, on_click=add_task),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                task_column,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)