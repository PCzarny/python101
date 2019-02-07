from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from gui import Ui_Widget
from login_dialog import LoginDialog
import db
from tab_model import TabModel

class Tasks(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super(Tasks, self).__init__(parent)
        self.setupUi(self)

        self.loginButton.clicked.connect(self.login)
        self.endButton.clicked.connect(self.end)

    def login(self):
        login, password, ok = LoginDialog.getCredentials(self)
        if not ok:
            return

        if not login or not password:
            QMessageBox.warning(self, 'Error', 'Empty username or password', QMessageBox.Ok)
            return

        self.user = db.signin(login, password)
        if self.user is None:
            QMessageBox.critical(self, 'Error', 'Incorrect pasword', QMessageBox.Ok)
            return

        tasks = db.readData(self.user)
        model.update(tasks)
        model.layoutChanged.emit()
        self.refresh()

    def refresh(self):
        self.view.setModel(model)
        self.view.hideColumn(0)
        self.view.horizontalHeader().setStretchLastSection(True)
        self.view.resizeColumnsToContents()

    def end(self):
        self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    db.connect()
    model = TabModel()
    window = Tasks()
    window.show()
    window.move(350, 200)

    sys.exit(app.exec_())