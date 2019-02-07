from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QGridLayout

def formatInput(lineEdit):
    return lineEdit.text().strip()

class LoginDialog(QDialog):
    """Dialog window for login"""

    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        self.login = QLineEdit()
        self.password = QLineEdit()

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)

        container = QGridLayout(self)
        container.addWidget(QLabel('Login'), 0, 0)
        container.addWidget(self.login, 0, 1)
        container.addWidget(QLabel('Password'), 1, 0)
        container.addWidget(self.password, 1, 1)
        container.addWidget(self.buttons, 2, 0, 2, 0)

        # Slots and events
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.setModal(True)
        self.setWindowTitle('Sign in')

    @staticmethod
    def getCredentials(parent=None):
        dialog = LoginDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        return (formatInput(dialog.login), formatInput(dialog.password), ok == QDialog.Accepted)