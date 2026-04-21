from machine import Pin, I2C
import machine, ssd1306
import framebuf
import time
import screen
import comms
import asyncio


# HARDWARE INITIALIZARION
lz = Pin(32, Pin.OUT)
ldr = Pin(15, Pin.IN, Pin.PULL_UP)
pb = Pin(14, Pin.IN, Pin.PULL_UP)

# GAME VARIABLES & TRACKING
ammo = 10
lives = 5
hits = 0
misses = 0
last_button_state = 1

running = True

# HIT LISTENER
async def hit_listener():
    global hits, misses, lives, running
    while True:
        msg = await comms.arcv() 
        
        if msg == "hit2":
            hits = hits + 1
            await asyncio.gather(screen.hit(), screen.bzhit())
            await screen.stats(lives, ammo, hits, misses)
            if hits >= 5:
                await asyncio.gather(screen.bzend(), screen.win())
                running = False
                break
            
        elif msg == "miss2":
            misses = misses + 1
            await asyncio.gather(screen.bzmiss(), screen.miss())
            await screen.stats(lives, ammo, hits, misses)
        
        elif msg == "shot2":
            if ldr.value() == 0:
                await comms.asend("hit1")
                lives = lives - 1
                await screen.life(lives)
                if lives <= 0:
                    await asyncio.gather(screen.bzend(), screen.lose())
                    running = False
                    break
                await screen.stats(lives, ammo, hits, misses)
            else:
                await comms.asend("miss1")
                await screen.stats(lives, ammo, hits, misses)
        await asyncio.sleep(0.1)


# SHOOTER (MAIN LOOP)
async def main_game():

    # GAME INITIALIZATION
    global lives, ammo, hits, misses, last_button_state, running
        
    await screen.welcome()
    
    await screen.press()
    
    while pb.value() == 1:       # Gate for the rest of the code
        await asyncio.sleep(0.1)
    
    await screen.getready()
    await screen.countdown()
    asyncio.create_task(hit_listener())
    await screen.stats(lives, ammo, hits, misses)

    while running == True: # ATTACK
        click = pb.value()
        if click == 0  and last_button_state == 1:
            
            # SUFFICIENT AMMO
            if ammo >= 1:
                lz.on()
                await asyncio.sleep(0.3)
                await comms.asend("shot1")
                lz.off()
                ammo = ammo - 1

            # INSUFFICIENT AMMO
            elif ammo <= 0:
                await screen.cooldown()
                ammo = 10
                await asyncio.gather(screen.bzcool(), screen.countdown())
                
            await screen.stats(lives, ammo, hits, misses)

        last_button_state = click
        await asyncio.sleep(0.05)
        
asyncio.run(main_game())