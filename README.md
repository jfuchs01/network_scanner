
# Network Scanner Tool

## Overview
The Network Scanner Tool is a Python-based application designed to scan and analyze your local network. It identifies connected devices, checks for open ports, and performs basic OS detection. This tool is useful for network administrators, cybersecurity professionals, and anyone interested in network security.

## Features
- **Device Discovery**: Identify all devices connected to the network.
- **Port Scanning**: List open ports on discovered devices.
- **OS Detection**: Infer operating systems of networked devices.

## Getting Started

### Prerequisites
You'll need Python installed on your system to run the network scanner. Ensure you have administrative or network permissions to conduct scans.

### Installation
Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/jfuchs01/network-scanner.git
cd network-scanner
pip install -r requirements.txt
```

### Usage
Execute the script from the command line to start the network scan:

```bash
python network_scanner.py
```

## How It Works
The tool uses the `scapy` library to craft and send packets across the network, listening for responses to identify devices and open ports. It then analyzes the collected data to provide a summary of the network state.

## Contributing
Your contributions are welcome! If you have suggestions or improvements, please fork the repo and submit a pull request.




