import time
from machine import Pin
from blink import Blink
import machine

machine.freq(80000000)


class Main:
    blink = Blink(1, 50)
    led = Pin(2, Pin.OUT)

    def setup(e):
        pass

    def loop(e):
        if (e.blink.available()):
            e.led.value(e.blink.value())
            e.cout = 0


class Program:
    main = Main()
    D1_input = Pin(5, Pin.IN, Pin.PULL_UP)
    xungReset = Blink(2, 99.99)
    D0_outPut = Pin(16, Pin.OUT)

    def exit(e):
        if (e.xungReset.available()):
            e.D0_outPut.value(e.xungReset.value())
            return e.D1_input.value() == 0

    def run(e):
        print("start program")
        e.main.setup()
        while True:
            e.main.loop()
            if (e.exit()):
                print("end program")
                break


program = Program()
if __name__ == "__main__":
    program.run()

# start = [13,3,3,13,1,4,3,3]
# newline = [13,10]
# end = 4
