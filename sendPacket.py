from scapy.all import *
import random
import os
import time





def mainMenu():

    #Set variables to null so program knows variables are not set
    srcInt = None
    dstHost = None
    dstPort = None
    packetType = None

    os.system("clear")
    ## Show menu ##
    print("Packet Crafter v1")
    print(30 * '-')
    print("1. Select Interface")
    print("2. Select DST Host")
    print("3. Select DST Port")
    print("4. Select type of Packet")

    if srcInt is None:
        print(30 * '-')
        print("Diagnostics: ")
        print(30 * '-')
        print("Int not Selected")
    else:
        print("Int Selected")

    ## Get input ###
    choice = int(input('Enter your choice [1-4] : '))

    ### Take action as per selected menu-option ###
    if choice == 1:
            os.system("clear")
            print("en0 has been selected as INT")
            srcInt = os.system('ifconfig | grep "broadcast" | cut -d " " -f 2')
            time.sleep(2)
            mainMenu()
    elif choice == 2:
            os.system("clear")
            print("Select Destination Host")
            time.sleep(2)
            mainMenu()
    elif choice == 3:
            os.system("clear")
            print("Select DST Port")
            time.sleep(2)
            mainMenu()
    elif choice == 4:
            os.system("clear")
            print("Select type of Packet to Send")
            time.sleep(2)
            mainMenu()
    else:    ## default ##
            os.system("clear")
            print("Invalid number. Exiting to main menu...")

def sendPacket():
    portCounter = 1
    dst_ip = str(input("Please enter dst ip > "))
    while portCounter < 2:
        # randInt = random.randint(50, 80)
        dst_port = int(input("Please enter dst port > "))
        portScan = IP(dst=dst_ip)/TCP(sport=portCounter,dport=dst_port,flags="SA")
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

mainMenu()
