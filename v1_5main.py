import sys,os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from v1_5mainwindow import Ui_MainWindow
from characteristc import Ui_Form


#variables
done = False
characteristc = [1,[300,300,0],2,-10]
data=[]
#mainwindow
class MainWindow(QMainWindow):
    global done
    def __init__(self):
        self.characform = None
        #py text list
        with open("default.py","r") as r:
            self.raw_text=r.read()
            self.text_list=self.raw_text.split("\n")

        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.title = 'vpython'

        #menu
        self.ui.retranslateUi(self)
        self.ui.actioncreate.triggered.connect(self.show_characteristic_form)
        self.ui.actionbrowse.triggered.connect(self.browse)
        
        #self display button
        self.ui.displaybutton.clicked.connect(self.output_py)
        
        
    #set done
    def browse(self):
        global done
        done = True

    #painter
    def paintEvent(self,event):
        global characteristc
        if done == True:
            for each in data:
                curr_pos = each[1][1:6].split(",")
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
                painter.drawEllipse(int(curr_pos[0]),int(curr_pos[1]),10*int(each[0]),10*int(each[0]))
                painter.end()

    #show
    def show_characteristic_form(self):
        self.characform = characteristc_form()
        self.characform.show()
    #Output py file
    def output_py(self):
        self.ball_num=len(data)
        self.pos=MainWindow.listtostr(data,1)
        self.acceleration=MainWindow.listtostr(data,3)
        self.radius=[int(i[0]) for i in data ]
        self.velocity=MainWindow.listtostr(data,2)
        self.text_list[1]=f"g = {self.acceleration}"
        self.text_list[2]=f"size ={self.radius}"
        self.text_list[3]=f"pos ={self.pos}"
        self.text_list[4]=f"v = {self.velocity}"
        self.text_list[5]=f"N={self.ball_num}"
        with open("output.py","w") as f:
            for i in self.text_list:
                f.write(i+"\n")
        os.system("python .\output.py")
        sys.exit(app.exec_())
    def listtostr(A,n):
        ans="["
        for i in A[:-1]:
            ans+="vec"+ str(i[n])+","
        ans+="vec"+ str(A[-1][n])+"]"
        return ans

#form
class characteristc_form(QDialog):
    global characteristc
    global data
    def __init__(self):
        super(characteristc_form,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.retranslateUi(self)
        self.ui.buttonBox.accepted.connect(self.load_data)
        self.ui.buttonBox.rejected.connect(self.dont_load)
    #ok clicked -> load data to data_list
    def load_data(self):
        characteristc[0] = self.ui.radius.text()
        characteristc[1] = self.ui.position.text()
        characteristc[2] = self.ui.velocity.text()
        characteristc[3] = self.ui.acceleration.text()
        data.append(characteristc[:])
        #print(data)
        self.close()
    def dont_load(self):
        self.close()

         



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())