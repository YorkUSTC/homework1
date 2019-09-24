from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QLineEdit, QInputDialog
class SetWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        self.max=10
        self.kind="带余除法"
        
    def initUI(self):
        self.setWindowTitle("设置")
        self.resize(320,120)
        
        grid = QGridLayout()
        grid.setSpacing(1)
        
        label=QLabel(self)
        head= "<h1 style=\"text-align:center;\">设置</h1>"
        label.setText(head)
        grid.addWidget(label,1,1,1,3)
        
        label1=QLabel(self)
        label1.setText("算数最大值")
        grid.addWidget(label1,2,1,1,1)
        
        self.label3=QLabel(self)
        self.label3.setText(str(10))
        grid.addWidget(self.label3,2,2,1,1)
        
        self.btn1=QPushButton("设置")
        self.btn1.clicked.connect(self.getInt)
        grid.addWidget(self.btn1,2,3,1,1)
        
        label2=QLabel(self)
        label2.setText("除法类型")
        grid.addWidget(label2,3,1,1,1)
        
        self.label4=QLabel(self)
        self.label4.setText("带余除法")
        grid.addWidget(self.label4,3,2,1,1)
        
        self.btn2=QPushButton("设置")
        self.btn2.clicked.connect(self.getItem)
        grid.addWidget(self.btn2,3,3,1,1)
        
        self.btn3=QPushButton("确认")
        grid.addWidget(self.btn3,4,2,1,1)

        self.setLayout(grid)
        
    def getInt(self):
        num,ok=QInputDialog.getInt(self,"设置算数最大值",'请输入数字')
        if ok:
            self.label3.setText(str(num))
            self.label3.update()
            self.max=num
    
    def getItem(self):
        items=("带余除法","分数除法")
        item,ok=QInputDialog.getItem(self,"设置除法类型","除法类型",items,0,False)
        if ok and item:
            self.label4.setText(item)
            self.label4.update()
            self.kind=item