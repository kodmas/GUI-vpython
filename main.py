import sys,os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from mainwindow import Ui_MainWindow
from characteristic import Ui_Form
from collision import Ui_Form_collision
from graph import Ui_Form_graph
from floor import Ui_Form_floor

#variables
done = False
characteristc = [1,[300,300,0],2,-10,20,"True"]
data=[]
bounce = False
v_t_draw = False
E_t_draw = False
floor = [500,500]
#mainwindow
class MainWindow(QMainWindow):
    global done
    def __init__(self):
        self.characform = None
        self.colliform = None
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
        self.ui.actioncollision.triggered.connect(self.show_collision_form)
        self.ui.actionoptions.triggered.connect(self.show_graph_form)
        self.ui.actionsettings.triggered.connect(self.show_floor_form)
        #self display button
        self.ui.displaybutton.clicked.connect(self.output_py)
        
        
    #set done
    def browse(self):
        global done
        done = True

    #paintball
    def paintEvent(self,event):
        global characteristc
        if done == True:
            for each in data:
                #print(each)
                curr_pos = each[1][1:-1].split(",")
                #print(curr_pos)
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.green,Qt.SolidPattern))
                painter.drawEllipse(int(curr_pos[0])*10,400-int(curr_pos[1])*10,25*int(each[0]),25*int(each[0]))
                painter.end()
            
            #floor
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QPen(Qt.gray,8,Qt.SolidLine))
            #painter.setBrush(QBrush(Qt.gray,Qt.SolidPattern))
            points = QPolygon([QPoint(400,400),QPoint(400+floor[0],400),QPoint(400+floor[0],400+floor[1]),QPoint(402,400+floor[1])])
            painter.drawPolygon(points)
            painter.end()
    
 


    #show another window
    def show_characteristic_form(self):
        self.characform = characteristc_form()
        self.characform.show()
    
    def show_collision_form(self):
        self.colliform = collision_form()
        self.colliform.show()
    
    def show_graph_form(self):
        self.graform = graph_form()
        self.graform.show()
    
    def show_floor_form(self):
        self.flform = floor_form()
        self.flform.show()


       #Output py file
    def output_py(self):
        self.ball_num=len(data)
        self.pos=MainWindow.listtostr(data,1)
        self.acceleration=MainWindow.listtostr(data,3)
        self.radius=[int(i[0]) for i in data ]
        self.velocity=MainWindow.listtostr(data,2)
        self.mass=[int(i[4]) for i in data]
        self.trail=[True if i[5]=="True" else False for i in data]
        self.bounce=bounce
        #print(v_t_draw)
        self.plot_vt=v_t_draw
        self.plot_et=E_t_draw
        self.text_list[1]=f"g = {self.acceleration}"
        self.text_list[2]=f"size ={self.radius}"
        self.text_list[3]=f"pos ={self.pos}"
        self.text_list[4]=f"v = {self.velocity}"
        self.text_list[5]=f"N={self.ball_num}"
        self.text_list[6]=f"mass={self.mass}"
        self.text_list[7]=f"trail={self.trail}"
        self.text_list[11]=MainWindow.floor_object(floor[0],floor[1]) if self.bounce else ""
        self.text_list[67]=self.text_list[67][1:] if self.bounce else self.text_list[67]
        self.text_list[72]=self.text_list[72][1:] if self.plot_vt else self.text_list[72]
        self.text_list[73]=self.text_list[73][1:] if self.plot_et else self.text_list[73]
        with open("output.py","w") as f:
            for i in self.text_list:
                f.write(i+"\n")
        os.system("python .\output.py")
        sys.exit(app.exec_())

    def floor_object(x,y):
        return f"floor = box(length={x}, height=0.01, width={y}, color=color.blue) # the floor"

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
        global characteristc
        characteristc[0] = self.ui.radius.text()
        characteristc[1] = self.ui.position.text()
        characteristc[2] = self.ui.velocity.text()
        characteristc[3] = self.ui.acceleration.text()
        characteristc[4] = self.ui.mass.text()
        if self.ui.make_Trail.isChecked(): characteristc[5] = "True" 
        else: characteristc[5] = "False"
        data.append(characteristc[:])
        #print(data)
        self.close()
    def dont_load(self):
        self.close()

class collision_form(QDialog):
    global bounce
    def __init__(self):
        super(collision_form,self).__init__()
        self.ui = Ui_Form_collision()
        self.ui.setupUi(self)

        self.ui.retranslateUi(self)

        

        self.ui.buttonBox.accepted.connect(self.ok)
        self.ui.buttonBox.rejected.connect(self.cancel)
    
    def ok(self):
        global bounce
        if self.ui.ball_collision.isChecked():
            bounce = True
        self.close()
    def cancel(self):
        self.close()

class graph_form(QDialog):
    def __init__(self):
        super(graph_form,self).__init__()
        self.ui = Ui_Form_graph()
        self.ui.setupUi(self)

        self.ui.retranslateUi(self)

        

        self.ui.buttonBox.accepted.connect(self.ok)
        self.ui.buttonBox.rejected.connect(self.cancel)
    
    def ok(self):
        global v_t_draw,E_t_draw
        if self.ui.v_tgraph.isChecked():
            v_t_draw = True
        if self.ui.E_tgraph.isChecked():
            E_t_draw = True
        self.close()
    def cancel(self):
        self.close() 

class floor_form(QDialog):
    def __init__(self):
        super(floor_form,self).__init__()
        self.ui = Ui_Form_floor()
        self.ui.setupUi(self)

        self.ui.retranslateUi(self)

        

        self.ui.buttonBox.accepted.connect(self.ok)
        self.ui.buttonBox.rejected.connect(self.cancel)
    
    def ok(self):
        global floor
        floor[0] = int(self.ui.width.text())
        floor[1] = int(self.ui.length.text())
        self.close()
    def cancel(self):
        self.close() 


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
