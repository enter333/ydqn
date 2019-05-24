from pywinauto.application import Application
from PIL import Image
from pywinauto import win32structures
import os

class imgproc():
    def __init__(self):
        self.nowdir = os.getcwd()
    
    def capture(cls):
        im = self.dlg.capture_as_image()
        im.save("{}\\temp\\main.png".format(self.nowdir))
        i = 0
        for c in self.dlg.children():
            i = i + 1
            im = c.capture_as_image()
            im.save("{}\\temp\\{}.png".format(self.nowdir,i))
            if im == None:
                continue
            for d in c.children():
                try:
                    i = i + 1
                    im = d.capture_as_image()
                    if im == None:
                        continue
                    im.save("{}\\temp\\{}.png".format(self.nowdir,i))
                    print(d.class_name())

                    for e in d.children():
                        i = i + 1
                        im = e.capture_as_image()
                        print(type(e))
                        if im == None:
                            continue
                        im.save("{}\\temp\\{}.png".format(self.nowdir,i))
                        
                except:
                    continue


    
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

if __name__ == '__main__':
    cap = imgproc()
    cap.getpid("Fysw.atd")
    #cap.getpid("taskmgr.exe")
    cap.linkprocess()
    cap.capture()

