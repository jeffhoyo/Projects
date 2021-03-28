from scapy.all import *
import random
import os
import time

def mainMenu():

    os.system("clear")
    ## Show menu ##
    print("Packet Crafter v1")
    print(30 * '-')
    print("1. Select Interface")
    print("2. Select DST Host")
    print("3. Select DST Port")
    print("4. Select type of Packet")
    print(30 * '-')

    #Set variables to null so program knows variables are not set
    packetType = None

    ## Get input ###
    choice = int(input('Enter your choice [1-4] : '))

    ### Take action as per selected menu-option ###
    if choice == 1:
            os.system("clear")
            srcInt = str(os.system('ifconfig | grep "broadcast" | cut -d " " -f 2'))
            print(srcInt)
            time.sleep(2)
            mainMenu()
    elif choice == 2:
            os.system("clear")
            global dstHost
            dstHost = str(input("Enter destination IP: "))
            print("Destination Host set as: %s" % dstHost)
            time.sleep(2)
            mainMenu()
    elif choice == 3:
            os.system("clear")
            global dstPort
            dstPort = str(input("Enter destination Port: "))
            print("Destination Port set as: %s" % dstPort)
            print()
            print("Destination set as: %s:%s" % (dstHost,dstPort))
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
