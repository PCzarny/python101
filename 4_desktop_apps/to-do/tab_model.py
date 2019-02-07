from __future__ import unicode_literals
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant

class TabModel(QAbstractTableModel):
    def __init__(self, fields=[], data=[], parent=None):
        super(TabModel, self).__init__()
        self.fields = fields
        self.content = data

    def update(self, data):
        print(data)
        self.content = data

    def rowCount(self, parent=QModelIndex()):
        """Return row number"""
        return len(self.content)

    def columnCount(self, parent=QModelIndex()):
        if self.content:
            return len(self.content[0])
        else:
            return 0

    def data(self, index, role=Qt.DisplayRole):
        i = index.row()
        j = index.column()

        if role == Qt.DisplayRole:
            return '{0}'.format(self.content[i][j])
        else:
            return QVariant()