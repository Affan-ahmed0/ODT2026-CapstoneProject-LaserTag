import network
import aioespnow
import asyncio
import time

# FOUNDATIONS: Initialize Wi-Fi, AIOESPNow, and add Peer
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)  # Set channel explicitly if packets are not received
sta.disconnect()

e = aioespnow.AIOESPNow()
try:
    e.active(True)
    print("AIOESPNow Active.")
except OSError as err:
    print("Failed to initialize AIOESPNow:", err)
    raise

peer_mac = b'\xe0\x8c\xfe\x32\xa7\x6c' 
try:
    e.add_peer(peer_mac)
    print("Peer Added.")
except OSError as err:
    print("Failed to add peer:", err)
    raise


# CORE: Defining the send and recieve functions
async def asend(e, peer_mac, timeout=5.0):
    try:
        msgs = input("What?")
        if await e.asend(peer_mac, msgs, sync=True):
            print(f"Sent message: {msgs}")
        
        else:
            print("Failed to send message")
        await asyncio.sleep(1)  # Send every 1 second
    except OSError as err:
        print("Send error:", err)
        await asyncio.sleep(5)

async def arcv(e):
    try:
        mac, msgr = await e.arecv()
        if msgr:
            msgrdisplay = msgr.decode('utf-8', 'ignore')
            print(f"Received from {mac.hex()}: {msgrdisplay}")
    except OSError as err:
        print("Receive error:", err)
        await asyncio.sleep(5)
            
async def main(e, peer_mac):
    print("System online. Listening and ready to send.")
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