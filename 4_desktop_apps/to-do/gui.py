from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName('ToDo')

        self.view = QTableView()

        self.loginButton = QPushButton('&Login')
        self.endButton = QPushButton('&End')

        self.addButton = QPushButton('&Add')
        self.addButton.setEnabled(False)

        self.saveButton = QPushButton('&Save')
        self.saveButton.setEnabled(False)

        buttonBroup = QHBoxLayout()
        buttonBroup.addWidget(self.loginButton)
        buttonBroup.addWidget(self.addButton)
        buttonBroup.addWidget(self.saveButton)
        buttonBroup.addWidget(self.endButton)

        container = QVBoxLayout(self)
        container.addWidget(self.view)
        container.addLayout(buttonBroup)

        self.setWindowTitle('Todo list')
        self.resize(500, 300)
