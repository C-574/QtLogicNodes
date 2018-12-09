from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QGraphicsLineItem
from PyQt5.QtCore import Qt

from NodePainter import NodePainter

class LinkView(QGraphicsLineItem):
    def __init__(self, fromNode, fromPortIndex, toNode, toPortIndex, parent=None):
        super().__init__(parent=parent)
        
        self.fromNode = fromNode
        self.fromPortIndex = fromPortIndex

        self.toNode = toNode
        self.toPortIndex = toPortIndex

    def updatePosition(self):
        startPos = self.fromNode.pos()
        endPos = self.toNode.pos()

        self.setLine(startPos.x(), startPos.y(), endPos.x(), endPos.y())