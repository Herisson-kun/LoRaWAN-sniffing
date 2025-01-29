# LoRaWAN Sniffer Project

## Project Objective
The goal of this project is to create a **LoRaWAN sniffer** capable of listening to LoRa frames on any frequency and Spreading Factor (SF). The primary objective is to study the security of the LoRaWAN protocol by intercepting and analyzing the frames exchanged between IoT devices and a LoRaWAN network.

The project is built around a system using a Raspberry Pi 4 Model B and an RFM9x radio module, along with Python and Arduino scripts to capture, analyze, and convert LoRaWAN frames.

---

## Main Features
1. **LoRaWAN Frame Capture**:  
   A Raspberry Pi 4 Model B equipped with an RFM9x module captures raw LoRaWAN frames in hexadecimal format, for a specified frequency and SF.

2. **CSV Logging**:  
   The captured frames are logged in a `packet_capture.csv` file, which includes:
   - The time at which the frame has been received.
   - The frames in hexadecimal format.
   - Reception quality indicators such as RSSI and SNR.

3. **Conversion to PCAP**:  
   A Python script reads the CSV file, parses the frames, identifies each field of the protocol (e.g., MHDR, DevAddr, Encrypted Payload, etc.), and converts the frames into Python objects. Using these objects, the script generates a PCAP file compatible with Wireshark for analysis.

4. **Testing with MKR WAN 1310**:  
   To generate frames for testing, a **MKR WAN 1310** module connected to The Things Network (TTN) was used. The Arduino code provided in the repository configures this module to send frames to TTN.

---

## Project Architecture

### Hardware Components
- **Raspberry Pi 4 Model B**  
  Used as the platform for the sniffer, with its SPI port connected to the RFM9x module.

- **RFM9x Radio Module**  
  A LoRa module (SX1276) capable of receiving LoRa frames with configurable frequency, bandwidth, SF, and other parameters.

- **MKR WAN 1310**  
  Configured to send LoRaWAN frames, this module was used to test the sniffer.

### Wiring

**Hardware Setup**  
   The RFM9x module is connected to the Raspberry Pi via the SPI interface:  
   - **Vin**: Raspberry Pi 3.3V  
   - **GND**: Raspberry Pi Ground  
   - **G0**: Raspberry Pi GPIO #5  
   - **RST**: Raspberry Pi GPIO #25  
   - **CLK**: Raspberry Pi SCK  
   - **MISO**: Raspberry Pi MISO  
   - **MOSI**: Raspberry Pi MOSI  
   - **CS**: Raspberry Pi CE1  

---

### Software Components

#### 1. **Python Code (Sniffer)**  
   Hosted on the Raspberry Pi, this code performs the following tasks:
   - Configures the RFM9x module to listen for LoRaWAN frames at a specific frequency and SF.
   - Captures raw frames in hexadecimal format and logs them to a CSV file (`packet_capture.csv`) along with RSSI and SNR values.

   The following libraries are used in the Python code:  
   - `adafruit-circuitpython-rfm9x`: For interacting with the RFM9x module over SPI.  
   - `adafruit-blinka`: To enable hardware interfaces on the Raspberry Pi.  
   - `time`: For managing delays and recording message timestamps (built-in module).  
   - `csv`: For handling CSV file operations (built-in module).  
   - `digitalio`, `busio`, and `board`: For GPIO and SPI hardware configuration (provided by `adafruit-blinka`).

   To install the required libraries, run:  
   ```bash
   pip install adafruit-circuitpython-rfm9x adafruit-blinka
   ```

#### 2. **Python Code (PCAP Conversion)**  
   A separate Python script reads the CSV file, parses each frame, and decomposes it into:
   - **MHDR** (Message Header): Specifies the message type and protocol version.
   - **DevAddr**: Device address.
   - **FCtrl, FCnt, FOpts, FPort**: Control fields, frame counters, options, and port.
   - **FRMPayload**: Encrypted payload.
   - **MIC**: Message Integrity Code for frame authentication.

   These fields are encapsulated into `Packet` objects. A function then converts these objects into a PCAP file that can be opened with Wireshark for detailed analysis.

#### 3. **Arduino Code (MKR WAN 1310)**  
The MKR WAN 1310 module, configured with Arduino, serves as the LoRaWAN frame transmitter. To set up the board:  
1. **Download the Arduino IDE**: Install the [Arduino IDE](https://www.arduino.cc/en/software) on your computer.  
2. **Install the MKRWAN Library**: Open the Arduino IDE, go to **Tools > Manage Libraries**, search for "MKRWAN", and install the library.  
3. **Set Up the Board in the IDE**:  
   - Connect the MKR WAN 1310 to your computer using a USB cable.  
   - In the Arduino IDE, go to **Tools > Board > Boards Manager**, search for "MKR WAN 1310", and install the required package.  
   - Select the **MKR WAN 1310** board under **Tools > Board** and the appropriate **Port** under **Tools > Port**.  

Once configured, you can upload the provided Arduino code to the MKR WAN 1310. The module will send LoRaWAN frames to TTN, allowing the sniffer to intercept and analyze them.

---