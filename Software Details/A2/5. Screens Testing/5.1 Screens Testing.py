from machine import Pin, I2C
import machine, ssd1306
import framebuf
import time
import screen
import asyncio

i2c = I2C(scl=Pin(19), sda=Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# GENERAL TESTING

asyncio.run(screen.welcome())
asyncio.run(screen.getready())
asyncio.run(screen.countdown())
asyncio.run(screen.scan())
asyncio.run(screen.stats())
time.sleep(2)
asyncio.run(screen.hit())
asyncio.run(screen.stats())
time.sleep(2)
asyncio.run(screen.miss())
asyncio.run(screen.stats())
time.sleep(2)
asyncio.run(screen.life())
asyncio.run(screen.stats())
time.sleep(2)
asyncio.run(screen.cooldown())
asyncio.run(screen.countdown())
asyncio.run(screen.stats())
time.sleep(2)
asyncio.run(screen.lose())
asyncio.run(screen.win())


# P1
'''
asyncio.run(p1.welcome())
asyncio.run(p1.player())
asyncio.run(p1.getready())
asyncio.run(p1.countdown())
asyncio.run(p1.scan())
asyncio.run(p1.stats())
time.sleep(2)
asyncio.run(p1.hit())
asyncio.run(p1.stats())
time.sleep(2)
asyncio.run(p1.miss())
asyncio.run(p1.stats())
time.sleep(2)
asyncio.run(p1.life())
asyncio.run(p1.stats())
time.sleep(2)
asyncio.run(p1.cooldown())
asyncio.run(p1.countdown())
asyncio.run(p1.stats())
time.sleep(2)
asyncio.run(p1.lose())
asyncio.run(p1.win())
'''

# P2
'''
asyncio.run(p2.welcome())
asyncio.run(p2.player())
asyncio.run(p2.getready())
asyncio.run(p2.countdown())
asyncio.run(p2.scan())
asyncio.run(p2.stats())
time.sleep(2)
asyncio.run(p2.hit())
asyncio.run(p2.stats())
time.sleep(2)
asyncio.run(p2.miss())
asyncio.run(p2.stats())
time.sleep(2)
asyncio.run(p2.life())
asyncio.run(p2.stats())
time.sleep(2)
asyncio.run(p2.cooldown())
asyncio.run(p2.countdown())
asyncio.run(p2.stats())
time.sleep(2)
asyncio.run(p2.lose())
asyncio.run(p2.win())
'''