from machine import Pin
import machine, ssd1306
import framebuf
import time

i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)
display.text('hello there :)', 0, 0)
display.show()

time.sleep(1)
display.text("what's ur name?", 0, 20)
display.show()

time.sleep(1)
display.text("type it out!", 0, 40)
display.show()

time.sleep(0.5)
print("here: ")
name = input()

time.sleep(3)
display.fill(0)
display.text(f"hi {name}! <3", 0, 0)
display.show()

time.sleep(3)
display.fill(0)
