from scapy.all import sniff

def capture(packet):
    print(packet.summary())

def start_sniffing():
    sniff(prn=capture, count=10)