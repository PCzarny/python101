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

        # ComboBox and Spin Box
        self.radioGroup.clicked.connect(self.setState)
        self.listRGB.activated[str].connect(self.setChanelCBox)
        self.spinRGB.valueChanged[int].connect(self.changeColor)

        # Push button
        for btn in self.groupP.buttons():
            btn.clicked[bool].connect(self.setChanelPBtn)
        self.groupPBtn.clicked.connect(self.setState)

        # QLabel and QEditLine
        for v in ('R', 'G', 'B'):
            color = getattr(self, 'color' + v)
            color.textEdited.connect(self.changeColor)

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
        value = int(value)
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
        self.info()

    def setState(self, value):
        if value:
            self.listRGB.setEnabled(False)
            self.spinRGB.setEnabled(False)
        else:
            self.listRGB.setEnabled(True)
            self.spinRGB.setEnabled(True)
            self.chanels = set()
            self.chanels.add(self.listRGB.currentText())

    def setChanelCBox(self, value):
        self.chanels = set()
        self.chanels.add(value)

    def setChanelPBtn(self, value):
        sender = self.sender()
        if value:
            self.chanels.add(sender.text())
        elif value in self.chanels:
            self.chanels.remove(sender.text())

    def info(self):
        fontB = "QWidget { font-weight: bold }"
        fontN = "QWidget { font-weight: normal }"

        for v in ('R', 'G', 'B'):
            label = getattr(self, 'label' + v)
            color = getattr(self, 'color' + v)
            if v in self.chanels:
                label.setStyleSheet(fontB)
                color.setEnabled(True)
            else:
                label.setStyleSheet(fontN)
                color.setEnabled(False)

        self.colorR.setText(str(self.fillColor.red()))
        self.colorG.setText(str(self.fillColor.green()))
        self.colorB.setText(str(self.fillColor.blue()))




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Widgets()
    window.show()

    sys.exit(app.exec_())