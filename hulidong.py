import ydqn
import time

def init():
    yd = ydqn.yunduan()
    yd.getpid("Fysw.atd")
    yd.linkprocess()
    yd.setcontrol()
    yd._get_area_image()
    yd.openwu()
    yd.gettab()
    yd.openother()
    yd.setkillctrl()
    return yd
    
def set_ccyn_ddr(yd):
    yd.openkillset()
    yd.stopkill()
    yd.clearpoint()
    
    yd.addpoint("29,109")

    yd.clearmonster()
    yd.addmonster("挑点")

    yd.startkill()

    yd.closekillset()

def set_huli_addr(yd):
    yd.openkillset()
    yd.stopkill()
    yd.clearpoint()
    
    yd.addpoint("129,157")
    yd.addpoint("150,162")
    yd.addpoint("162,139")

    yd.clearmonster()
    yd.addmonster("白")

    yd.startkill()
    yd.closekillset()

def where(yd):
    if (round(yd.compareimage(),0)) > 1 :
        return "ccyn"
    else:
        return "txdym"
        
        
if __name__ == "__main__":
    yd = init()
    ccyn_n = 0
    hld_n = 0
    for i in range(20):
        if where(yd) == 'ccyn':
            if ccyn_n == 0 :
                  set_ccyn_ddr(yd)
                  ccyn_n = 1
                  hld_n = 0
        else:
            if hld_n == 0:
                  set_huli_addr(yd)
                  hld_n = 1
                  ccyn_n = 0
        time.sleep(30)
