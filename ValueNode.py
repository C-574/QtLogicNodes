from PyQt5.QtCore import pyqtSlot
from LogicNode import LogicNode
from NodeView import NodeView

class ValueNode(LogicNode):
    def __init__(self, value):
        super().__init__([], value)

    def process(self):
        return self.value

class ValueNodeView(NodeView):
    def __init__(self, value, parent=None):
        super().__init__(ValueNode(value), "", parent)

        self.dataChanged.connect(self.debugPrint)

        # Add the only output port and store its value.
        #super().addPort(False)
        self.setValue(value)


    @pyqtSlot(int)
    def debugPrint(self, portIndex):
        print("Node Data changed @ port " + str(portIndex))
        
    def setValue(self, value):
        self.data.setOutput(0, value)
        super().onDataChanged(0)