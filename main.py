import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        func = self.funcInput.text()
        min_b = self.minInput.value()
        max_b = self.maxInput.value()
        x = []
        y = []
        for i in range(min_b, max_b + 1):
            try:
                y.append(eval(func.replace('x', '(' + str(i) + ')').replace('^', '**')))
                x.append(i)
            except Exception:
                pass
        self.widget.clear()
        self.widget.plot(x, y, pen='r')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
