import sys
import pyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():
    mbox = QMessageBox()

    mbox.setText("Your alliegance has been noted")
    mbox.setDate

if__name__=="__main__":
    app = QApplication(sys.argv)
    W = QWidget()
    W.resize(300,300)
    W.setWindowTitle("Guru99")

    Label = QLabel(W)
    Label.setText("Behold the Guru, Guru99")
    Label.move(100,130)
    Label.show()

    btn = QPushButton(W)
    btn.setText("Behold")
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(dialog)


blah blah blah    
