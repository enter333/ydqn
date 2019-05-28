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
        # self.func 挂对话框
        self.func = None  
        self.nowdir = os.getcwd()
        self.hld = Image.open("{}\\temp\\hld.png".format(self.nowdir))


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
##            print(a.class_name())
            if a.class_name() == "TFrmBottom":
                self.edt = a.children()[1]
            for b in a.children():
                if b.class_name() == 'TListBox':
                    self.msglistitem = b.children()[2]
##                    im = self.msglistitem.capture_as_image()
##                    im.save("{}\\temp\\hld.png".format(self.nowdir))
                if b.class_name() == "TFrmIcon":
                    self.wu = b

    def openwu(self):
        if self.wu == None:
            print("wu is None")
            return
        '''
        查找弹出的对话框
        '''
        winlist = {}
        for a in self.dlg.children():
            winlist[a.class_name()] = a
        if "TFrmFunction" in winlist.keys():
            self.func = winlist["TFrmFunction"]
        else:
            # 如果窗口没有显示，就点击无字
            x = self.wu.rectangle().left
            x = x + random.randint(5,20)
            y = self.wu.rectangle().top
            y = y + random.randint(5,20)
            mouse.move(coords=(x,y))
            mouse.click(coords=(x,y))
##            print("======")
            for a in self.dlg.children():
                if a.class_name() == "TFrmFunction":
                    self.func = a
                    break
        # tab标签页
        for b in self.func.children()[0].children():
            if b.class_name() == "TPageControl":
                self.tab = b
##                print("self.tab:",self.tab.class_name())
            for c in self.tab.children():
##                print("c=",c.texts())
                if c.class_name() == "msctls_updown32":
                    self.d = c

                    x = self.d.rectangle().left
                    x = x + random.randint(5,10)
                    y = self.d.rectangle().top
                    y = y + random.randint(5,10)
                    mouse.move(coords=(x,y))
                    mouse.click(coords=(x,y))
                    mouse.click(coords=(x,y))
                    
                    x = self.d.rectangle().left
                    x = x + random.randint(5,10) + 20
                    y = self.d.rectangle().top
                    y = y + random.randint(5,10)
                    mouse.move(coords=(x,y))
                    mouse.click(coords=(x,y))
                    mouse.click(coords=(x,y))
                    
                if c.texts()[0] == "其他":
                    self.qita = c
##                    print("qita=",self.qita.texts())
                    x = self.qita.rectangle().left
                    x = x + random.randint(5,10)
                    y = self.qita.rectangle().top
                    y = y + random.randint(5,10)
                    mouse.move(coords=(x,y))
                    mouse.click(coords=(x,y))
        for a in self.tab.children():
            for b in a.children():
##                print(b.class_name())
                if b.class_name() == "TGroupBox":
                    for c in b.children():
##                        print(c.class_name())
##                        print(c.texts())
                        if c.class_name() == "TButton":
                            self.killset = c
                        if c.texts()[0] == "自动杀怪":
                            self.autokillcb = c
                    cl = b.children()
                    self.huticb = cl[0]
                    self.point = cl[2]
                    self.pointlist = cl[3]
                    self.monster = cl[4]
                    self.monsterlist = cl[5]
                    self.autokillcb = cl[6]
        

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
        for i in range(2):
            time.sleep(1)
            self.edt.set_edit_text("/where")
            self.edt.type_keys("{ENTER}")
        self.area = self.msglistitem.capture_as_image()

    def compareimage(self):
        # self.area = Image.open("{}\\temp\\ccyn.png".format(self.nowdir))
        # self.hld = Image.open("{}\\temp\\hld.png".format(self.nowdir))
        self._get_area_image()
        sz = self.area.size
        self.areacut = self.area.crop((36,0,sz[0],sz[1]))
        # self.areacut.show()
        sz = self.hld.size
        self.hldcut = self.hld.crop((36,0,sz[0],sz[1]))
        # self.hldcut.show()
        return self._compareimage(self.areacut,self.hldcut)


if __name__ == "__main__":
    yd = yunduan()
    # yd.getpid("Fysw.atd")
    # yd.linkprocess()
    # yd.setcontrol()
    # yd.openwu()
    # yd.openkillset()
    imgret = yd.compareimage()
    print(imgret)
    if round(imgret*10,0) > 1 :
        print("ccyn")
    else:
        print("hld")

##    yd.openwu()
##    yd.gettab()
##    yd.openother()
##    yd.setkillctrl()
##    
##    time.sleep(2)
##    yd.closekillset()
##    yd.startkill()
##    yd.clearpoint()
##    yd.addpoint()
##    yd.clearmonster()
##    yd.addmonster()
    


