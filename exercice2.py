from PySide2.QtWidgets import *
class LabeledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)
        self.t=text

        self.layout = QHBoxLayout()
        self.setMaximumHeight(50)
        self.label=QLabel(self.t)
        self.layout.addWidget(self.label)
        self.texte=QTextEdit()
        self.layout.addWidget(self.texte)

        self.setLayout(self.layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()

        self.objet1=LabeledTextField("IP address")
        self.layout.addWidget(self.objet1)

        self.objet2=LabeledTextField("User")
        self.layout.addWidget(self.objet2)

        self.objet3=LabeledTextField("Password")
        self.layout.addWidget(self.objet3)

        self.setLayout(self.layout)



if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialog()
   win.show()
   app.exec_()

