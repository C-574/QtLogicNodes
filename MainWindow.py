import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QAction
from PyQt5.QtGui import QPainter, QKeySequence
from PyQt5.QtCore import Qt

from OrNode import OrNodeView
from AndNode import AndNodeView
from ValueNode import ValueNodeView


class MainWindow(QMainWindow):

    def toggleSelectedValue(self):
        selectedItems = self.scene.selectedItems()
        if len(selectedItems) >= 1:
            node = selectedItems[0]
            node.setValue(not node.data.value)        

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

    def initScene(self):
        valueNodeA = ValueNodeView(self.scene, 1)
        valueNodeA.setPos(0, 10)
        valueNodeB = ValueNodeView(self.scene, 0)
        valueNodeB.setPos(0, 50)
        valueNodeC = ValueNodeView(self.scene, 0)
        valueNodeC.setPos(0, 110)
        valueNodeD = ValueNodeView(self.scene, 1)
        valueNodeD.setPos(0, 150)
        valueNodeE = ValueNodeView(self.scene, 0)
        valueNodeE.setPos(0, 250)

        orNode = OrNodeView(self.scene, [valueNodeA, valueNodeB])
        orNode.setPos(300, 40)

        andNode = AndNodeView(self.scene, [
            orNode,
            valueNodeC,
            valueNodeD,
            valueNodeE
        ])
        andNode.setPos(400, 90)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # This will raise an exception to exit from python but will be caught by the debugger.
    # For now just uncheck 'Uncaught Exceptions' but that is just a workaround.
    sys.exit(app.exec_())
