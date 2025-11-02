import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def on_refresh_clicked(button):
    print("Обновление каталога...")


def build_ui(app: toga.App) -> toga.Box:
    refresh_btn = toga.Button("Обновить каталог", on_press=on_refresh_clicked)
    root = toga.Box(style=Pack(direction=COLUMN, padding=16))
    top = toga.Box(style=Pack(direction=ROW, padding_bottom=12))
    top.add(refresh_btn)
    root.add(top)
    return root


def startup(app: toga.App):
    app.main_window = toga.MainWindow(title=app.formal_name)
    app.main_window.content = build_ui(app)
    app.main_window.show()


def main() -> toga.App:
    return toga.App(
        formal_name="X-Port",
        app_id="ru.xportstore",
        startup=startup,
    )
