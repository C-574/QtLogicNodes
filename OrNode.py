from PyQt5.QtCore import pyqtSlot
from LogicNode import LogicNode
from NodeView import NodeView

class OrNode(LogicNode):
    def __init__(self, inputs):
        super().__init__(inputs, 0)

    def process(self):
        result = 0

        for input in self.inputs:
            result |= input.process()

        self.value = result
        return result



class OrNodeView(NodeView):
    def __init__(self, scene, inputs, parent=None):
        super().__init__(OrNode(None), "OR", parent)

        # Add all available input ports.
        for index, inputNode in enumerate(inputs):
            inputNode.dataChanged.connect(self.onDataChanged)
            self.setValue(index, inputNode.data)

        scene.addItem(self)

    def setValue(self, portIndex, value):
        self.data.setInput(portIndex, value)
        super().onDataChanged(portIndex)