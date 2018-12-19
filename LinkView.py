from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtWidgets import QGraphicsObject
from PyQt5.QtCore import Qt

from NodePainter import NodePainter

class LinkView(QGraphicsObject):
    def __init__(self, fromNode, fromPortIndex, toNode, toPortIndex, parent=None):
        super().__init__(parent=parent)
        
        self.fromNode = fromNode
        self.fromPortIndex = fromPortIndex

        self.toNode = toNode
        self.toPortIndex = toPortIndex

        self.startPos = QPointF()
        self.endPos = QPointF()

        self.updatePosition()

    def updatePosition(self):
        startPos = self.fromNode.pos()
        endPos = self.toNode.pos()

        self.startPos = startPos + (NodePainter.getPortPos(True, self.fromPortIndex))
        self.endPos += endPos + (NodePainter.getPortPos(False, self.toPortIndex))

    def paint(self, painter, option, widget):
        startPos = self.mapToScene(self.startPos)
        endPos = self.mapToScene(self.endPos)

        painter.drawLine(startPos.x(), startPos.y(), endPos.x(), endPos.y())