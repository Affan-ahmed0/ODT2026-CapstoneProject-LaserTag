from machine import Pin
import machine, ssd1306
import framebuf
import time

i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)
display.text("LINE TESTING.", 0, 0)
display.text("LINE TESTING.", 0, 16)
display.text("LINE TESTING.", 0, 26)
display.text("LINE TESTING.", 0, 36)
display.text("LINE TESTING.", 0, 46)
display.text("LINE TESTING.", 0, 56)
display.show()
time.sleep(1)

# I have one yellow header line and 5 normal blue lines

display.fill(0)
display.text("XXXXXXXXXXXXXXX0)", 0, 0)
display.show()
time.sleep(1)

# AND I HAVE 16 CHARACTER SPACES ON ONE SCREEN, AND 128 P

display.fill(0)
display.text("1+5 LINES.", 3, 16)
display.text("16 SPACES.", 0, 26)
display.text("6p each char.", 0, 36)
display.text("2p each char space", 0, 46)
display.text("6p each word space", 0, 56)
display.show()