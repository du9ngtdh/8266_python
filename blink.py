import time
# start = [13,3,3,13,1,4,3,3]
# newline = [13,10]
# end = 4
class Blink:
    _begin = 0
    _value = 0
    _hight = 0
    _low = 0
    def __init__(e, hz: float = 1, duty: float = 50) -> None:
        e.tong = 1000/hz
        e._hight = duty/100*e.tong
        e._low = e.tong - e._hight

    def setting(self,hz:float =-1,duty:float =-1):
        if(hz != -1):
            self.tong = 1000/hz
        self._hight = (duty/100)*self._hight
        self._low = self.tong - self._hight
        
    
    def value(e) -> int:
        return e._value

    def available(e) -> bool:
        now = time.ticks_ms()
        error = now - e._begin
        if (e._value == 0):
            islow = error > e._low
            if islow:
                e._begin = now
                e._value = 1
            return islow
        else:
            ishight = error > e._hight
            if ishight:
                e._begin = now
                e._value = 0
            return ishight
