from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtCore import Qt

PORT_RADIUS = 5
NODE_WIDTH = 50
VERTICAL_PADDING = 10

class NodePainter:

    @staticmethod
    def getPortPos(isOutput, index):

        x = 0
        y = VERTICAL_PADDING

        if isOutput:
            x += NODE_WIDTH
        
        y += index * (PORT_RADIUS + VERTICAL_PADDING)

        result = QPointF(x, y)
        
        return result

    @staticmethod
    def getNodeBounds(node):
        rect = NodePainter.getNodeDim(node)

        halfPortRadius = PORT_RADIUS / 2
        result = QRectF(rect.x() - halfPortRadius, rect.y(), rect.width() + PORT_RADIUS, rect.height())
        return result

    @staticmethod
    def getNodeDim(node):
        lastPortPos = NodePainter.getPortPos(True, len(node.data.inputs))
        lastPortPosOut = NodePainter.getPortPos(False, 1)

        maxY = max(lastPortPos.y(), lastPortPosOut.y())

        topLeft = QPointF(0, 0)
        bottomRight = QPointF(NODE_WIDTH, maxY)
        return QRectF(topLeft, bottomRight)

    @staticmethod
    def drawPort(painter, isOutput, portIndex, portData):
        pos = NodePainter.getPortPos(isOutput, portIndex)

        if portData == 0:
            painter.setBrush(Qt.red)
        elif portData == 1:
            painter.setBrush(Qt.green)
        else:
            painter.setBrush(Qt.darkGray)

        painter.drawEllipse(pos, PORT_RADIUS, PORT_RADIUS)

    @staticmethod
    def drawNode(painter, node):
        rect = NodePainter.getNodeDim(node)

        painter.setBrush(Qt.gray)
        painter.drawRect(rect)

        for index, port in enumerate(node.data.inputs):
            NodePainter.drawPort(painter, False, index, node.data.getInput(index).value)

        #for index, port in enumerate(node.node.value):
        #    NodePainter.drawPort(painter, False, index, node.data.getOutput(index))
        NodePainter.drawPort(painter, True, 0, node.data.getOutput(0))
        
