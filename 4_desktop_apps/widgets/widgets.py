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

        # slider and radio buttons
        for i in range(self.radioContainer.count()):
            self.radioContainer.itemAt(i).widget().toggled.connect(self.setColorChanel)
        self.slider.valueChanged.connect(self.changeColor)

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

    def setColorChanel(self, value):
        self.chanels = set() # reset chanels set
        sender = self.sender()
        if value:
            self.chanels.add(sender.text())

    def changeColor(self, value):
        self.lcd.display(value)

        if 'R' in self.chanels:
            self.fillColor.setRed(value)
        if 'G' in self.chanels:
            self.fillColor.setGreen(value)
        if 'B' in self.chanels:
            self.fillColor.setBlue(value)

        self.activeShape.setFillColor(
            self.fillColor.red(),
            self.fillColor.green(),
            self.fillColor.blue())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Widgets()
    window.show()

    sys.exit(app.exec_())