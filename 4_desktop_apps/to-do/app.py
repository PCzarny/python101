from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from gui import Ui_Widget

class Tasks(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super(Tasks, self).__init__(parent)
        self.setupUi(self)

        self.loginButton.clicked.connect(self.login)
        self.endButton.clicked.connect(self.end)

    def login(self):
        login, ok = QInputDialog.getText(self, 'Login', 'Enter username:')
        if ok:
            password, ok = QInputDialog.getText(self, 'Login', 'Enter password:')
            if ok:
                if not login or not password:
                    QMessageBox.warning(self, 'Error', 'Empty username or password', QMessageBox.Ok)
                    return
                QMessageBox.information(self, 'Login data', 'You\'ve entered data', QMessageBox.Ok)

    def end(self):
        self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Tasks()
    window.show()
    window.move(350, 200)

    sys.exit(app.exec_())