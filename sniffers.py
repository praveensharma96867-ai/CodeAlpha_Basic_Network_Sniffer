from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

print("=" * 50)
print("        BASIC NETWORK SNIFFER")
print("=" * 50)
print("Starting packet capture...")
print("Press Ctrl + C to stop.\n")


def analyze_packet(packet):

    print("-" * 50)

    if packet.haslayer(IP):

        print("Source IP       :", packet[IP].src)
        print("Destination IP  :", packet[IP].dst)

        protocol = packet[IP].proto

        if protocol == 6:
            print("Protocol        : TCP")

        elif protocol == 17:
            print("Protocol        : UDP")

        elif protocol == 1:
            print("Protocol        : ICMP")

        else:
            print("Protocol        : Other")

    if packet.haslayer(TCP):

        print("Source Port     :", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)

    elif packet.haslayer(UDP):

        print("Source Port     :", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)

    elif packet.haslayer(ICMP):

        print("ICMP Type       :", packet[ICMP].type)
        print("ICMP Code       :", packet[ICMP].code)

    if packet.haslayer(Raw):

        payload = packet[Raw].load

        print("Payload         :", payload[:50])

    print("-" * 50)


sniff(prn=analyze_packet, store=False)