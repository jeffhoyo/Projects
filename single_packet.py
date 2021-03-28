from scapy import *

# our packet callback
def packet_callback(packet):

    print(packet.summary())
    print("-----------------")
    print(packet.show())
    print("-----------------")
    # print(packet.getlayer(IP in ICMP).ttl)
    # print(packet.getlayer(Dot3).dst)
    # print(packet.getlayer(Dot3).src)
    # print(packet.getlayer(Dot3).len)

# fire up our sniffer
sniff(iface="en0",prn=packet_callback,count=50)
