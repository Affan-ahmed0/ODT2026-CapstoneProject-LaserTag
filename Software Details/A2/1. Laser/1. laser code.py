from machine import Pin
import machine, ssd1306
import framebuf
import time
import screen
import asyncio

i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

lz = Pin(25, Pin.OUT)
ldr = Pin(15, Pin.IN, Pin.PULL_UP)
pb = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    if pb.value() == 0:
        lz.on()
        asyncio.sleep(0.2)
        asyncio.run(screen.stats())
        
        if ldr.value() == 0:
            asyncio.run(screen.hit())