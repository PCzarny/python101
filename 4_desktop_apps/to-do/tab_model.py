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
        elif role == Qt.CheckStateRole and (j == 3 or j == 4):
            if self.content[i][j]:
                return Qt.Checked
            else:
                return Qt.Unchecked
        elif role == Qt.EditRole and j == 1:
            return self.content[i][j]
        else:
            return QVariant()

    def flags(self, index):
        flags = super(TabModel, self).flags(index)
        j = index.column()
        if j == 1:
            flags |= Qt.ItemIsEditable
        elif j == 3 or j == 4:
            flags |= Qt.ItemIsUserCheckable
        return flags

    def setData(self, index, value, role=Qt.DisplayRole):
        i = index.row()
        j = index.column()
        if role == Qt.EditRole and j == 1:
            self.content[i][j] = value
        elif role ==Qt.CheckStateRole and (j == 3 or j == 4):
            if value:
                self.content[i][j] = True
            else:
                self.content[i][j] = False
        return True

    def headerData(self, section, direction, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and direction == Qt.Horizontal:
            return self.fields[section]
        elif role == Qt.DisplayRole and direction == Qt.Vertical:
            return section + 1
        else:
            return QVariant()