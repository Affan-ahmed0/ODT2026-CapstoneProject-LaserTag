from machine import Pin, I2C
import ssd1306
import time

print("--- Starting Hardware Component Test ---")

# 1. TEST I2C & OLED
print("Testing OLED...")
try:
    i2c = I2C(scl=Pin(19), sda=Pin(21))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.fill(0)
    display.text("OLED: WORKING", 0, 0)
    display.show()
    print("OLED: Success (Check screen)")
except Exception as e:
    print("OLED: FAILED -", e)

time.sleep(1)

# 2. TEST LASER (Pin 32)
print("Testing Laser (Pin 32)...")
lz = Pin(32, Pin.OUT)
lz.on()
print("LASER: SHOULD BE ON NOW")
time.sleep(2)
lz.off()
print("LASER: OFF")

# 3. TEST BUZZER (Pin 25)
print("Testing Buzzer (Pin 25)...")
bz = Pin(25, Pin.OUT)
for _ in range(3):
    bz.on()
    time.sleep(0.1)
    bz.off()
    time.sleep(0.1)
print("BUZZER: Success if you heard 3 beeps")

# 4. TEST PUSH BUTTON (Pin 14)
print("Testing Button (Pin 14)...")
pb = Pin(14, Pin.IN, Pin.PULL_UP)
print("Please press the BUTTON now...")
start_time = time.time()
button_pressed = False
while time.time() - start_time < 5: # 5 second window
    if pb.value() == 0:
        print("BUTTON: DETECTED!")
        button_pressed = True
        break
    time.sleep(0.1)
if not button_pressed:
    print("BUTTON: TIMEOUT (Check wiring)")

# 5. TEST LDR (Pin 15)
print("Testing LDR (Pin 15)...")
ldr = Pin(15, Pin.IN, Pin.PULL_UP)
print("Point a light at the LDR or cover it...")
for _ in range(10):
    val = ldr.value()
    status = "LIGHT/LASER DETECTED" if val == 0 else "NO LIGHT"
    print(f"LDR Reading: {val} ({status})")
    time.sleep(0.5)

print("--- Hardware Test Complete ---")