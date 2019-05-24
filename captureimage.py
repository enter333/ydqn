from pywinauto.application import Application
from PIL import Image
from PIL import ImageGrab
from pywinauto import win32structures
import pytesseract
import os

class ocrdemo():
    def __init__(self):
        nowdir = os.getcwd()
        self.pngfile = '{}\\screen.png'.format(nowdir)
        self.tempimg = '{}\\temp.png'.format(nowdir)
    
    def runexe(self):
        self.app = Application(backend='uia').start("C:\\Users\\Administrator\\Documents\\other\\PuTTY_0.67.0.0.exe")
        self.dlg_uia = self.app.window()
        self.btn = self.dlg_uia.Edit.wrapper_object()
        ## 使用ImageGrab.grab方法截图
        rect = self.btn.rectangle()
        im2 = ImageGrab.grab((rect.left,rect.top,rect.right,rect.bottom))
        im2.save("C:\\Users\\Administrator\\Documents\\other\\save.jpeg","jpeg")

        ## 使用控件截图方法
        im3 = self.btn.capture_as_image()
        im3.save("C:\\Users\\Administrator\\Documents\\other\\saveim3.bmp","bmp")

    def ocrimg(self):
        ## 识别图片返回文字lang = 'eng' 英文，lang='chi_sim' 中文  config= '-psm 7' 识别一行
        file = 'C:\\Users\\Administrator\\Documents\\other\\saveim3.bmp'
        code = pytesseract.image_to_string(file, lang="eng", config='-psm 7')
        print(code)
    
    def _get_skills_image(self):
        im = Image.open(self.pngfile)
        left = 22
        top = 56
        h = 48
        w = 68
        right = left + w
        bottom = top + h
        size = (left ,top ,right ,bottom)
        self._skillimage = im.crop(size)
        # self._skillimage.show()

    def get_skills(self):
        self._get_skills_image()
        fontheight = 12
        fontweight = 68
        for n in range(3):
            size1 = (0,n * fontheight,fontweight,fontheight * (n+1))
            skill_1 = self._skillimage.crop(size1)
            skill_1.save(self.tempimg)
            code = self._ocrzhcnimg()
            # print(code)

    def _get_pos_image(self):
        im = Image.open(self.pngfile)
        left = 58
        top = 117
        h = 11
        w = 41
        right = left + w
        bottom = top + h
        size = (left ,top ,right ,bottom)
        self._posimage = im.crop(size)
        # self._posimage = self._posimage.resize((self._posimage.size[0] * 2,self._posimage.size[1] * 2))
        # self._posimage.show()
        self._posimage.save(self.tempimg)
        code = self._ocrengimg()
        print(code)


    def get_pos(self):
        self._get_pos_image()
        left,top = 0,0
        h ,w = 12 ,18
        right ,bottom = left + w ,top + h
        size_x = (left,top,right,bottom)
        img_x = self._posimage.crop(size_x)
        # img_x.show()
        # img_x.save(self.tempimg)
        x = self._ocrengimg()

        left ,top = 24 ,0
        right ,bottom = left + w ,top + h
        size_y = (left,top,right,bottom)
        img_y = self._posimage.crop(size_y)
        img_y = img_y.resize((img_y.size[0] * 2,img_y.size[1] * 2))
        # img_y.show()
        img_y.save(self.tempimg)
        y = self._ocrengimg()
        print('{},{}'.format(x,y))

    def _get_msglist_image(self):
        im = Image.open(self.pngfile)
        left = 153
        top = 49
        h = 55
        w = 268
        right = left + w
        bottom = top + h
        size = (left ,top ,right ,bottom)
        self._msglistimage = im.crop(size)
        # self._msglistimage.show()

    def get_msglist(self):
        self._get_msglist_image()
        h = 14
        w = 100

        s1 = (0 ,0 ,w ,h)
        msg = self._msglistimage.crop(s1)
        msg.save(self.tempimg)
        code = self._ocrzhcnimg()
        print(code)

        s2 = (0 ,15 ,w ,28)
        msg = self._msglistimage.crop(s2)
        msg.save(self.tempimg)
        code = self._ocrzhcnimg()
        print(code)

        s3 = (0 ,29 ,w ,43)
        msg = self._msglistimage.crop(s3)
        msg.save(self.tempimg)
        code = self._ocrzhcnimg()
        print(code)

        s4 = (0 ,41 ,w ,60)
        msg = self._msglistimage.crop(s4)
        msg.save(self.tempimg)
        code = self._ocrzhcnimg()
        print(code)
        
    def _ocrzhcnimg(self):
        code = pytesseract.image_to_string(self.tempimg, lang="chi_sim", config='-psm 7')
        return code
    
    def _ocrengimg(self):
        code = pytesseract.image_to_string(self.tempimg, lang="eng", config='-psm 7')
        return code

if __name__ == '__main__':
    ocr = ocrdemo()
    
    # ocr.get_skills()
    
    # ocr.get_pos()
    ocr.get_msglist()