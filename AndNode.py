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