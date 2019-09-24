from PyQt5.QtWidgets import QWidget,  QLabel, QGridLayout

class Help(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("帮助")
        
        grid = QGridLayout()
        grid.setSpacing(1)
        
        label=QLabel(self)
        head= "<h1 style=\"text-align:center;\">帮助</h1>"
        label.setText(head)
        grid.addWidget(label,1,1,1,1)
        
        label1=QLabel(self)
        body= "<p>使用方法</p><p>可以在设置中更改除法类型和算数中出现的最大值，每次可以生成300道题目，可以选择保存为已排版的html格式文件，可以直接打印。（注意，每次都会覆盖掉上一次生成结果）</p><p>祝您的学生每天都写得开心！</p>"
        label.setText(body)
        grid.addWidget(label1,2,1,1,1)
        
        self.setLayout(grid)