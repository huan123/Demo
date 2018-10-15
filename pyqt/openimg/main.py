import sys
sys.path.append('/Users/huan/code/pythondemo/pyqt/openimg')
from PyQt5.QtWidgets import QApplication
from pyqt.openimg.dumbDialog import DumbDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dia = DumbDialog()
    dia.show()
    app.exec_()