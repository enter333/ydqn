from pywinauto.application import Application
from pywinauto import mouse
import time,random
import math
from functools import reduce
import operator
import os
from PIL import Image
from ImgProc import imgproc


class yunduan():
    def __init__(self):
        self.nowdir = os.getcwd()
        self.txdym = Image.open("{}\\temp\\txdym.png".format(self.nowdir))


    def getpid(self,processname):
        # pset = set()
        proc = os.popen('tasklist /NH /FO "csv" /FI "IMAGENAME eq {}"'.format(processname))
        procstrs = proc.read()
        # print(procstrs)
        procl = procstrs.splitlines()
        for l in procl:
            ll = l.split(",")
            self.pid = eval(ll[1])
            # print(self.pid)

    def linkprocess(self):
        self.pid = int(self.pid)
        self.app = Application(backend='uia')
        self.app.connect(process=self.pid)
        self.dlg = self.app.windows()[0]
        print(self.dlg)

    def setcontrol(self):
        for a in self.dlg.children():
            print(a.class_name())
            if a.class_name() == "TFrmBottom":
                self.edt = a.children()[1]
            for b in a.children():
                if b.class_name() == 'TListBox':
                    self.msglistitem = b.children()[2]
                if b.class_name() == "TFrmIcon":
                    self.wu = b


    def openwu(self):
        for a in self.dlg.children():
            print(a.class_name())
            if a.class_name() == "TFrmBottom":
                for b in a.children():
                    if b.class_name() == "TFrmIcon":
                        self.wu = b
                        break
        ## 点击 无 字
        x = self.wu.rectangle().left
        x = x + random.randint(5,20)
        y = self.wu.rectangle().top
        y = y + random.randint(5,20)
        mouse.move(coords=(x,y))
        mouse.click(coords=(x,y))
        print("======")
        for a in self.dlg.children():
            print(a.class_name())
            if a.class_name() == "TFrmFunction":
                self.tab = a
        for b in self.tab.children()[0].children():
            if b.class_name() == "TabControl":
                self.tab = b
            print(b.class_name())
            print(b.print_control_identifiers())
            for c in b.children():
                print(c.class_name())

    def gettab(self):
##        print(self.dlg.TabControl)
        try:
            self.tab = self.dlg.TabControl.wrapper_object()
        except:
            print("not found tab.")
            exit

    def openother(self):
        self.tabchild = self.tab.children()
##        print(len(self.tabchild))
##        for t in self.tabchild:
##            print(t)
        r = self.tab.rectangle().right
        if r < 800:
            x = 0
            y = 0
            ## tab 页面向右滚动按钮
            x = self.tabchild[1].children()[1].rectangle().left
            x = x + 5
            y = self.tabchild[1].children()[1].rectangle().top
            y = y + 5

            ## 点击 5次向右 
            for i in range(5):
                mouse.click(coords=(x,y))
                
            ## ## tab 页面向右滚动按钮，点击 1次向左
            x = self.tabchild[1].children()[0].rectangle().left
            x = x + 5
            y = self.tabchild[1].children()[0].rectangle().top
            y = y + 5
            mouse.click(coords=(x,y))

            # 点击 关于 
            x = self.tabchild[6].rectangle().left
            x = x + 5
            y = self.tabchild[6].rectangle().top
            y = y + 5
            mouse.click(coords=(x,y))

            ## 点击 配置
            x = self.tabchild[5].rectangle().left
            x = x + 5
            y = self.tabchild[5].rectangle().top
            y = y + 5
            mouse.click(coords=(x,y))
##            print(len(self.tabchild))
##            for t in self.tabchild:
##                print(t)

    def setkillctrl(self):
        self.othera = self.tabchild[0].children()[0]
        cl = self.othera.children()
        self.huticb = cl[0]
        self.point = cl[2]
        self.pointlist = cl[3]
        self.monster = cl[4]
        self.monsterlist = cl[5]
        self.autokillcb = cl[6]
        self.killset = cl[7]

        

    def startkill(self):
        killstatus = self.autokillcb.get_toggle_state()
        if killstatus == 0 :
            self.autokillcb.click()
##            print(self.autokillcb.get_toggle_state())

    def stopkill(self):
        killstatus = self.autokillcb.get_toggle_state()
        if killstatus == 1 :
            self.autokillcb.click()
##            print(self.autokillcb.get_toggle_state())

    def openkillset(self):
        setstr = self.killset.texts()
        if setstr[0] == "配置->":
            self.killset.click()
            
    def closekillset(self):
        setstr = self.killset.texts()
        if setstr[0] == "配置<-":
            self.killset.click()

    def addmonster(self,monster):
        self.monster.set_edit_text(monster)
        self.monster.type_keys("{ENTER}")

    def addpoint(self,point):
        self.point.set_edit_text(point)
        self.point.type_keys("{ENTER}")


    def clearpoint(self):
        listitems = self.pointlist.get_items()
        x = listitems[0].rectangle().left
        x = x + 5
        y = listitems[0].rectangle().top
        y = y + 5
        for i in range(len(listitems)):
            mouse.double_click(coords=(x,y))

    def clearmonster(self):
        listitems = self.monsterlist.get_items()
        x = listitems[0].rectangle().left
        x = x + 5
        y = listitems[0].rectangle().top
        y= y + 5
        for i in range(3):
            mouse.double_click(coords=(x,y))
            

    def _compareimage(self,firstImage, secondImage ):
            """
            return the two image's different value  
            """
            "Calculate the root-mean-square difference between two images"
            h1 = firstImage.histogram ()
            h2 = secondImage.histogram ()
            rms = math.sqrt (reduce(operator.add, map ( lambda a, b: ( a - b ) ** 2, h1, h2 ) ) / len( h1 ))
##            print( {'图片比较':'图片【%s】和图片【%s】比较的差值为【%s】' % ( str( firstImage ), str( secondImage ), str( rms ) )} )
            return rms

    def _get_area_image(self):
        for a in self.dlg.children():
            if a.class_name() == 'TFrmBottom':
                self.edt = a.children()[1]
                for i in range(2):
                    self.edt.set_edit_text("/where")
                    time.sleep(1)
                    self.edt.type_keys("{ENTER}")
                for b in a.children():
                    if b.class_name() == 'TListBox':
                        self.msglistitem = b.children()[2]
                        self.area = self.msglistitem.capture_as_image()

    def compareimage(self):
        self.area = self.msglistitem.capture_as_image()
##        self.area = Image.open("{}\\temp\\txdym.png".format(self.nowdir))
        return self._compareimage(self.area,self.txdym)


if __name__ == "__main__":
    yd = yunduan()
    yd.getpid("Fysw.atd")
    yd.linkprocess()
    yd._get_area_image()
    print(round(yd.compareimage(),0))
    if (round(yd.compareimage(),0)) > 1 :
        print("ccyn")
    else:
        print("txdym")

##    yd.openwu()
##    yd.gettab()
##    yd.openother()
##    yd.setkillctrl()
##    yd.openkillset()
##    time.sleep(2)
##    yd.closekillset()
##    yd.startkill()
##    yd.clearpoint()
##    yd.addpoint()
##    yd.clearmonster()
##    yd.addmonster()
    


