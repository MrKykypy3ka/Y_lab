from PyQt6 import uic, QtWidgets
from Form import Ui_Dialog
from PyQt6.QtWidgets import QPushButton
from TicTacToe import TicTacToe
from Player import Player
import sys

Form, Window = uic.loadUiType("form.ui")


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        for btn in self.ui.groupBox.findChildren(QPushButton):
            btn.clicked.connect(self.buttonPresed)

    def buttonPresed(self):
        self.sender().setEnabled(False)
        btn = self.sender().objectName()
        temp = str(int(btn.split('_')[1]) - 1)
        s = '0' + temp if len(temp) == 1 else temp
        figure = game.add_position(int(s[0]), int(s[1]), player1)
        self.sender().setText(figure[0])
        self.end(figure[1])
        if type(figure[1]) is not tuple:
            self.draw()

    def draw(self):
        n, m = game.opponent_move()
        temp = game.add_position(n, m, player2)
        s = str(int(str(n) + str(m)) + 1)
        for pqbutton in self.ui.groupBox.findChildren(QPushButton):
            if pqbutton.objectName() == 'pushButton_' + s:
                pqbutton.setText(temp[0])
                pqbutton.setEnabled(False)
        self.end(temp[1])

    def end(self, res):
        if res == 'Ничья':
            return print(res)
        if res != 0:
            for i in range(len(res[1])):
                temp = str(int(str(res[1][i][0]) + str(res[1][i][1])) + 1)
                res[1][i] = 'pushButton_' + temp
            for pqbutton in self.ui.groupBox.findChildren(QPushButton):
                pqbutton.setEnabled(False)
                if pqbutton.objectName() in res[1]:
                    font = pqbutton.font()
                    font.setBold(True)
                    font.setItalic(True)
                    pqbutton.setFont(font)
            print(res[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    player1 = Player('human', 'X')
    player2 = Player('computer', 'O')
    game = TicTacToe('hard', player1, player2)
    sys.exit(app.exec())
