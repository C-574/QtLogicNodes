from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5.QtGui import QColor, QPen, QFontMetrics

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

        color = QColor(20, 20, 20)

        if portData == 0:
            color = QColor(255, 0, 0)
        elif portData == 1:
            color = QColor(0, 255, 0)

        painter.setBrush(color)
        painter.setPen(QPen(color.darker(200), 2.0))

        painter.drawEllipse(pos, PORT_RADIUS, PORT_RADIUS)

    @staticmethod
    def drawNode(painter, isSelected, node):
        rect = NodePainter.getNodeDim(node)

        if isSelected:
            painter.setPen(QPen(Qt.cyan, 3.0))
        else:
            painter.setPen(Qt.black)

        painter.setBrush(Qt.gray)
        painter.drawRect(rect)

        for index, port in enumerate(node.data.inputs):
            NodePainter.drawPort(painter, False, index, node.data.getInput(index).value)

        #for index, port in enumerate(node.node.value):
        #    NodePainter.drawPort(painter, False, index, node.data.getOutput(index))
        NodePainter.drawPort(painter, True, 0, node.data.getOutput(0))

        metrics = QFontMetrics(painter.font())
        textBounds = metrics.boundingRect(node.title)

        painter.setPen(QColor(0, 0, 0, 128))
        painter.setBrush(QColor(0, 0, 0, 128))

        textRect = QRectF((rect.width() - textBounds.width()) / 2.0, (rect.height() - textBounds.height()) / 2.0 - 3.5, textBounds.width(), textBounds.height())
        painter.drawText(textRect.bottomLeft(), node.title)
      
