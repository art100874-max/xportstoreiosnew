import os
import traceback
import toga


def _build_ui(app: toga.App) -> toga.Box:
    box = toga.Box()
    box.add(toga.Label("XPort: hello iOS 👋"))
    return box


def _startup(app: toga.App):
    # безопасный старт с записью стека в файл при любой ошибке
    try:
        app.main_window = toga.MainWindow(title="XPort")
        app.main_window.content = _build_ui(app)
        app.main_window.show()
    except Exception:
        # пишем лог падения в Documents приложения
        try:
            docs_dir = app.paths.documents  # On My iPhone / XPort
            os.makedirs(docs_dir, exist_ok=True)
            with open(os.path.join(docs_dir, "last_crash.txt"), "w", encoding="utf-8") as f:
                traceback.print_exc(file=f)
        except Exception:
            pass
        raise


def main() -> toga.App:
    # имя и app_id должны совпадать с pyproject.toml
    return toga.App(formal_name="XPort", app_id="ru.xportstore", startup=_startup)
