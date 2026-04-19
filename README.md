Here is the finalized `README.md` content, structured for clarity and professional technical documentation. You can copy this directly into your GitHub editor.

---

# ODT 2026 Capstone: Decentralized Laser Tag System

An autonomous hardware-software implementation of a laser tag system built on the ESP32 platform. This project utilizes the NEC Infrared (IR) transmission protocol to facilitate real-time, peer-to-peer combat mechanics without the need for a central server.

## ⚡ Electronic Details

| Component | Role | Rationale |
| :--- | :--- | :--- |
| **ESP32** | Central MCU | Dual-core processing allows for simultaneous IR signal monitoring and UI updates via MicroPython. |
| **Laser Dot Diode (650nm)** | Aiming Aid | Provides a visible red dot for player targeting; strictly visual to ensure aiming precision. |
| **IR Emitter LED** | Data Transmitter | High-output 940nm LED modulated at $38\text{kHz}$ to transmit encoded NEC packets. |
| **IR Receiver LED** | Signal Capture | High-sensitivity photodiode used to detect incoming modulated IR pulses. |
| **0.96" OLED (I2C)** | HUD Display | A $128\times64$ pixel screen used to display real-time health, ammunition, and team ID. |
| **Active Buzzer** | Audio Feedback | Provides immediate haptic/audio confirmation of "hits," "firing," and "respawn" states. |
| **3-Stage Slide Switch** | Power Control | Controls the 6V rail to the ESP32, allowing for Off/Safe/Active power states. |
| **Push Button** | Trigger | Tactile input for firing sequences; debounced in software to prevent ghost firing. |
| **4x AA Batteries** | Power Source | Provides a portable $6\text{V}$ supply, ideal for extended gameplay on a college campus. |

---

## 💻 Software Details

### System Architecture
The firmware is developed in **MicroPython**. It utilizes a non-blocking asynchronous architecture to handle multiple hardware peripherals simultaneously.

### Logic & Implementation
* **NEC Protocol Timing:** The system follows the NEC standard: a $9\text{ms}$ leading pulse followed by a $4.5\text{ms}$ space. This robust timing ensures the receiver can distinguish a "shot" from ambient infrared noise.
* **Signal Demodulation:** Since a raw IR receiver LED is used, the ESP32 performs high-speed sampling of the GPIO state. A software-based state machine decodes the pulses into 32-bit data packets containing Player IDs and damage values.
* **Feedback Loop:** Upon a valid "Hit" detection, the system triggers a hardware interrupt that immediately updates the OLED display and activates the buzzer, ensuring zero-latency feedback for the player.

---

## 📂 Project Documents

### Project Basis & Planning
The project was selected to solve the challenge of creating an engaging, low-cost recreational technology that can function in any environment. The choice of a decentralized model (Peer-to-Peer) removes the requirement for Wi-Fi infrastructure, making it ideal for open-campus environments.

### Design Decisions
* **NEC vs. Custom Protocol:** The NEC protocol was chosen for its error-correction capabilities (sending logical inverses of data), which is critical when using raw IR LEDs instead of integrated ICs.
* **Component Selection:** Standardized modules (0.96" OLED and 650nm Laser) were selected to ensure the design is easily replicable and repairable by other students.

---

## 🛠️ Mechanical Details

### Physical Architecture
The handheld unit is designed with a footprint of **17cm x 9cm**, balanced for ergonomics during active use.

* **Housing Design:** Developed in Fusion 360, the chassis uses a "Join" strategy to integrate the internal component mounting plates directly into the outer shell for maximum structural rigidity.
* **Optical Alignment:** The Laser Diode and IR Emitter are mounted in a fixed-parallel barrel assembly. This ensures the IR "cone" of transmission is centered on the visual laser dot.
* **User Ergonomics:** The 3-stage slide switch and trigger button are positioned for one-handed operation, while the OLED is recessed at the rear for easy visibility during combat.

---

## 🚀 Current Status
* **Hardware:** Component sourcing complete (Robu/MakerBazar).
* **CAD:** Enclosure design finalized in Fusion 360.
* **Software:** NEC modulation logic implemented via RMT peripheral.
* **Next Step:** Physical field testing to calibrate IR receiver sensitivity in outdoor daylight.
