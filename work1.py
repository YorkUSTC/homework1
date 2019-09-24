import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot
from main import Content, Main
from Set import SetWindow
from logic import Logic
from help import Help
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w=Content()
    setwindow=SetWindow()
    main = Main(w)
    help=Help()
    
    main.setAction.triggered.connect(setwindow.show)
    main.helpAction.triggered.connect(help.show)
    main.saveAction.triggered.connect(w.save)
    
    setwindow.btn3.clicked.connect(lambda: w.logic.set_max(setwindow.max))
    setwindow.btn3.clicked.connect(lambda: w.logic.set_kind(setwindow.kind))
    sys.exit(app.exec_())
