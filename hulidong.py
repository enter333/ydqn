import ydqn
import time

def init():
    yd = ydqn.yunduan()
    yd.getpid("Fysw.atd")
    yd.linkprocess()
    yd.setcontrol()
    yd.openwu()
    yd.openkillset()
    return yd
    
def set_ccyn_ddr(yd):
    yd.openkillset()
    yd.stopkill()
    yd.clearpoint()
    
    yd.addpoint("141,265")

    yd.clearmonster()
    yd.addmonster("挑点")

    yd.startkill()

    yd.closekillset()

def set_huli_addr(yd):
    yd.openkillset()
    yd.stopkill()
    yd.clearpoint()
    
    yd.addpoint("52,95")
    yd.addpoint("61,61")
    yd.addpoint("118,30")
    yd.addpoint("140,103")
    yd.addpoint("112,116")

    yd.clearmonster()
    yd.addmonster("白")

    yd.startkill()
    yd.closekillset()

def where(yd):
    imgret = yd.compareimage()
    if round(imgret*10,0) > 1 :
        return "ccyn"
    else:
        return "hld"
        
        
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
