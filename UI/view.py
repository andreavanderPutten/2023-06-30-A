import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddsquadra = None
        self._ddanno = None
        self.btn_graph = None
        self.txtOut = None
        self.txt_container = None

        self.btn_tifosi = None
        self.btn_details = None
        self.txtOut2 = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Lab11: Prova tema d'esame", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self._ddsquadra = ft.Dropdown(label="Squadra")
        self._ddanno = ft.Dropdown(label="anno")
        self._txttitolo = ft.TextField(label="")

        # button for the "creat graph" reply
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self._ddsquadra, self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._controller.fillDD()

        # List View where the reply is printed
        self.txtOut = ft.ListView(expand=1, spacing=10, padding=10, auto_scroll=True)
        self._page.controls.append(self.txtOut)

        self.btn_details = ft.ElevatedButton(text="Dettagli", on_click=self._controller.handle_details)
        row2 = ft.Row([self._ddanno, self.btn_details], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.btn_tifosi = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_tifosi)
        row3 = ft.Row([self._txttitolo,self.btn_tifosi],alignment=ft.MainAxisAlignment.CENTER)
        self.txtOut2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txtOut2)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()