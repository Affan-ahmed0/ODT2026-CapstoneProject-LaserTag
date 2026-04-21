import network
import aioespnow
import asyncio
import time

from machine import Pin
import machine, ssd1306
import framebuf

# OLED
i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)

def wrap_text(text, width=16):
    return [text[i:i + width] for i in range(0, len(text), width)]

# FOUNDATIONS: Initialize Wi-Fi, AIOESPNow, and add Peer
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)  # Set channel explicitly if packets are not received
sta.disconnect()

e = aioespnow.AIOESPNow()
try:
    e.active(True)
    print("AIOESPNow Active.")
    display.text("ACTIVE.", 0, 0)
    display.show()
    
except OSError as err:
    print("Failed to initialize AIOESPNow:", err)
    display.text("INACTIVE.", 0, 0)
    display.show()
    
    raise

peer_mac = b'\xe0\x8c\xfe\x32\xa7\x6c' 
try:
    e.add_peer(peer_mac)
    print("Peer Added.")
    display.text("Peer Added.", 0, 20)
    display.show()
    
except OSError as err:
    print("Failed to add peer:", err)
    display.text("FAILED.", 0, 20)
    display.show()
    
    raise


# CORE: Defining the send and recieve functions
async def asend(e, peer_mac, timeout=5.0):
    try:
        display.fill(0)
        display.text("ACTIVE.", 0, 0)
        display.show()
        display.text("What?", 0, 20)
        display.show()
        await asyncio.sleep(2)
        
        msgs = input("What?")
        
        if await e.asend(peer_mac, msgs, sync=True):
            print(f"Ok. Sent message: {msgs}")
            
            msgslines = wrap_text(msgs, 16)
            for i, msgsline in enumerate(msgslines):
                if i < 6:
                    display.fill_rect(0, 8, 128, 20, 0)
                    display.show()
                    display.text("Sent.", 0, (i+2) * 10)
                    
            display.show()
            await asyncio.sleep(2)
            display.fill_rect(0, 8, 128, 20, 0)
            display.show()
            display.text("hold tight...", 0, 20)
            display.show()
                        
        else:
            print("Failed to send message")
            
            display.text("FAILED.", 0, 30)
            display.show()
            await asyncio.sleep(2)
            
        await asyncio.sleep(1)  # Send every 1 second
        
    except OSError as err:
        print("Send error:", err)
        await asyncio.sleep(5)

async def arcv(e):
    try:
        mac, msgr = await e.arecv()
        
        if msgr:
            msgrdisplay = msgr.decode('utf-8', 'ignore')
            print(msgrdisplay)
            
            display.fill(0)
            display.text("ACTIVE.", 0, 0)
            display.text(msgrdisplay, 0, 20)
            display.show()
            await asyncio.sleep(2)
            
    except OSError as err:
        print("Receive error:", err)
        display.text("FAILED.", 20, 0)
        display.show()
        await asyncio.sleep(2)
            
async def main(e, peer_mac):
    print("System online. Listening and ready to send.")
    display.fill(0)
    display.text("ACTIVE.", 0, 0)
    display.show()
    await asyncio.sleep(2)
    
    while True:
        await arcv(e)
        await asend(e, peer_mac)

# FINAL CUT: Running it all together
try:
    asyncio.run(main(e, peer_mac))
except KeyboardInterrupt:
    print("Stopping...")
    e.active(False)
    sta.active(False)
except OSError as err:
    print("Error:", err)