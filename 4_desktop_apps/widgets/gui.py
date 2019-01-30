from __future__ import unicode_literals
from shape import Shape, Shapes

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QButtonGroup, QVBoxLayout, QHBoxLayout

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

        self.setLayout(checkboxContainer)
        self.setWindowTitle('Widgets')
