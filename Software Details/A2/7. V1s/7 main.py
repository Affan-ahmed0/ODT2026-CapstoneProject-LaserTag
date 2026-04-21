from machine import Pin
import machine, ssd1306
import framebuf
import time
import screen
import comms
import asyncio


# HARDWARE INITIALIZARION
lz = Pin(25, Pin.OUT)
ldr = Pin(15, Pin.IN, Pin.PULL_UP)
pb = Pin(14, Pin.IN, Pin.PULL_UP)

# GAME VARIABLES & TRACKING
ammo = 10
lives = 5
hits = 0
misses = 0
last_button_state = 1

# HIT LISTENER
async def hit_listener():
    global hits, misses
    while True:
        msg = await comms.arcv() 
        
        if msg == "hit2":
            hits = hits + 1
            await screen.hit()
            
            if hits >= 5:
                await screen.win()
                return True
        else:
            misses = misses + 1
            await screen.miss()
        await asyncio.sleep(0.01)


# MAIN GAME LOOP
async def main_game():

    # GAME INITIALIZATION
    global lives, ammo, hits, misses, last_button_state
        
    await screen.welcome()
    await screen.getready()
    await screen.countdown()
    asyncio.create_task(hit_listener())
    await screen.stats(lives, ammo, hits, misses)

    while True:
        # ATTACK
        click = pb.value()
        if click == 0  and last_button_state == 1:
            
            # SUFFICIENT AMMO
            if ammo >= 1:
                lz.on()
                await asyncio.sleep(0.3)
                lz.off()
                ammo = ammo - 1                

            # INSUFFICIENT AMMO
            elif ammo <= 0:
                await screen.cooldown()
                ammo = 10
                await screen.countdown()
                
            await screen.stats(lives, ammo, hits, misses)
                
        # VICTIM
        if ldr.value() == 0:
            await comms.asend()
            lives = lives - 1
            await screen.life(lives)
            
            if lives <= 0:
                await screen.lose()
                return                
            await screen.stats(lives, ammo, hits, misses)

        last_button_state = click
        await asyncio.sleep(0.05)
        
asyncio.run(main_game())

