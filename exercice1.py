from PySide2.QtWidgets import *
class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)


        self.setWindowTitle("SQL CLIENT") #titre fenetre
        self.setMinimumSize(600,400)

        self.layout = QVBoxLayout()

        self.ButtonsPanel=ButtonsPanel()
        self.layout.addWidget(self.ButtonsPanel)

        self.texte=QTextEdit()
        self.layout.addWidget(self.texte)
        

        self.resultTable=QTableWidget(5,3)
        self.layout.addWidget(self.resultTable)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)




        self.setLayout(self.layout)

class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()

        self.button1 = QPushButton("Configure")
        self.layout.addWidget(self.button1)
        self.button2 = QPushButton("Connect")
        self.layout.addWidget(self.button2)
        self.button3 = QPushButton("Disconnect")
        self.layout.addWidget(self.button3)

        self.setLayout(self.layout)






if __name__ == "__main__":
   app = QApplication([])
   win = SQLClientWindow()
   win.show()
   app.exec_()

