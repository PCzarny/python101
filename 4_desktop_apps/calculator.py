from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        container = QGridLayout()
        #labels
        label1 = QLabel('Number 1:', self)
        label2 = QLabel('Number 3:', self)
        label_result = QLabel('Result:', self)

        container.addWidget(label1, 0, 0)
        container.addWidget(label2, 0, 1)
        container.addWidget(label_result, 0, 2)

        #inputs
        self.number_1_edit = QLineEdit()
        self.number_2_edit = QLineEdit()
        self.result_edit = QLineEdit()

        self.result_edit.readonly = True
        self.result_edit.setToolTip('Type <b>numbers</b> and choose operation...')

        container.addWidget(self.number_1_edit, 1, 0)
        container.addWidget(self.number_2_edit, 1, 1)
        container.addWidget(self.result_edit, 1, 2)

        # buttons
        addBtn = QPushButton("&Add", self)
        substrBtn = QPushButton("&Substract", self)
        multiBtn = QPushButton("&Multiplicate", self)
        divBtn = QPushButton("&Divide", self)
        endBtn = QPushButton("&End", self)
        endBtn.resize(endBtn.sizeHint())

        # event handlers
        addBtn.clicked.connect(self.operation)
        substrBtn.clicked.connect(self.operation)
        multiBtn.clicked.connect(self.operation)
        divBtn.clicked.connect(self.operation)

        # Horizontal wrapper
        wrapper = QHBoxLayout()
        wrapper.addWidget(addBtn)
        wrapper.addWidget(substrBtn)
        wrapper.addWidget(multiBtn)
        wrapper.addWidget(divBtn)

        container.addLayout(wrapper, 2, 0, 1, 3)
        container.addWidget(endBtn, 3, 0, 1, 3)

        self.setLayout(container)

        endBtn.clicked.connect(self.finish)

        self.number_1_edit.setFocus(),

        self.setGeometry(20, 20, 300, 100)

        self.setWindowIcon(QIcon('calculator.png'))
        self.setWindowTitle('Simple calculator')

        # self.resize(300, 100)

        self.show()

    def finish(self):
        self.close()

    # overriding super method
    def closeEvent(self, event):
        shouldClose = QMessageBox.question(
            self, 'Message',
            "Are you sure?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if shouldClose == QMessageBox.Yes:
            # default event behaaviour
            event.accept()
        else:
            # ignore event
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def operation(self):
        sender = self.sender()
        try:
            number_1 = float(self.number_1_edit.text())
            number_2 = float(self.number_2_edit.text())

            result = ''

            if sender.text() == "&Add":
                result = number_1 + number_2
            elif sender.text() == "&Substract":
                result = number_1 - number_2
            elif sender.text() == "&Multiplicate":
                result = number_1 * number_2
            else:
                try:
                    result = round(number_1 / number_2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(self, 'Error', 'Can\'t divide by zero!')
                    return



            self.result_edit.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid data', QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())