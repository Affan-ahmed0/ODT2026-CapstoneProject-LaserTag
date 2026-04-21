import network
import aioespnow
import asyncio
import time

# Initialize Wi-Fi in station mode
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)  # Set channel explicitly if packets are not received
sta.disconnect()

# Initialize AIOESPNow
e = aioespnow.AIOESPNow()
try:
    e.active(True)
except OSError as err:
    print("Failed to initialize AIOESPNow:", err)
    raise

# Peer MAC address (replace with the actual MAC of the other board)
peer_mac = b'\xe0\x8c\xfe\x32\xf8\x40'  # Example peer MAC for unicast

# Add peer for unicast reliability
try:
    e.add_peer(peer_mac)
except OSError as err:
    print("Failed to add peer:", err)
    raise


# Async function to send messages
async def send_messages(e, peer):
    while True:
        try:
            message = f"Hello from ESP32"
            if await e.asend(peer, message, sync=True):
                print(f"Sent message: {message}")
            else:
                print("Failed to send message")
            await asyncio.sleep(1)  # Send every 1 second
        except OSError as err:
            print("Send error:", err)
            await asyncio.sleep(5)

# Async function to receive messages
async def receive_messages(e):
    while True:
        try:
            async for mac, msg in e:
                print(f"Received from {mac.hex()}: {msg.decode()}")
        except OSError as err:
            print("Receive error:", err)
            await asyncio.sleep(5)


# Main async function
async def main(e, peer):
    # Run send, receive, and stats tasks concurrently
    await asyncio.gather(send_messages(e, peer), receive_messages(e))

# Run the async program
try:
    asyncio.run(main(e, peer_mac))
except KeyboardInterrupt:
    print("Stopping transceiver...")
    e.active(False)
    sta.active(False)