# (A & B) | C = R
#  0   0    0   0
#  0   0    1   1
#  0   1    0   0
#  0   1    1   1
#  1   0    0   0
#  1   0    1   1
#  1   1    0   1
#  1   1    1   1

class LogicNode:
    def __init__(self, inputs, value):
        if inputs is None:
            self.inputs = []
        else:
            self.inputs = inputs
        self.value = value

    def process(self):
        raise NotImplementedError('Users must implement the process methods!')

    def setInput(self, portIndex, value):
        if portIndex >= len(self.inputs):
            self.inputs.append(value)
        else:
            self.inputs[portIndex] = value

    def setOutput(self, portIndex, value):
        self.value = value

    def getInput(self, portIndex):
        if portIndex >= len(self.inputs):
            return None
        
        return self.inputs[portIndex]

    def getOutput(self, portIndex):
        return self.value    


# def testNodeLogic():
#     a = ValueNode(1)
#     b = ValueNode(1)

#     c = ValueNode(1)
#     d = ValueNode(0)

#     ab = AndNode([a, b])
#     cd = AndNode([c, d])

#     abcd = OrNode([ab, cd])

#     r = abcd.process()

#     print("Result: " + str(r))
 

