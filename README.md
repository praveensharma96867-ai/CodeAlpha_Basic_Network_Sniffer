# Basic Network Sniffer

A simple Python-based Network Sniffer that captures live network packets and displays useful information such as source IP, destination IP, protocol, ports, and payload.

---

## Features

- Capture live network traffic
- Display Source IP Address
- Display Destination IP Address
- Identify Protocol (TCP, UDP, ICMP)
- Display Source and Destination Ports
- Display Packet Payload
- Beginner-friendly Python code

---

## Technologies Used

- Python 3
- Scapy Library

---

## Project Structure

```
Basic-Network-Sniffer/
│── sniffer.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Basic-Network-Sniffer.git
```

Go to the project folder:

```bash
cd Basic-Network-Sniffer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Program

```bash
python sniffer.py
```

On Windows, run the terminal or VS Code as Administrator.

---

## Sample Output

```
==================================================
        BASIC NETWORK SNIFFER
==================================================

Starting packet capture...

--------------------------------------------------
Source IP       : 192.168.1.10
Destination IP  : 142.250.182.14
Protocol        : TCP
Source Port     : 54231
Destination Port: 443
Payload         : b'GET / HTTP/1.1'
--------------------------------------------------
```

---

## Learning Outcomes

- Learned how packets travel across a network.
- Understood the IP, TCP, UDP, and ICMP protocols.
- Captured live packets using Scapy.
- Extracted useful information from network packets.
- Displayed packet payload for analysis.

---

## Future Improvements

- Save captured packets to a log file.
- Add filtering by protocol.
- Display timestamps.
- Export packet details to a CSV file.
- Create a graphical user interface.

---

## Author

Praveen Sharma
