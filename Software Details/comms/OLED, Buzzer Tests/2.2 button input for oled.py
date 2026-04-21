from machine import Pin
import machine, ssd1306
import framebuf
import time

pb1 = Pin(14, Pin.IN, Pin.PULL_UP)
i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    val = pb1.value()
    if val == 0:
        display.fill(0)
        display.text('PLAYER 1', 33, 4)
        display.text('SUCCESS!!! ', 2, 20)
        display.show()
        time.sleep(2)
    else:
        display.fill(0)
        display.text('PLAYER 1', 33, 4)
        display.text('Nothing yet.', 2, 20)
        display.show()
        time.sleep(0.1)
