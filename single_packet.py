from scapy.all import *

# our packet callback
def packet_callback(packet):

    # print(packet.summary())
    # print("-----------------")
    print(packet.getlayer(Dot3).dst)
    print(packet.getlayer(Dot3).src)
    print(packet.getlayer(Dot3).len)

# fire up our sniffer
sniff(iface="en0",filter="stp",prn=packet_callback,count=50)
