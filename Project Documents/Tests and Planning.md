### Project Planning and Testing Framework

| Phase | Activity | Objectives | Outcome/Status |
| :--- | :--- | :--- | :--- |
| **Initial Planning** | **Mechanical CAD Modeling** | [cite_start]Design a 17cm x 9cm housing in Fusion 360 to contain all electronics[cite: 3, 59, 62]. | Housing designed with integrated mounting plates and an ergonomic handle for a 4x AA battery pack. |
| **Initial Planning** | **System Architecture** | [cite_start]Define the multi-layer logic for detection, control, and feedback using an ESP32[cite: 22, 23, 26]. | Established a decentralized P2P model using MicroPython and the NEC protocol for robust data exchange. |
| **Testing** | **Protocol Verification** | Ensure the NEC signal timing (9ms pulse/4.5ms space) is accurate using the RMT peripheral. | Confirmed via logic analysis that the carrier wave remains stable under processor load. |
| **Testing** | **Signal Demodulation** | Test the raw IR receiver's ability to distinguish 38kHz pulses from ambient light. | Software-based sampling successfully decoded 32-bit packets without an integrated TSOP sensor. |
| **Integration** | **Circuit Dry-Run** | [cite_start]Verify all components (OLED, Buzzer, Laser, IR) function together on a breadboard[cite: 59]. | Successfully tested the full feedback loop: trigger press leads to IR transmission and local UI update. |
| **Integration** | **Housing Fitment** | Attempt to integrate the wired circuit into the 3D-printed gun shell. | **Failure:** The overwhelming number of discrete connections exceeded the internal volume of the shell. |
| **Post-Mortem** | **Failure Analysis** | Evaluate why the circuit did not fit despite exhaustive CAD planning. | Identified that 22AWG wiring density and cumulative solder joint volume were not sufficiently accounted for in CAD. |
