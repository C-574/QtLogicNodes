from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import Qt

from NodePainter import NodePainter, PORT_RADIUS
from LinkView import LinkView

class PortView(QGraphicsItem):
    def __init__(self, portIndex, isOutput, parent, title=""):
        super().__init__(parent)
        self.index = portIndex
        self.isOutput = isOutput
        self.title = title
        self.links = []

    def linkTo(self, toNode, toNodeId):
        toPort = toNode.getPortById(toNodeId)

        if toPort:
            # Check if any connection exists on both ports.
            if (not self.isConnected()) and (not toPort.isConnected()):
                link = LinkView(self, toPort)

                self.links.append(link)
                toPort.links.append(link)

    def move(self):
        for link in self.links:
            link.updatePosition()

    def isConnected(self):
        return (len(self.links) > 0)