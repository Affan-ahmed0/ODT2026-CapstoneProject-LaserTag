import network
import espnow
import time
import framebuf
import machine, ssd1306
from machine import Pin

i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize Wi-Fi in station mode
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)  # Set channel explicitly if packets are not delivered
sta.disconnect()

# Initialize ESP-NOW
e = espnow.ESPNow()
try:
    e.active(True)
except OSError as err:
    display.text("Failed to initialize ESP-NOW:", 0, 0)
    raise

if e.active() == True:
    display.fill(0)
    display.text("espnow active!!", 0, 0)
    display.show()
    time.sleep(1)
    

# Receiver's MAC address
receiver_mac = b'\xe0\x8c\xfe\x32\xf8\x40'

# Adding peer
try:
    e.add_peer(b'\xe0\x8c\xfe\x32\xf8\x40')
except OSError as err:
    print("Failed to add peer:", err)
    raise

# Main loop to send messages
while True:
    try:
        display.text("What would you", 0, 20)
        display.text("like to tell your", 0, 30)
        display.text("fellow ESP32?", 0, 40)
        display.show()
        text = input()
        try:
            if e.send(b'\xe0\x8c\xfe\x32\xf8\x40', text, True):
                (f"Sent message: '{text}'")

            else:
                print("Failed to send message (send returned False)")
        except OSError as err:
            print(f"Failed to send message (OSError: {err})")
        
    except OSError as err:
        print("Error:", err)
        time.sleep(5)
        break
