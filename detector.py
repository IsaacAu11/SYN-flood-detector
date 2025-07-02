import socket
from scapy.all import *
import time

syn_tracker = {}
threshold = 5
time_window = 10

def detect_syn_flood(packet):
    global syn_tracker
    if packet.haslayer('TCP') and packet['TCP'].flags == 'S':
        src_ip = packet['IP'].src
        try:
            src_name = socket.gethostbyaddr(src_ip)[0]
        except Exception:
            src_name = "Unknown"
        print(f"Detected SYN packet from {src_ip} ({src_name})")
        current_time = time.time()
        if src_ip not in syn_tracker:
            syn_tracker[src_ip] = []
        syn_tracker[src_ip] = [t for t in syn_tracker[src_ip] if current_time - t < time_window]
        syn_tracker[src_ip].append(current_time)
        print(f"Current SYN count for {src_ip}: {len(syn_tracker[src_ip])}")
        if len(syn_tracker[src_ip]) > threshold:
            print()
            print(f"Potential SYN flood detected from {src_ip}!")
            print(f"Number of SYN packets: {len(syn_tracker[src_ip])}")
            print()