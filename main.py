from PyQt5.QtWidgets import  QWidget, QPushButton, QLabel, QGridLayout, QAction, qApp, QMainWindow
from PyQt5.QtCore import pyqtSlot
from logic import Logic

class Main(QMainWindow):

    def __init__(self,w):
        super().__init__()
        
        self.initUI(w)
    
    def initUI(self,w):
    
        self.setWindowTitle("work1")
        
        exitAction = QAction('&退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        
        self.setAction = QAction('&设置', self)
        
        self.helpAction = QAction('&帮助', self)
        self.helpAction.setShortcut('Ctrl+H')
        
        self.saveAction = QAction('&保存', self)
        self.saveAction.setShortcut('Ctrl+S')
        
        menubar = self.menuBar()
        
        fileMenu1 = menubar.addMenu('&文件')
        fileMenu1.addAction(exitAction)
        fileMenu1.addAction(self.saveAction)
        
        fileMenu2 = menubar.addMenu('&设置')
        fileMenu2.addAction(self.setAction)
        
        fileMenu3 = menubar.addMenu('&帮助')
        fileMenu3.addAction(self.helpAction)
        
        self.setCentralWidget(w)
        
        self.setGeometry(0, 30, 1080, 960)    
        
        self.showFullScreen()
            
        
class Content(QWidget):
    
    html_ls=["","","","","","","","","","","","",]
    label=[]
    
    def __init__(self):
        super().__init__()

        self.initUI()
        
        self.logic=Logic()
        
        
    def initUI(self):
        html_head= "<h1 style=\"text-align:center;\">四则运算出题器</h1>"
        html_sub1= "<h3 style=\"text-align:center;\">题目</h3>"
        html_sub2= "<h3 style=\"text-align:center;\">答案</h3>"
        
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        
        label1.setText(html_head)
        label2.setText(html_sub1)
        label3.setText(html_sub2)
        
        for i in range(0,11):
            label_temp=QLabel(self)
            self.label.append(label_temp)
        
        self.btn1 = QPushButton('Creat!', self)
        self.btn1.clicked.connect(self.setLs)
        
        grid = QGridLayout()
        grid.setSpacing(1)
        grid.addWidget(label1,1,1,1,12)
        grid.addWidget(label2,2,1,1,6)
        grid.addWidget(label3,2,7,1,6)
        for i in range(0,11):
            grid.addWidget(self.label[i],3,i+1,20,1)
        grid.addWidget(self.btn1,22,6,22,2)
        self.setLayout(grid)
             
    def setLs(self):
         
         self.logic.creat()
         
         for i in range(0,11):
            self.html_ls[i]=self.logic.get_text(i)
            self.label[i].setText(self.html_ls[i])
         
         for i in range(0,11):
            self.label[i].repaint()
    
    def save(self):
        html=self.logic.get_html()
        f=open("out.html","w")
        f.write(html)
        f.close()
        
    
       
 