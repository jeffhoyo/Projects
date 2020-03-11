from scapy.all import *

# our packet callback
def packet_callback(packet):

    print(packet.summary())
    print("")
    print("-----------------")
    print("")
    print(packet.show())

# fire up our sniffer
sniff(iface="lo0",prn=packet_callback,count=2)
