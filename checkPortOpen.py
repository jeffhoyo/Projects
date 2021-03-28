from scapy.all import *

def sendPacket():
    dst_ip = str(input("Please enter dst ip > "))
    dst_port = int(input("Please enter dst port > "))
    portCounter = 443
    portScan = IP(dst=dst_ip)/TCP(sport=portCounter,dport=dst_port,flags="SA")
    print("")
    print(portScan.show())
    response = sr(portScan,iface="en0")
    print("")
    print(response.summary())

sendPacket()
