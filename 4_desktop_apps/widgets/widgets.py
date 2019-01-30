from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor
from gui import Ui_Widget

class Widgets(QWidget, Ui_Widget):
    """Main class of application"""
    chanels = {'R'}
    fillColor = QColor(0, 0, 0)

    def __init__(self, parent=None):
        super(Widgets, self).__init__(parent)
        self.setupUi(self)

        # events and slots
        self.checkboxGroup.buttonClicked[int].connect(self.setShape)
        self.activeShapeCheckbox.clicked.connect(self.activateShape)

    def setShape(self, value):
        self.activeShape.setShape(value)

    def activateShape(self, value):
        sender = self.sender()
        if value:
            self.activeShape = self.shape1
            sender.setText('<=')
        else:
            self.activeShape = self.shape2
            sender.setText('=>')

        self.checkboxGroup.buttons()[self.activeShape.shape].setChecked(True)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Widgets()
    window.show()

    sys.exit(app.exec_())