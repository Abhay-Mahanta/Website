#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    print("IP\t\t\t  MAC address\n------------------------------------------")
    for element in answered:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        
def get_arguements():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest = "target", help = "Enter ther range of IP address.")   
    options = parser.parse_args()
    return options

options = get_arguements()
scan(options.target)