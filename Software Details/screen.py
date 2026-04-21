from machine import Pin
import machine, ssd1306
import asyncio

i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
bz = Pin(25, Pin.OUT)

async def bzhit():
    i = 1
    for i in range(4):
        bz.on()
        await asyncio.sleep(0.033)
        bz.off()
        await asyncio.sleep(0.033)
        i = i + 1
        print(i)
    bz.on()
    await asyncio.sleep(0.5)
    bz.off()
    await asyncio.sleep(0.5)

async def bzmiss():
    i = 1
    for i in range(3):
        bz.on()
        await asyncio.sleep(0.033)
        bz.off()
        await asyncio.sleep(0.033)
        i = i + 1
        print(i)

async def bzend():
    i = 1
    for i in range(5):
        bz.on()
        await asyncio.sleep(0.5)
        bz.off()
        await asyncio.sleep(0.5)
        i = i + 1
        print(i)
        
async def bzcool():
    i = 1
    for i in range(3):
        bz.on()
        await asyncio.sleep(0.2)
        bz.off()
        await asyncio.sleep(0.8)
        i = i + 1
        print(i)

async def stats(lives, ammo, hits, misses):
    display.fill(0)
    display.text("YOUR STATS", 24, 0)
    display.hline(0, 14, 128, 1)
    display.text(f"Lives left: {lives}", 0, 20)
    display.text(f"Ammo: {ammo}", 0, 30)
    display.text(f"Hits: {hits}", 0, 40)
    display.text(f"Misses: {misses}", 0, 50)
    display.show()

async def welcome():
    display.fill(0)
    display.text('WELCOME', 36, 0)
    await asyncio.sleep(1)
    display.text('Lives: 5', 0, 20)
    display.text('Ammo: 10', 0, 30)
    display.hline(0, 39, 128, 1)
    display.text('3s cooldown', 0, 40)
    display.text('after 10 shots.', 0, 50)
    display.show()
    await asyncio.sleep(1)

async def press():
    display.fill(0)
    display.text("PRESS BUTTON", 16, 23)
    display.text("TO START", 32, 33)
    display.show()

async def countdown():
    display.fill(0)
    display.text("3...", 48, 28)
    display.show()
    await asyncio.sleep(1)
    
    display.fill(0)
    display.text("2...", 48, 28)
    display.show()
    await asyncio.sleep(1)
    
    display.fill(0)
    display.text("1...", 48, 28)
    display.show()
    await asyncio.sleep(1)

async def getready():
    display.fill(0)
    display.text("GET READY", 28, 28)
    display.show()
    await asyncio.sleep(1)
    await countdown()

async def scan():
    display.fill(0)
    display.text("SCAN!", 44, 28)
    display.show()
    await asyncio.sleep(1)

async def hit():
    display.fill(0)
    display.text(":)", 56, 23)
    display.text("THAT'S A HIT!", 12, 33)
    display.show()
    await asyncio.sleep(1)

async def miss():
    display.fill(0)
    display.text(":(", 56, 23)
    display.text("You missed...", 12, 33)
    display.show()
    await asyncio.sleep(1)

async def thanks():
    display.fill(0)
    display.text("Thanks for", 24, 23)
    display.text("playing!", 32, 33)
    display.show()
    await asyncio.sleep(1)
    display.fill(0)

async def win():
    display.fill(0)
    display.text(":D", 56, 28)
    display.show()
    await asyncio.sleep(1)
    display.fill(0)
    display.text("YOU WIN!", 32, 28)
    display.show()
    await asyncio.sleep(3)
    await thanks()

async def lose():
    display.fill(0)
    display.text(":(", 56, 28)
    display.show()
    await asyncio.sleep(1)
    display.fill(0)
    display.text("You lost...", 20, 28)
    display.show()
    await asyncio.sleep(3)
    await thanks()

async def cooldown():
    display.fill(0)
    display.text('COOLDOWN', 32, 28)
    display.show()
    await asyncio.sleep(1)
    
async def life(lives):
    display.fill(0)
    display.text("You lost", 32, 18)
    display.text("one life.", 28, 28)
    display.text(f"Lives left: {lives}", 12, 38)
    display.show()
    await asyncio.sleep(2)

