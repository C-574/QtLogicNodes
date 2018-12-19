from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QGraphicsScene
from NodeView import NodeView
from LinkView import LinkView
from LogicNode import LogicNode

class AndNode(LogicNode):
    def __init__(self, inputs):
        super().__init__(inputs, 0)

    def process(self):
        result = 1

        for input in self.inputs:
            result &= input.process()

        self.value = result
        return result

    
class AndNodeView(NodeView):
    def __init__(self, scene, inputs, parent=None):
        super().__init__(AndNode(None), "AND", parent)

        # Add all available input ports.
        for inputPortIndex, inputNode in enumerate(inputs):
            inputNode.dataChanged.connect(self.onDataChanged)
            self.setValue(inputPortIndex, inputNode.data)
            #link = LinkView(self, inputPortIndex, inputNode, 0)
            #scene.addItem(link)

        scene.addItem(self)

    def setValue(self, portIndex, value):
        self.data.setInput(portIndex, value)
        super().onDataChanged(portIndex)