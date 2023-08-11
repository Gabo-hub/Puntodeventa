from PySide6.QtWidgets import QApplication
from controllers.login_windows import LoginWindows

if __name__ == "__main__":
    app = QApplication()
    windows = LoginWindows()
    windows.show()
    app.exec()