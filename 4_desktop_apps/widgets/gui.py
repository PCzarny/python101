from __future__ import unicode_literals
from shape import Shape, Shapes

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QButtonGroup, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QSlider, QLCDNumber, QSplitter
from PyQt5.QtWidgets import QRadioButton, QGroupBox
from PyQt5.QtWidgets import QComboBox, QSpinBox
from PyQt5.QtWidgets import QPushButton

class Ui_Widget(object):
    def setupUi(self, Widget):
        self.shape1 = Shape(self, Shapes.Polygon)
        self.shape2 = Shape(self, Shapes.Ellipse)
        self.activeShape = self.shape1

        # Check Boxex panel
        checkboxWrapper = QVBoxLayout()
        self.checkboxGroup = QButtonGroup()
        for i, value in enumerate(('Square', 'Circle', 'Triangle', 'Line')):
            self.checkbox = QCheckBox(value)
            self.checkboxGroup.addButton(self.checkbox, i)
            checkboxWrapper.addWidget(self.checkbox)
        self.checkboxGroup.buttons()[self.activeShape.shape].setChecked(True)

        self.activeShapeCheckbox = QCheckBox('<=')
        self.activeShapeCheckbox.setChecked(True)
        checkboxWrapper.addWidget(self.activeShapeCheckbox)

        checkboxContainer = QHBoxLayout()
        checkboxContainer.addWidget(self.shape1)
        checkboxContainer.addLayout(checkboxWrapper)
        checkboxContainer.addWidget(self.shape2)

        # Slider panel
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)

        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        sliderContainer = QSplitter(Qt.Horizontal, self)
        sliderContainer.addWidget(self.slider)
        sliderContainer.addWidget(self.lcd)
        sliderContainer.setSizes((125, 75))

        # Radio buttons
        self.radioContainer = QHBoxLayout()
        for v in ('R', 'G', 'B'):
            self.radio = QRadioButton(v)
            self.radioContainer.addWidget(self.radio)
        self.radioContainer.itemAt(0).widget().setChecked(True)

        self.radioGroup = QGroupBox('RGB options')
        self.radioGroup.setLayout(self.radioContainer)
        self.radioGroup.setObjectName('Radio')
        self.radioGroup.setCheckable(True)

        # ComboBox and SpinBox
        self.listRGB = QComboBox(self)
        for v in ('R', 'G', 'B'):
            self.listRGB.addItem(v)
        self.listRGB.setEnabled(False)

        # SpinBox
        self.spinRGB = QSpinBox()
        self.spinRGB.setMinimum(0)
        self.spinRGB.setMaximum(255)
        self.spinRGB.setEnabled(False)

        comboContainer = QVBoxLayout()
        comboContainer.addWidget(self.listRGB)
        comboContainer.addWidget(self.spinRGB)

        radioRow = QHBoxLayout()
        radioRow.addWidget(self.radioGroup)
        radioRow.insertSpacing(1, 25)
        radioRow.addLayout(comboContainer)

        # Push button
        pushContainer = QHBoxLayout()
        self.groupP = QButtonGroup()
        self.groupP.setExclusive(False)
        for v in ('R', 'G', 'B'):
            self.btn = QPushButton(v)
            self.btn.setCheckable(True)
            self.groupP.addButton(self.btn)
            pushContainer.addWidget(self.btn)

        self.groupPBtn = QGroupBox('RGB Buttons')
        self.groupPBtn.setLayout(pushContainer)
        self.groupPBtn.setObjectName('Push')
        self.groupPBtn.setCheckable(True)
        self.groupPBtn.setChecked(False)

        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(checkboxContainer)
        mainLayout.addWidget(sliderContainer)
        mainLayout.addLayout(radioRow)
        mainLayout.addWidget(self.groupPBtn)

        self.setLayout(mainLayout)
        self.setWindowTitle('Widgets')
