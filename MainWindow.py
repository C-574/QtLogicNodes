import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QAction
from PyQt5.QtGui import QPainter, QColor, QFont, QKeySequence
from PyQt5.QtCore import Qt

from NodeView import NodeView
from OrNode import OrNode, OrNodeView
from AndNode import AndNode, AndNodeView
from ValueNode import ValueNode, ValueNodeView


class MainWindow(QMainWindow):

    def toggleSelectedValue(self):
        selectedItems = self.scene.selectedItems()
        if len(selectedItems) >= 1:
            node = selectedItems[0]
            node.setValue(not node.data.value)
            node.onDataChanged(0)
        

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Node Application")
        self.setGeometry(50, 150, 640, 480)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu(self.tr("&File"))
        editMenu = mainMenu.addMenu(self.tr("&Edit"))

        quitAction = QAction(self.tr("&Quit"), self)
        quitAction.setShortcut(QKeySequence.Quit)
        quitAction.setStatusTip(self.tr("Quit the application"))
        quitAction.triggered.connect(self.close)
        fileMenu.addAction(quitAction)

        toggleAction = QAction(self.tr("Toggle State"), self)
        toggleAction.setShortcut("Ctrl+T")
        toggleAction.triggered.connect(self.toggleSelectedValue)
        editMenu.addAction(toggleAction)


        self.graphicsView = QGraphicsView()
        # self.graphicsView.setMouseTracking(True)
        # self.graphicsView.viewport().installEventFilter(self)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(self.graphicsView)
        
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.initScene()


        # a = self.addNode(ValueNode(1))
        # b = self.addNode(ValueNode(0))
        # c = self.addNode(ValueNode(1))

        # a.setPos(0, 0)
        # b.setPos(0, 50)
        # a.setPos(0, 100)

        # node = self.addNode(OrNode([a.node, b.node, c.node]))
        # node.setPos(200, 60)
        # node.addPort(True)
        # node.addPort(True)
        # node.addPort(True)
        # node.addPort(True)
        # node.addPort(True)
        # node.addPort(False)
        # node.process()

        #self.scene.setSceneRect(-1000, -1000, 1000, 1000)

    def initScene(self):
        valueNodeA = ValueNodeView(0)
        valueNodeA.setPos(0, 10)
        valueNodeB = ValueNodeView(0)
        valueNodeB.setPos(0, 50)
        valueNodeC = ValueNodeView(0)
        valueNodeC.setPos(0, 80)
        valueNodeD = ValueNodeView(1)
        valueNodeD.setPos(0, 110)

        orNode = OrNodeView([valueNodeA, valueNodeB])
        orNode.setPos(300, 40)

        andNode = AndNodeView([orNode, valueNodeC, valueNodeD])
        andNode.setPos(400, 90)
        
        self.scene.addItem(orNode)
        self.scene.addItem(andNode)
        self.scene.addItem(valueNodeA)
        self.scene.addItem(valueNodeB)
        self.scene.addItem(valueNodeC)
        self.scene.addItem(valueNodeD)


        valueNodeA.setValue(1)

    def addNode(self, node):
        title = ""
        if isinstance(node, OrNode):
            title = "OR"
        elif isinstance(node, AndNode):
            title = "AND"

        view = NodeView(node, title)
        self.scene.addItem(view)
        
        return view

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())