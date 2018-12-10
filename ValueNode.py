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
        super().__init__(ValueNode(value), "Value", parent)

        # Add the only output port and store its value.
        self.setValue(value)

    def setValue(self, value):
        self.data.setOutput(0, value)
        super().onDataChanged(0)