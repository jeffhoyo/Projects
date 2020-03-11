from scapy.all import *

def packet_callback(packet):
       icmp_type = str(packet.getlayer(ICMP).type)
       if icmp_type != "0":
          # print("[*] ICMP Echo Request %s -> %s" % (packet[IP].src, packet[IP].dst))
	  print("ICMP 0 Type: %s" % packet.getlayer[ICMP].type)
       elif icmp_type == "0":
          # print("[*] ICMP Echo Reply %s -> %s" % (packet[IP].src, packet[IP].dst))
	  print("ICMP 8 Type: %s" % packet.getlayer[ICMP].type)
       else:
          # print("[*] Traffic Not ICMP")
          print("ICMP Not Specified Type: %s" % packet.getlayer[ICMP].type)

sniff(prn=packet_callback,store=0)
