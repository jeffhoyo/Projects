from scapy.all import *

def packet_callback(packet):

       ether_type = str(packet.getlayer(Ether).type)
       if ether_type == "2048":

          icmp_type = str(packet.getlayer(ICMP).type)

          if icmp_type == "0":
             print("[*] ICMP Echo Reply %s -> %s" % (packet[IP].src, packet[IP].dst))
             print(ether_type)
             #print("ICMP 0 Type: %s" % icmp_type)
          elif icmp_type == "8":
             print("[*] ICMP ECHO Request %s -> %s" % (packet[IP].src, packet[IP].dst))
             print(ether_type)
             #print("ICMP 8 Type: %s" % icmp_type)
          else:
             print("[*] ICMP Type not ECHO")
             #print("ICMP Not Specified Type: %s" % icmp_type)
       print("[%s] is not valid ICMP type, skipping" % ether_type)

sniff(iface="ens33",prn=packet_callback,store=0)
