import network
import espnow
import time
import framebuf
import ssd1306
import machine

i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize Wi-Fi in station mode
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)  # Set channel explicitly if packets are not received
sta.disconnect()

# Initialize ESP-NOW
e = espnow.ESPNow()
try:
    e.active(True)
except OSError as err:
    print("Failed to initialize ESP-NOW:", err)
    raise

if e.active() == True:
    display.fill(0)
    display.text("espnow active!", 0, 0)
    display.show()
    time.sleep(1)

# Sender's MAC address
sender_mac = b'e0:8c:fe:32:f8:6c'  # Sender MAC

display.text("hold tight...", 0, 20)
display.show()
time.sleep(1)

while True:
    try:
        # Receive message (host MAC, message, timeout of 10 seconds)
        host, text = e.recv(10000)
        displaytext = text.decode('utf-8')
        if text:
            display.fill(0)
            display.text("you got a text!", 0, 20)
            display.text(f"msg: '{displaytext}", 0, 30)
            display.show()
        
    except OSError as err:
        print("Error:", err)
        time.sleep(5)
        
        break
