from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load the UI file
        uic.loadUi("titack.ui", self)
        # define counter to track the turn
        self.counter = 0

        # define our widgets
        self.button1 = self.findChild(QPushButton, "p1")
        self.button2 = self.findChild(QPushButton, "p2")
        self.button3 = self.findChild(QPushButton, "p3")
        self.button4 = self.findChild(QPushButton, "p4")
        self.button5 = self.findChild(QPushButton, "p5")
        self.button6 = self.findChild(QPushButton, "p6")
        self.button7 = self.findChild(QPushButton, "p7")
        self.button8 = self.findChild(QPushButton, "p8")
        self.button9 = self.findChild(QPushButton, "p9")
        self.button10 = self.findChild(QPushButton, "p10")
        self.button11 = self.findChild(QPushButton, "p11")
        self.button12 = self.findChild(QPushButton, "p12")
        self.button13 = self.findChild(QPushButton, "p13")
        self.button14 = self.findChild(QPushButton, "p14")
        self.button15 = self.findChild(QPushButton, "p15")
        self.button16 = self.findChild(QPushButton, "p16")
        self.button17 = self.findChild(QPushButton, "p17")
        self.button18 = self.findChild(QPushButton, "p18")
        self.button19 = self.findChild(QPushButton, "p19")
        self.button20 = self.findChild(QPushButton, "p20")
        self.button21 = self.findChild(QPushButton, "p21")
        self.button22 = self.findChild(QPushButton, "p22")
        self.button23 = self.findChild(QPushButton, "p23")
        self.button24 = self.findChild(QPushButton, "p24")
        self.button25 = self.findChild(QPushButton, "p25")

        self.button26 = self.findChild(QPushButton, "start")

        self.label = self.findChild(QLabel, "label")

        # connect the buttons to the clicker method
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.button10.clicked.connect(lambda: self.clicker(self.button10))
        self.button11.clicked.connect(lambda: self.clicker(self.button11))
        self.button12.clicked.connect(lambda: self.clicker(self.button12))
        self.button13.clicked.connect(lambda: self.clicker(self.button13))
        self.button14.clicked.connect(lambda: self.clicker(self.button14))
        self.button15.clicked.connect(lambda: self.clicker(self.button15))
        self.button16.clicked.connect(lambda: self.clicker(self.button16))
        self.button17.clicked.connect(lambda: self.clicker(self.button17))
        self.button18.clicked.connect(lambda: self.clicker(self.button18))
        self.button19.clicked.connect(lambda: self.clicker(self.button19))
        self.button20.clicked.connect(lambda: self.clicker(self.button20))
        self.button21.clicked.connect(lambda: self.clicker(self.button21))
        self.button22.clicked.connect(lambda: self.clicker(self.button22))
        self.button23.clicked.connect(lambda: self.clicker(self.button23))
        self.button24.clicked.connect(lambda: self.clicker(self.button24))
        self.button25.clicked.connect(lambda: self.clicker(self.button25))

        self.button26.clicked.connect(lambda: self.reset())

        self.show()

    def clicker(self, button):
        if button.text() == "":
            if self.counter % 2 == 0:
                button.setText("X")
                self.label.setText("Player 2's Turn (O)")
            else:
                button.setText("O")
                self.label.setText("Player 1's Turn (X)")
            self.counter += 1
            self.checkWin()

    def checkWin(self):
        # Rows
        if (
            self.button1.text() == self.button2.text() == self.button3.text() == self.button4.text() == self.button5.text() != ""
            or self.button6.text() == self.button7.text() == self.button8.text() == self.button9.text() == self.button10.text() != ""
            or self.button11.text() == self.button12.text() == self.button13.text() == self.button14.text() == self.button15.text() != ""
            or self.button16.text() == self.button17.text() == self.button18.text() == self.button19.text() == self.button20.text() != ""
            or self.button21.text() == self.button22.text() == self.button23.text() == self.button24.text() == self.button25.text() != ""
        ):
            self.win(self.button1, self.button2, self.button3, self.button4, self.button5)
            self.win(self.button6, self.button7, self.button8, self.button9, self.button10)
            self.win(self.button11, self.button12, self.button13, self.button14, self.button15)
            self.win(self.button16, self.button17, self.button18, self.button19, self.button20)
            self.win(self.button21, self.button22, self.button23, self.button24, self.button25)

        # Columns
        if (
            self.button1.text() == self.button6.text() == self.button11.text() == self.button16.text() == self.button21.text() != ""
            or self.button2.text() == self.button7.text() == self.button12.text() == self.button17.text() == self.button22.text() != ""
            or self.button3.text() == self.button8.text() == self.button13.text() == self.button18.text() == self.button23.text() != ""
            or self.button4.text() == self.button9.text() == self.button14.text() == self.button19.text() == self.button24.text() != ""
            or self.button5.text() == self.button10.text() == self.button15.text() == self.button20.text() == self.button25.text() != ""
        ):
            self.win(self.button1, self.button6, self.button11, self.button16, self.button21)
            self.win(self.button2, self.button7, self.button12, self.button17, self.button22)
            self.win(self.button3, self.button8, self.button13, self.button18, self.button23)
            self.win(self.button4, self.button9, self.button14, self.button19, self.button24)
            self.win(self.button5, self.button10, self.button15, self.button20, self.button25)

        # Diagonals
        if (
            self.button1.text() == self.button7.text() == self.button13.text() == self.button19.text() == self.button25.text() != ""
            or self.button5.text() == self.button9.text() == self.button13.text() == self.button17.text() == self.button21.text() != ""
        ):
            self.win(self.button1, self.button7, self.button13, self.button19, self.button25)
            self.win(self.button5, self.button9, self.button13, self.button17, self.button21)

        # Draw
        if (
            self.button1.text() != "" and self.button2.text() != "" and self.button3.text() != "" and self.button4.text() != "" and self.button5.text() != "" and
            self.button6.text() != "" and self.button7.text() != "" and self.button8.text() != "" and self.button9.text() != "" and self.button10.text() != "" and
            self.button11.text() != "" and self.button12.text() != "" and self.button13.text() != "" and self.button14.text() != "" and self.button15.text() != "" and
            self.button16.text() != "" and self.button17.text() != "" and self.button18.text() != "" and self.button19.text() != "" and self.button20.text() != "" and
            self.button21.text() != "" and self.button22.text() != "" and self.button23.text() != "" and self.button24.text() != "" and self.button25.text() != ""
        ):
            self.label.setText("It's a Draw!")
            self.button1.setStyleSheet("background-color: blue")
            self.button2.setStyleSheet("background-color: blue")
            self.button3.setStyleSheet("background-color: blue")
            self.button4.setStyleSheet("background-color: blue")
            self.button5.setStyleSheet("background-color: blue")
            self.button6.setStyleSheet("background-color: blue")
            self.button7.setStyleSheet("background-color: blue")
            self.button8.setStyleSheet("background-color: blue")
            self.button9.setStyleSheet("background-color: blue")
            self.button10.setStyleSheet("background-color: blue")
            self.button11.setStyleSheet("background-color: blue")
            self.button12.setStyleSheet("background-color: blue")
            self.button13.setStyleSheet("background-color: blue")
            self.button14.setStyleSheet("background-color: blue")
            self.button15.setStyleSheet("background-color: blue")
            self.button16.setStyleSheet("background-color: blue")
            self.button17.setStyleSheet("background-color: blue")
            self.button18.setStyleSheet("background-color: blue")
            self.button19.setStyleSheet("background-color: blue")
            self.button20.setStyleSheet("background-color: blue")
            self.button21.setStyleSheet("background-color: blue")
            self.button22.setStyleSheet("background-color: blue")
            self.button23.setStyleSheet("background-color: blue")
            self.button24.setStyleSheet("background-color: blue")
            self.button25.setStyleSheet("background-color: blue")


    def win(self, b1, b2, b3, b4, b5):
        b1.setStyleSheet("background-color: red")
        b2.setStyleSheet("background-color: red")
        b3.setStyleSheet("background-color: red")
        b4.setStyleSheet("background-color: red")
        b5.setStyleSheet("background-color: red")

        self.button1.setEnabled(False)
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        self.button4.setEnabled(False)
        self.button5.setEnabled(False)
        self.button6.setEnabled(False)
        self.button7.setEnabled(False)
        self.button8.setEnabled(False)
        self.button9.setEnabled(False)
        self.button10.setEnabled(False)
        self.button11.setEnabled(False)
        self.button12.setEnabled(False)
        self.button13.setEnabled(False)
        self.button14.setEnabled(False)
        self.button15.setEnabled(False)
        self.button16.setEnabled(False)
        self.button17.setEnabled(False)
        self.button18.setEnabled(False)
        self.button19.setEnabled(False)
        self.button20.setEnabled(False)
        self.button21.setEnabled(False)
        self.button22.setEnabled(False)
        self.button23.setEnabled(False)
        self.button24.setEnabled(False)
        self.button25.setEnabled(False)

        if b1.text() == "X":
            self.label.setText("Player 1 Wins!")
        else:
            self.label.setText("Player 2 Wins!")

    def reset(self):
        self.counter = 0

        self.button1.setText("")
        self.button2.setText("")
        self.button3.setText("")
        self.button4.setText("")
        self.button5.setText("")
        self.button6.setText("")
        self.button7.setText("")
        self.button8.setText("")
        self.button9.setText("")
        self.button10.setText("")
        self.button11.setText("")
        self.button12.setText("")
        self.button13.setText("")
        self.button14.setText("")
        self.button15.setText("")
        self.button16.setText("")
        self.button17.setText("")
        self.button18.setText("")
        self.button19.setText("")
        self.button20.setText("")
        self.button21.setText("")
        self.button22.setText("")
        self.button23.setText("")
        self.button24.setText("")
        self.button25.setText("")

        self.button1.setStyleSheet("")
        self.button2.setStyleSheet("")
        self.button3.setStyleSheet("")
        self.button4.setStyleSheet("")
        self.button5.setStyleSheet("")
        self.button6.setStyleSheet("")
        self.button7.setStyleSheet("")
        self.button8.setStyleSheet("")
        self.button9.setStyleSheet("")
        self.button10.setStyleSheet("")
        self.button11.setStyleSheet("")
        self.button12.setStyleSheet("")
        self.button13.setStyleSheet("")
        self.button14.setStyleSheet("")
        self.button15.setStyleSheet("")
        self.button16.setStyleSheet("")
        self.button17.setStyleSheet("")
        self.button18.setStyleSheet("")
        self.button19.setStyleSheet("")
        self.button20.setStyleSheet("")
        self.button21.setStyleSheet("")
        self.button22.setStyleSheet("")
        self.button23.setStyleSheet("")
        self.button24.setStyleSheet("")
        self.button25.setStyleSheet("")

        self.button1.setEnabled(True)
        self.button2.setEnabled(True)
        self.button3.setEnabled(True)
        self.button4.setEnabled(True)
        self.button5.setEnabled(True)
        self.button6.setEnabled(True)
        self.button7.setEnabled(True)
        self.button8.setEnabled(True)
        self.button9.setEnabled(True)
        self.button10.setEnabled(True)
        self.button11.setEnabled(True)
        self.button12.setEnabled(True)
        self.button13.setEnabled(True)
        self.button14.setEnabled(True)
        self.button15.setEnabled(True)
        self.button16.setEnabled(True)
        self.button17.setEnabled(True)
        self.button18.setEnabled(True)
        self.button19.setEnabled(True)
        self.button20.setEnabled(True)
        self.button21.setEnabled(True)
        self.button22.setEnabled(True)
        self.button23.setEnabled(True)
        self.button24.setEnabled(True)
        self.button25.setEnabled(True)

        self.label.setText("Player 1's Turn (X)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    sys.exit(app.exec_())
