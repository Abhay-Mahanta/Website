#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if current_mac:
        return current_mac.group(0)
    else:
        print("[-] Could not find any MAC address.")

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguement():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Enter interface.")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "Enter new MAC address.")
    return parser.parse_args()

(options, arguements) = get_arguement()
interface = options.interface
new_mac = options.new_mac
current_mac = get_current_mac(interface)
print("[+] Current MAC add is: ", current_mac)
change_mac(interface, new_mac)
current_mac_after_change = get_current_mac(interface)
print("[+] MAC add is changed to: ", current_mac_after_change)