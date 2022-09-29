import time


class Blink:
    _begin = 0
    _val = 0
    _hight = 0
    _low = 0
    _tong = 0
    def __init__(e, hz: float = 1, duty: float = 50) -> None:
        e._tong = 1000/hz
        e._hight = (duty/100)*e._tong
        e._low = e._tong - e._hight

    def setting(e, hz: float = -1, duty: float = -1) -> None:
        if hz != -1:
            e._tong = 1000/hz
        if duty != -1:
            e._hight = (duty/100)*tong
            e._low = tong = e._hight

    def value(e, togle: int = 1) -> int:
        if togle == 1:
            return e._val
        else:
            if e._val == 0:
                return 1
            else:
                return 0

    def available(e) -> bool:
        now = time.ticks_ms()
        error = now - e._begin
        if (e._val == 0):
            islow = error > e._low
            if islow:
                e._begin = now
                e._val = 1
            return islow
        else:
            ishight = error > e._hight
            if ishight:
                e._begin = now
                e._val = 0
            return ishight
