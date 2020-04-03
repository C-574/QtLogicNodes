from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGraphicsObject

from NodePainter import NodePainter


class NodeView(QGraphicsObject):

    dataChanged = pyqtSignal(int)

    def __init__(self, node, title, parent=None):
        super().__init__(parent=parent)
        self.data = node
        self.title = title
        self.setFlags(QGraphicsObject.ItemIsMovable | QGraphicsObject.ItemIsSelectable)

        self.xChanged.connect(self.onMove)
        self.yChanged.connect(self.onMove)

    def onMove(self):
        # @Todo: Notify the parent scene that the node has moved.
        pass

    def onDataChanged(self, portIndex):
        print("Updating " + self.title)
        self.dataChanged.emit(portIndex)
        self.data.process()
        self.update()

    def boundingRect(self):
        bounds = NodePainter.getNodeBounds(self)
        return bounds

    def paint(self, painter, option, widget):
        # rect = self.boundingRect()

        # Draw the bouds for debugging
        # painter.drawRect(NodePainter.getNodeBounds(self.node))
        NodePainter.drawNode(painter, self.isSelected(), self)
