from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import QPoint, QRect, QSize

class Shapes:
    Rect, Ellipse, Polygon, Line = range(4)

class Shape(QWidget):
    rect = QRect(1,1, 101, 101)
    points = QPolygon([
        QPoint(1, 101),
        QPoint(51, 1),
        QPoint(101, 101)])

    def __init__(self, parent, shape=Shapes.Rect):
        super(Shape, self).__init__(parent)

        self.shape = shape
        self.borderColor = QColor(0, 0, 0)
        self.fillColor = QColor(255, 255, 255)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawFigure(e, qp)
        qp.end()

    def drawFigure(self, e, qp):
        qp.setPen(self.borderColor)
        qp.setBrush(self.fillColor)
        qp.setRenderHint(QPainter.Antialiasing)

        if self.shape == Shapes.Rect:
            qp.drawRect(self.rect)
        elif self.shape == Shapes.Ellipse:
            qp.drawEllipse(self.rect)
        elif self.shape == Shapes.Polygon:
            qp.drawPolygon(self.points)
        elif self.shape == Shapes.Line:
            qp.drawLine(self.rect.topLeft(), self.rect.bottomRight())
        else:
            qp.drawRec(self.rect)

    def sizeHint(self):
        return QSize(102, 102)

    def minimumSizeHint(self):
        return QSize(102, 102)

    def setShape(self, shape):
        self.shape = shape
        self.update()

    def setFillColor(self, r=0, g=0, b=0):
        self.fillColor = QColor(r, g, b)
        self.update()