## Port Scanner (TCP Connect Scan)
### 0x01 Overview
This is a lightweight network reconnaissance tool written in Python. It identifies open ports on a target IP address by attempting to complete the TCP Three-Way Handshake.

In a cybersecurity context, this represents the "Reconnaissance" phase of the Cyber Kill Chain, helping an auditor understand the attack surface of a host.

### 0x02 Technical Deep Dive
The script utilizes the socket library to perform a TCP Connect Scan.

Protocol: TCP (Transmission Control Protocol)

Logic: 1. The script sends a SYN packet to the target port.
2. If the port is Open, the target responds with a SYN/ACK.
3. The script's connect_ex() method returns 0 (Success).
4. If the port is Closed, the target responds with an RST (Reset) packet, and the method returns an error code.

### 0x03 Features
Custom Range: Allows the user to specify a start and end port range.

Error Handling: Includes specific exceptions for:

KeyboardInterrupt: Clean exit on Ctrl+C.

gaierror: Handles cases where the hostname cannot be resolved.

socket.error: Manages general connection failures.

Timing: Implements a 0.5s timeout per port to balance speed and accuracy.

### 0x04 Setup & Usage
Clone the parent repo:

git clone https://github.com/aadyaraikar/Cybersecurity/edit/main/Cybersec/port-scanner/port-scanner.py
cd cybersec/port-scanner

Run the tool:
python scanner.py

Input details:

Target: 127.0.0.1 (to test your own machine) or a specific IP.

Range: e.g., 20 to 80.

### 0x05 Key Learning Outcomes
Socket Programming: Gained hands-on experience with the Python socket module and low-level network communication.

Handshake Mechanics: Visualized how OS-level networking responds to connection requests.

Exception Handling: Learned to manage network-level errors (timeouts, DNS failures) that often crash basic scripts.

### ⚠️ Disclaimer
This tool is for educational and ethical testing purposes only. Unauthorized scanning of networks you do not own or have explicit permission to test is illegal and unethical.
