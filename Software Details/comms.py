import network
import aioespnow
import asyncio
import time

# FOUNDATIONS
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)
time.sleep_ms(100)
sta.disconnect()
e = aioespnow.AIOESPNow()
e.active(True)

# Add Broadcast Peer
peer_mac = b'\xff\xff\xff\xff\xff\xff' 
try:
    e.add_peer(peer_mac)
except OSError:
    pass

# CORE: Defining the send and receive functions
async def asend(msg):
    try:
        await e.asend(peer_mac, msg, sync=True)
    except OSError as err:
        print("Send failed:", err)

async def arcv():
    try:
        mac, msgr = await asyncio.wait_for(e.arecv(), timeout=0.1)
        if msgr is not None:
            return msgr.decode('utf-8')
    except asyncio.TimeoutError:
        pass
    return None
