from machine import Pin
import machine, ssd1306
import framebuf
import time
import screen

i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

'''
screen.welcome()
screen.player1()

screen.welcome()
screen.player2()

screen.getready()

screen.countdown()
screen.scan()
'''
screen.cooldown()
screen.countdown()

screen.hit()

screen.miss()

screen.win()

screen.lose()

screen.thanks()