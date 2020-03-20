from scapy.all import *
import random



def sendPacket():
    portCounter = 20
    dst_ip = str(input("Please enter dst ip > "))
    while portCounter < 30:
        randInt = random.randint(20, 30)
        # dst_port = int(input("Please enter dst port > "))
        portScan = IP(dst=dst_ip)/TCP(sport=randInt,dport=portCounter,flags="SA")
        print("")
        print(portScan.show())
        response = send(portScan,iface="en0")
        print("")
        portCounter += 1
    print(response.summary())

def sendICMP():
    #dst_ip = str(input("Dest IP > "))
    dst_ip = "127.0.0.1"
    icmpPkt = IP(dst=dst_ip,ttl=128)/ICMP()
    print("")
    # print("Sending packet now and waiting for 1 response...")
    # print("")
    print(icmpPkt.show())
    print("")
    response = srloop(icmpPkt,iface="lo0",count=4)
    print("")
    print(response[0].summary())

sendPacket()
