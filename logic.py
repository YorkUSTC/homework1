import random
class Logic:

    text=["","","","","","","","","","","",""]
    
    def gcd(self,b,a):
        b,a=a,b%a
        if a==0:
            return b
        else:
            return self.gcd(b,a)
    
    def __init__(self):
        self.max=10
        
        self.kind="带余除法"
        
        self.creat()
        
    def set_max(self,max):
        self.max=max
    
    def set_kind(self,kind):
        self.kind=kind
    
    def creat(self):
        for i in range(0,6):
            self.text[i]="<ul>"
            self.text[i+6]="<ul>"
        
            for j in range(0,50):
                num1=random.randint(1,self.max)
                num2=random.randint(1,self.max)
                signal=random.randint(0,3)
                if(signal==0):
                    num3=num1+num2
                    self.text[i]=self.text[i]+"<li>"+str(num1)+"+"+str(num2)+"=?</li>"
                    self.text[i+6]=self.text[i+6]+"<li>"+str(num3)+"</li>"
                elif(signal==1):
                    num3=num1-num2
                    self.text[i]=self.text[i]+"<li>"+str(num1)+"-"+str(num2)+"=?</li>"
                    self.text[i+6]=self.text[i+6]+"<li>"+str(num3)+"</li>"
                elif(signal==2):
                    num3=num1*num2
                    self.text[i]=self.text[i]+"<li>"+str(num1)+"*"+str(num2)+"=?</li>"
                    self.text[i+6]=self.text[i+6]+"<li>"+str(num3)+"</li>"
                elif(signal==3):
                    self.text[i]=self.text[i]+"<li>"+str(num1)+"/"+str(num2)+"=?</li>"
                    if(self.kind=="带余除法"):
                        num3=num1//num2
                        num4=num1%num2
                        
                        self.text[i+6]=self.text[i+6]+"<li>"+str(num3)+"......"+str(num4)+"</li>"
                    
                    elif(self.kind=="分数除法"):
                        gcd=self.gcd(num1,num2)
                        num3=num1//gcd
                        num4=num2//gcd
                        
                        self.text[i+6]=self.text[i+6]+"<li>"+str(num3)+"/"+str(num4)+"</li>"

            self.text[i]=self.text[i]+"</ul>"
            self.text[i+6]=self.text[i+6]+"</ul>"
            
    def get_html(self):
            
        self.html="<!DOCTYPE html><html><head><title>题目</title></head><body><h1>题目</h1>"
        for i in range(0,6):
            self.html=self.html+self.text[i]
        self.html=self.html+"<h1>答案</h1>"
        for i in range(6,12):
            self.html=self.html+self.text[i]
        self.html=self.html+"</body></html>"
        return self.html
        
    def get_text(self,i):
        return self.text[i]
