from detector import detect_syn_flood

def main():
    from scapy.all import sniff
    print("sniffing started... Press Ctrl+C to stop.")
    sniff(prn=detect_syn_flood, store=0, iface="en0")

if __name__ == "__main__":
    main()