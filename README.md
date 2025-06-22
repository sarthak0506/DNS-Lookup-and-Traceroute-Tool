DNS Lookup and Traceroute Tool

> Description
A Python-based network diagnostic tool that performs DNS resolution, traceroutes, and latency checks. It helps users and network engineers analyze connectivity issues.

> Features
•	DNS Lookup
•	ICMP-based Traceroute
•	Latency testing using ping logic

> Technologies
•	Python 3.x
•	socket
•	scapy
•	time

> Getting Started
Create and activate a virtual environment
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install scapy
Run the app
python dns_tool.py

> Requirements
scapy
⚠ Note: You might see a No libpcap provider available warning. It can be ignored if basic traceroute and ping are functioning.
