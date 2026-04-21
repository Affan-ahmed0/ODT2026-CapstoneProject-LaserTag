import network
import aioespnow
import asyncio

# 1. Initialize Wi-Fi and ESP-NOW
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)
sta.disconnect()

e = aioespnow.AIOESPNow()
e.active(True)

# 2. Define Peer
peer_mac = b'\xe0\x8c\xfe\x32\xf8\x40'

try:
    e.add_peer(peer_mac)
except OSError:
    pass # Peer might already be added

async def run_once(e, peer):
    # --- SEND ONCE ---
    
    message = input("What?")
    print(f"Sending: {message}")
    
    # Using 'await' ensures we wait for the delivery confirmation
    success = await e.asend(peer, message, sync=True)
    if success:
        print("Sent successfully!")
    else:
        print("Failed to send.")l

    # --- RECEIVE ONCE ---
    print("Waiting for one incoming message...")
    
    async for mac, msg in e:
        print(f"{msg.decode()}")


# 3. Execution
try:
    asyncio.run(run_once(e, peer_mac))
except KeyboardInterrupt:
    print("Stopped.")
finally:
    e.active(False)
    sta.active(False)