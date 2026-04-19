# Components Used:

**Laser Dot Diode Module:** Acts as visual aid for player to know where they are shooting  

**Infrared Emmiter LED:** Sends a IR Signal  

**Infrared Reciever LED:** Recieves the IR Signal  

**ESP32:** Used for computing the signals, giving outputs and Wireless communication between ESP32's  

**OLED Display:** Displays information to the Player.  

**Active Buzzer:** Gives audible feedback to the player when hit registered and game ends.  

**3 Stage Slider Switch:** Controls the power to the ESP32  

**Push Button (Trigger):** Fires Laser and IR Emmiter when pressed  

**Battery:** Powers the ESP32

# Components used & Purpose

### Project Components Overview

| Component | Purpose | Justification of Use |
| :--- | :--- | :--- |
| **ESP32 Microcontroller** | Central processing and logic unit. | High clock speed for precise IR pulse timing and built-in Wi-Fi/Bluetooth for future scoring sync. |
| **Laser Dot Diode (650nm)** | Visual aiming reference. | Provides a clear, visible point of impact for the player without interfering with the IR data stream. |
| **IR Emitter LED | PIN 18 (RMT)** | Data transmitter. | Operates at a 940nm wavelength, allowing for discrete, high-speed data transmission invisible to the human eye. |
| **IR Receiver LED | PIN 19 (IRQ)** | Signal detection. | A lightweight, low-cost solution for capturing incoming IR pulses for software-based demodulation. |
| **0.96" OLED Display | PIN 21 (SLC) PIN 21 (SDA) ** | Real-time Head-Up Display (HUD). | Provides essential game telemetry (health, ammo, team) in a compact, low-power I2C form factor. |
| **Active Buzzer** | Audio feedback system. | Low-latency audible alerts for "hits" and "firing," essential for situational awareness during play. |
| **3-Stage Slide Switch** | Power and state control. | Offers a physical "Safety" or "Off" state, preventing accidental battery drain and accidental firing. |
| **Push Button (Trigger)** | Input for firing action. | Provides tactile feedback for the user and is easily integrated with ESP32 GPIO interrupts. |
| **4x AA Battery Pack** | Portable power supply. | Readily available and provides a stable 6V input to the ESP32’s voltage regulator for long-duration play. |
