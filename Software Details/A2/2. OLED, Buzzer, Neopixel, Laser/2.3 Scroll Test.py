from machine import Pin
import machine, ssd1306
import framebuf
import time

i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

message = "HELLO WORLD"
x = 128  # Start at the right edge of the screen
y = 28   # Vertical center

while True:
    display.fill(0)              # Clear screen
    display.text(message, x, y)  # Draw text at current X
    display.show()               # Update display
    
    x -= 2                       # Move 2 pixels to the left
    
    # Reset position if it goes off screen
    # (assuming 8 pixels per character, 11 chars * 8 = 88)
    if x < -90: 
        x = 128
        
    time.sleep(0.01)             # Control scroll speed
