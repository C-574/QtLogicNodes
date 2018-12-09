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
    def __init__(self, inputCount, valA, valB, parent=None):
        super().__init__(OrNode(None), "OR", parent)

        # Add all available input ports.
        #for inputIndex in range(inputCount):
        #    super().addPort(True)

        valA.dataChanged.connect(self.test)
        valB.dataChanged.connect(self.test)
        

        self.setValue(0, valA.data)
        self.setValue(1, valB.data)

    @pyqtSlot(int)
    def test(self, foo):
        super().onDataChanged(foo)

    def setValue(self, portIndex, value):
        self.data.setInput(portIndex, value)
        super().onDataChanged(portIndex)