## A simple IDS to detect SYN flood attacks using Python and Scapy.

### Features:

- Monitors TCP SYN packets in real time.

- Alerts if SYN count from a source IP exceeds a threshold.

- Includes a SYN flood simulation script for testing.

### Usage:

1) Run IDS script:
"sudo python3 main.py"

2) Run SYN flood simulation:
"sudo python3 simulate_syn_flood.py <target_ip> <target_port> [packet_count]"

### Requirements:

- Python 3

- Scapy

- Root privileges
