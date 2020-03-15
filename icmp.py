# Import Scapy Library
from scapy.all import *

# Main Packet Filtering Method
def packet_callback(packet):

    # For OSX: Ethernet Frame Header does not exist
    icmp_osx = str(packet.getlayer(Loopback).type)

    # Evaluate Loopback Header for IP version, 2=IPv4, 30=IPv6
    if icmp_osx == "2":
        # print(packet.summary())
        # print(packet.getlayer(Loopback).type)
        ip_type = str(packet.getlayer(IP).proto)
        if ip_type == "1":

            icmp_type = str(packet.getlayer(ICMP).type)

            if icmp_type == "0":
                print("[%s] ICMP Echo Reply %s -> %s" % (packet.getlayer(ICMP).type,packet[IP].src, packet[IP].dst))
            elif icmp_type == "8":
                print("[%s] ICMP ECHO Request %s -> %s" % (packet.getlayer(ICMP).type,packet[IP].src, packet[IP].dst))
            elif icmp_type == "3":
                print("[%s] ICMP Traceroute Packet %s -> %s" % (packet.getlayer(ICMP).type,packet[IP].src, packet[IP].dst))
            else:
                print("[%s] ICMP Type not ECHO" % icmp_type)
                #print("ICMP Not Specified Type: %s" % icmp_type)
        elif ip_type == "6":
            print("[%s] TCP Packet Detected" % packet.getlayer(IP).proto)
        elif ip_type == "17":

            udp_ttl = str(packet.getlayer(IP).ttl)

            if udp_ttl == "1":
                print("[TTL: %s] UDP Traceroute Paket Detected" % udp_ttl)
            else:
                print("[%s] UDP Packet Detected" % packet.getlayer(IP).proto)
        else:
            print("[%s] Unknown Protocol Detected" % packet.getlayer(IP).proto)
    elif icmp_osx == "30":
        print("[%s] IPv6 Traffic Detected" % packet.getlayer(Loopback).type)
    else:
        print("Traffic does not have Loopback Header")

sniff(iface="lo0",prn=packet_callback,store=0)
