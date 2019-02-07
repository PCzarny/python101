from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName('ToDo')

        self.table = QTableView()

        self.loginButton = QPushButton('&Login')
        self.endButton = QPushButton('&End')

        buttonBroup = QHBoxLayout()
        buttonBroup.addWidget(self.loginButton)
        buttonBroup.addWidget(self.endButton)

        container = QVBoxLayout(self)
        container.addWidget(self.table)
        container.addLayout(buttonBroup)

        self.setWindowTitle('Todo list')
        self.resize(500, 300)
